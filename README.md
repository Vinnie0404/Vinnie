# DL exp 1
What is Linear Regression? How does it differ from Logistic Regression?
2
Write the equation of a multiple linear regression model with n features.
3
What is the cost function used in Linear Regression? Why do we minimise it?
4
Explain Gradient Descent. How does it help find the optimal weights?
5
What does the R² score tell us? What is an ideal value?
6
What is the difference between MAE, MSE, and RMSE?
Hint: MAE is robust to outliers; MSE penalises large errors more due to squaring; RMSE is in original units.
7
Why is feature scaling important before applying Linear Regression?
8
What is multicollinearity? How does it affect the regression coefficients?
9
How do you detect and handle outliers in a regression dataset?
10
What is the difference between simple and multiple linear regression?
11
What does a positive vs negative regression coefficient mean?
12
What is the train-test split? Why don't we train and test on the same data?
13
Explain the concept of overfitting in a regression model. How can you detect it?
14
What is Ridge Regression (L2 regularisation)? How does it differ from plain Linear Regression?
15
What is Lasso Regression (L1 regularisation)? When would you prefer it over Ridge?
16
What is the Normal Equation? When is it preferred over Gradient Descent?
17
What is homoscedasticity? Why is it an assumption of Linear Regression?
18
How do residual plots help evaluate a regression model?
19
Explain the concept of the bias-variance tradeoff in regression.
20
What is cross-validation? How is k-fold CV better than a single train-test split?
21
What preprocessing steps did you apply to the USA Housing dataset?
22
How did you handle the categorical 'Address' column in the dataset?
23
What does the intercept term β₀ represent in your house price model?
24
Which feature had the highest correlation with house price? How did you find this?
25
What is the p-value of a regression coefficient? What does it tell you?
26
How would you improve the model if the RMSE was still high after Linear Regression?
27
What is polynomial regression? When would it be more appropriate than linear?
28
What is the difference between correlation and causation in your housing dataset?
29
Explain how you would deploy this trained model as an API for real estate agents.
30
What ethical concerns exist when using ML models to predict house prices?

# 2
What is a Convolutional Neural Network? How does it differ from a Dense network?
2
Explain the convolution operation. What does a 3×3 filter detect?
3
What is a feature map (activation map)? How many feature maps does Conv2D(32) produce?
4
Why do we apply ReLU activation after convolution?
5
What is MaxPooling? How does a 2×2 MaxPool change the spatial dimensions?
6
Why is Softmax used in the output layer for MNIST? Write its formula.
7
What loss function is used for multiclass classification? Write the formula.
8
What is Dropout? How does dropout = 0.5 affect a layer with 256 neurons?
9
What is Batch Normalisation? Where is it placed in the network?
10
Why do we reshape MNIST images from (28,28) to (28,28,1)?
11
What does one-hot encoding do to the label '7' in a 10-class problem?
12
What is the Adam optimiser? What makes it better than plain SGD?
13
How does EarlyStopping work? What does patience=5 mean?
14
What is a confusion matrix? How do you read it for a 10-class problem?
15
Define Precision, Recall, and F1-score in the context of digit classification.
16
What is the effect of increasing the number of filters (e.g., from 32 to 64)?
17
What is padding='same' vs padding='valid' in Conv2D?
18
How do you compute the number of trainable parameters in a Conv2D(32, (3,3)) layer?
19
What is the Flatten layer and why is it needed before Dense layers?
20
What is the difference between training accuracy and validation accuracy?
21
Which MNIST digit pairs are most commonly confused and why?
22
What is data augmentation? Give three augmentation techniques suitable for MNIST.
23
Explain the concept of receptive field in a CNN.
24
What is transfer learning? Would it be useful for MNIST? Why or why not?
25
How does ReduceLROnPlateau help during training?
26
What is the vanishing gradient problem? How do ReLU and BatchNorm help address it?
27
What is the difference between a shallow and deep CNN? What are the tradeoffs?
28
How would you handle class imbalance if digit '1' appeared 10× more than digit '5'?
29
What does model.evaluate() return and how does it differ from model.predict()?
30
How would you convert this digit classifier into a real-time handwriting recognition app?

# 3
What is a Recurrent Neural Network? What makes it suitable for sequential data?
2
What is the vanishing gradient problem in vanilla RNNs? Why does it occur?
3
Explain the architecture of an LSTM cell. What are the three gates?
4
Write the equations for the forget gate and cell state update in LSTM.
5
What is the difference between LSTM and GRU? List advantages of each.
6
What is an Embedding layer? How does it differ from one-hot encoding?
7
What is the vocabulary size parameter in Embedding? How did you choose 10,000?
8
What is sequence padding? Why is post-padding preferred for LSTM?
9
What does MAX_LEN = 300 mean? What happens to reviews longer than 300 tokens?
10
What is a Bidirectional LSTM? How does it improve sentiment analysis?
11
What is Binary Cross-Entropy loss? Write its formula.
12
What is the Sigmoid activation function? Why is it used in the output layer?
13
Explain SpatialDropout1D. How is it different from regular Dropout for sequences?
14
What is teacher forcing in sequence models? Is it used during inference?
15
What is the AUC-ROC score? What does a value of 0.92 mean?
16
How do you choose the decision threshold (default 0.5)? When would you lower it?
17
What is the difference between precision and recall? Give a sentiment analysis example.
18
How does recurrent dropout differ from regular dropout in an LSTM?
19
What is attention mechanism? How would it improve your sentiment model?
20
What is BERT? How does it outperform LSTM for sentiment tasks?
21
What is text tokenisation? Describe the process applied to IMDB reviews.
22
What is the difference between word-level and character-level models?
23
How would you handle negation in sentiment (e.g., 'not good')?
24
What is the purpose of the ReduceLROnPlateau callback in training?
25
What is SMOTE? When would you apply it to the IMDB dataset?
26
How would you extend this binary classifier to a 5-star rating predictor?
27
What is the effect of doubling the LSTM units from 64 to 128?
28
What does the training loss vs. validation loss graph tell you after 15 epochs?
29
How would you interpret the model's output of 0.82 for a movie review?
30
What are the limitations of LSTM for very long documents (e.g., 10,000 words)?

# 4
What is hyperparameter tuning? How does it differ from training (learning parameters)?
2
How does the learning rate affect convergence? What happened at LR = 0.1 vs 0.0001?
3
Compare SGD, Adam, and RMSprop. Which worked best in your experiment and why?
4
What is the effect of filter size (3×3 vs 5×5 vs 7×7) on feature extraction?
5
How does increasing the number of convolutional layers affect the model?
6
What is Transfer Learning? Name two pre-trained models and when you'd use them.
7
What is fine-tuning in transfer learning? How did you apply it?
8
What is Data Augmentation? List 5 techniques and explain each.
9
What is the ImageDataGenerator in Keras? How did you configure it?
10
What is Dropout regularisation? How does dropout=0.4 affect a Dense(512) layer?
11
What is L2 regularisation (weight decay)? How does it prevent overfitting?
12
What is GlobalAveragePooling2D? When is it preferred over Flatten?
13
Explain the concept of receptive field and how it grows with network depth.
14
What is Grid Search? How did you use it to tune hyperparameters?
15
What is Random Search? Why is it sometimes better than Grid Search?
16
What is the difference between overfitting and underfitting? How did your training curves indicate which occurred?
17
What is class activation mapping (CAM)? How does it help interpret CNN decisions?
18
Why is it important to use a separate validation set during hyperparameter tuning?
19
What is Batch Size? How does choosing batch=32 vs batch=256 affect training?
20
What is the difference between local minima, global minima, and saddle points in optimisation?
21
What is weight initialisation? Why does it matter for deep CNN training?
22
What is a learning rate scheduler? Describe the ReduceLROnPlateau strategy.
23
Why is it important to freeze base model layers during the first training phase of transfer learning?
24
What metrics beyond accuracy would you use for an imbalanced medical image dataset?
25
How do you prevent data leakage when using augmentation with train/test split?
26
What is the purpose of the Sigmoid activation in a binary image classifier output?
27
What is Grad-CAM? How does it differ from basic CAM?
28
How would you handle a medical imaging dataset with only 500 labelled images?
29
What is the confusion matrix for binary image classification? Define TP, TN, FP, FN.
30
What hardware would you recommend for training deep CNNs and why?

# 5

# BI exp1
Assignment 1
Data Import from Multiple Sources
Excel, SQL Server, Oracle, CSV · ETL integration

0 / 30 revealed
1
What is Business Intelligence (BI)? How does data import fit into the BI lifecycle?
2
What are the most common data sources used in a BI project? Give five examples.
3
What is a flat file? How does importing an Excel file differ from importing a CSV?
4
What is a database connection string? Write an example for SQL Server.
5
What is ODBC? How does it allow connection to different databases?
6
What is OLEDB? How does it differ from ODBC?
7
What is a JDBC driver? In which tools is it commonly used?
8
What is Power Query in Power BI? How does it help import data from multiple sources?
9
What steps would you follow to import data from Oracle into SQL Server?
10
What is schema-on-read vs schema-on-write? Give an example of each.
11
What is data type mismatch? How do you handle it during import?
12
What is a primary key? Why is it important when importing into a relational target?
13
What is data profiling? What metrics do you capture before importing?
14
How do you import data from a REST API into Power BI?
15
What is an SSIS package? List its main components.
16
What is a staging area in a data warehouse? Why is raw data loaded there first?
17
What is the difference between a full load and an incremental (delta) load?
18
What is a watermark in incremental data loading? How is it implemented?
19
What are orphan records? How do you detect them during import?
20
What is data masking? When is it applied during import?
21
What is a linked server in SQL Server? How is it used to import from Oracle?
22
What is the difference between structured, semi-structured, and unstructured data? Give examples.
23
How would you handle importing a 10GB Excel file efficiently?
24
What is data latency? How does the choice of import method affect it?
25
What is a connection manager in SSIS? What properties does it store?
26
What is the difference between append mode and overwrite mode during import?
27
How do you import JSON data into SQL Server?
28
What is a data catalog? How does it help manage multiple data sources?
29
What is ETL metadata? Give examples of metadata tracked during import.
30
What security considerations must you address when importing data from external sources?

#2
signment 2
Data Visualization from ETL Process
Power BI / Tableau / Python · Charts, Dashboards, KPIs

0 / 30 revealed
1
What is data visualisation in the context of a BI project? Why is it important?
2
What is the difference between a report and a dashboard in Power BI?
3
What is a KPI (Key Performance Indicator)? Give three examples used in sales analytics.
4
What chart type is best for showing trends over time? Why?
5
When would you use a bar chart vs a column chart?
6
What is a heatmap? How is it useful after the ETL process?
7
What is a scatter plot? What relationship does it help visualise?
8
What is a pie chart vs a donut chart? When should you avoid using a pie chart?
9
What is DAX in Power BI? Give an example of a calculated measure.
10
What is Power Query M language? How is it used after ETL?
11
What is drill-through in Power BI? How does it help analysts?
12
What is a slicer in Power BI? How does it interact with visuals?
13
What is row-level security (RLS) in Power BI? Why is it important after ETL?
14
What is a calculated column vs a measure in Power BI? When to use each?
15
What is a star schema? How does it improve visualisation performance in Power BI?
16
What is data granularity? How does the grain of your ETL output affect visualisations?
17
What is a waterfall chart? Give a business use case.
18
What is a funnel chart? Where is it typically used in BI dashboards?
19
What are bookmarks in Power BI? How do they improve dashboards?
20
What is conditional formatting in Power BI tables? Give an example.
21
What is the difference between a live connection and an import mode in Power BI?
22
What is a decomposition tree visual? How does it help with root cause analysis?
23
What is the importance of colour theory in data visualisation?
24
What is a sparkline? Where are they useful in dashboards?
25
How do you publish a Power BI report to the Power BI Service?
26
What is a paginated report in Power BI? How does it differ from standard reports?
27
How do you schedule automatic data refresh in Power BI Service?
28
What is the Q&A visual in Power BI? Give an example query.
29
What are tooltips in Power BI? How can you customise them?
30
How does data accuracy in the ETL process directly impact visualisation quality?

#3
nment 3
ETL Process – SQL Server / Power BI
Extraction, Transformation, Loading · SSIS · Data Warehouse

0 / 30 revealed
1
What is ETL? Explain each phase with an example.
2
What is a data warehouse? How does it differ from an OLTP database?
3
What is SSIS? What are its main components?
4
What is the difference between OLTP and OLAP?
5
What is a Data Flow Task in SSIS? What transformations can it contain?
6
What is a Lookup Transformation in SSIS? Give a real-world use case.
7
What is a Derived Column transformation in SSIS? Give an example.
8
What is a Slowly Changing Dimension (SCD)? Explain Type 1 and Type 2.
9
What is a surrogate key? Why is it preferred over a natural key in a data warehouse?
10
What is a fact table? What is a dimension table? Give examples of each.
11
What is the difference between a star schema and a snowflake schema?
12
What is a Control Flow in SSIS? Name three control flow tasks.
13
What is an Execute SQL Task in SSIS? Give two use cases.
14
What is incremental loading in ETL? How do you implement it using a watermark?
15
What is data cleansing? Name five common cleansing operations.
16
What is a null value? How do you handle nulls during the transformation phase?
17
What is deduplication in ETL? How do you detect and remove duplicate records?
18
What is data normalisation vs denormalisation in the context of ETL?
19
What is an error row redirect in SSIS Data Flow?
20
What is the difference between truncate-and-reload vs upsert (merge)?
21
Write a SQL MERGE statement example for loading a dimension table.
22
What is a package configuration in SSIS? Why is it used?
23
What is logging in SSIS? What events do you typically log?
24
What is Power BI Dataflow? How does it relate to ETL?
25
What is a staging database? How does it differ from a data warehouse?
26
What is partitioning in a data warehouse table? How does it improve ETL performance?
27
What is a checksum in ETL? How is it used to detect changed records?
28
What is the difference between a Type 3 SCD and Type 2 SCD?
29
What is a business key vs a surrogate key in a dimension table?
30
What is data lineage? Why is it important in a BI project?

#4
ssignment 4
Data Analysis and Visualization – Advanced Excel
PivotTables, VLOOKUP, Charts, What-If Analysis, Macros

0 / 30 revealed
1
What is a PivotTable in Excel? How do you create one from a dataset?
2
What is a PivotChart? How does it relate to a PivotTable?
3
What is VLOOKUP? Write its syntax and explain each argument.
4
What is HLOOKUP? When would you use it instead of VLOOKUP?
5
What is the INDEX-MATCH formula? How is it better than VLOOKUP?
6
What is XLOOKUP? How does it improve upon VLOOKUP?
7
What is an array formula in Excel? Give an example using SUMPRODUCT.
8
What are conditional formatting rules? Give a business example.
9
What is the SUMIF function? How does it differ from SUMIFS?
10
What is COUNTIF? Write an example to count orders with status 'Pending'.
11
What is an Excel Slicer? How does it differ from a filter dropdown?
12
What is Goal Seek in Excel? Give a use case.
13
What is Scenario Manager in Excel? How does it differ from Goal Seek?
14
What is a Data Table (What-If Analysis)? Explain a one-variable data table.
15
What is Power Pivot in Excel? What does it add to standard PivotTables?
16
What is a named range in Excel? How does it improve formula readability?
17
What is the difference between absolute and relative cell references?
18
What is an Excel Macro? How do you record one for repetitive tasks?
19
What is VBA in Excel? Write a simple Sub to display a message box.
20
What is the difference between a workbook, worksheet, and cell range?
21
What is Excel's Data Validation feature? Give two use cases.
22
What is the TEXT function in Excel? Give an example.
23
What is an Excel Dashboard? What elements make a good BI dashboard?
24
What is Power Query in Excel? How does it help with ETL inside Excel?
25
What is Get & Transform (Power Query)? How do you merge two tables?
26
What is the IFERROR function? How is it used with VLOOKUP?
27
What is a dynamic array formula in Excel 365? Give an example using FILTER.
28
What is the difference between AVERAGE, MEDIAN, and MODE in Excel?
29
How would you create a sales trend line chart in Excel? Describe the steps.
30
What is a sparkline in Excel? How do you insert one in a dashboard?

#5
Assignment 5
Data Classification Algorithm
Decision Tree, Naive Bayes, KNN, SVM · Scikit-learn / WEKA

0 / 30 revealed
1
What is data classification in machine learning? How does it differ from regression?
2
What is a Decision Tree classifier? Explain how it splits data at each node.
3
What is Information Gain? How is it used in Decision Tree construction?
4
What is Gini Impurity? Write its formula and compare it with entropy.
5
What is the Naive Bayes classifier? What assumption makes it 'naive'?
6
Write Bayes' Theorem and explain each term in the context of classification.
7
What is a K-Nearest Neighbours (KNN) classifier? How does it make predictions?
8
How do you choose the value of K in KNN? What happens with very small or large K?
9
What is a Support Vector Machine (SVM)? What is a hyperplane?
10
What is the kernel trick in SVM? Name three kernels.
11
What is a Random Forest? How does it improve over a single Decision Tree?
12
What is bagging (Bootstrap Aggregating)? How is it used in Random Forest?
13
What is a confusion matrix? Define TP, TN, FP, FN for a binary classifier.
14
What is accuracy? When is it a misleading metric?
15
What is Precision? What is Recall? When do you prioritise each?
16
What is the F1-Score? Write its formula. When is it preferred over accuracy?
17
What is a ROC curve? What does the AUC value represent?
18
What is cross-validation? How does 10-fold CV work?
19
What is overfitting in a Decision Tree? How do pruning and max_depth prevent it?
20
What is feature importance in a Random Forest? How is it computed?
21
What is the difference between hard and soft margin SVM?
22
What is stratified sampling in train-test split? Why is it important?
23
What is Label Encoding vs One-Hot Encoding? When should you use each?
24
What is Gradient Boosting? How does it differ from Random Forest?
25
What is XGBoost? Why is it popular for classification tasks in BI?
26
What is the effect of class imbalance on a classifier? How do you handle it?
27
What is a learning curve? What does it tell you about your model?
28
What is hyperparameter tuning for a Decision Tree? Which parameters did you tune?
29
What is WEKA? How did you use it to apply a classification algorithm?
30
How would you explain your classification model's decision to a non-technical manager?
