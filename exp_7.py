import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications import VGG19
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load image
def load_image(path):
    img = load_img(path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return tf.keras.applications.vgg19.preprocess_input(img)

content = load_image("C:\BE sem8\CL_3\content.jpeg")
style = load_image("C:\BE sem8\CL_3\style.jpeg")

# Load model
vgg = VGG19(weights='imagenet', include_top=False)

# Select layers
content_layers = ['block5_conv2']
style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1']

outputs = [vgg.get_layer(name).output for name in content_layers + style_layers]
model = tf.keras.Model(vgg.input, outputs)

# Gram matrix
def gram_matrix(x):
    x = tf.reshape(x, (-1, x.shape[-1]))
    return tf.matmul(x, x, transpose_a=True)

# Loss function
def compute_loss(gen):
    outputs = model(gen)
    
    content_loss = tf.reduce_mean((outputs[0] - model(content)[0])**2)

    style_loss = 0
    for i in range(len(style_layers)):
        gram_gen = gram_matrix(outputs[i+1])
        gram_style = gram_matrix(model(style)[i+1])
        style_loss += tf.reduce_mean((gram_gen - gram_style)**2)

    return content_loss + 1e-4 * style_loss

# Optimization
generated = tf.Variable(content, dtype=tf.float32)
optimizer = tf.optimizers.Adam(learning_rate=0.01)

for i in range(100):
    with tf.GradientTape() as tape:
        loss = compute_loss(generated)
    
    grads = tape.gradient(loss, generated)
    optimizer.apply_gradients([(grads, generated)])

    if i % 10 == 0:
        print(f"Iteration {i}, Loss: {loss}")

# Show image
def deprocess(img):
    img = img.reshape((224, 224, 3))
    img = img - np.min(img)
    img = img / np.max(img)
    return img

plt.imshow(deprocess(generated.numpy()))
plt.axis('off')
plt.show()
