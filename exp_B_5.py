import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications import VGG19
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load and preprocess image
def load_image(path):
    img = load_img(path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return tf.keras.applications.vgg19.preprocess_input(img)

# Load images
content_image = load_image("content.jpg")
style_image = load_image("style.jpg")

# Load VGG19
vgg = VGG19(weights='imagenet', include_top=False)

# Select layers
content_layers = ['block5_conv2']
style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1']

outputs = [vgg.get_layer(name).output for name in content_layers + style_layers]
model = tf.keras.Model(vgg.input, outputs)

# Gram Matrix
def gram_matrix(x):
    x = tf.reshape(x, (-1, x.shape[-1]))
    return tf.matmul(x, x, transpose_a=True)

# Loss functions
def compute_loss(generated):
    outputs = model(generated)
    
    content_output = outputs[0]
    style_outputs = outputs[1:]

    content_loss = tf.reduce_mean((content_output - model(content_image)[0])**2)

    style_loss = 0
    for i, style_output in enumerate(style_outputs):
        gram_gen = gram_matrix(style_output)
        gram_style = gram_matrix(model(style_image)[i+1])
        style_loss += tf.reduce_mean((gram_gen - gram_style)**2)

    total_loss = content_loss + 1e-4 * style_loss
    return total_loss

# Optimization
generated = tf.Variable(content_image, dtype=tf.float32)
optimizer = tf.optimizers.Adam(learning_rate=5)

# Training loop
for i in range(100):
    with tf.GradientTape() as tape:
        loss = compute_loss(generated)
    
    grads = tape.gradient(loss, generated)
    optimizer.apply_gradients([(grads, generated)])

    if i % 10 == 0:
        print(f"Iteration {i}, Loss: {loss}")

# Display image
def deprocess(img):
    img = img.reshape((224, 224, 3))
    img = img - np.min(img)
    img = img / np.max(img)
    return img

plt.imshow(deprocess(generated.numpy()))
plt.axis('off')
plt.show()
