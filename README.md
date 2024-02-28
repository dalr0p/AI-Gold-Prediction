## AI-Gold-Prediction

![Default_Im_developing_an_AI_that_can_predict_gold_prices_I_wan_0](https://github.com/dalr0p/AI-Gold-Prediction/assets/137183562/8b072eb7-292c-4940-b1ae-7a5dbbb2d887)

# Overview
This project aims to predict the price of gold using machine learning techniques. Gold price prediction has significant implications for investors, traders, and financial analysts, as it can help in making informed decisions regarding investments and portfolio management.

# Dataset
The dataset used in this project was obtained from many sources to get the best results possible. It consists of historical gold prices, including the opening price, daily high and low, closing price, adjusted closing price, and trading volume. The data was collected over a period of 1 month for the collection and cleanning.

# Data Preprocessing
Before training the machine learning model, the dataset underwent preprocessing to ensure it was suitable for training. This involved:

- Parsing date strings into datetime objects for time-series analysis.
- Removing commas from numeric columns and converting them to float data type.
- Handling missing values and outliers appropriately.
  
# Model Selection
For this project, a Random Forest Regressor model was chosen for predicting gold prices. Random Forest is an ensemble learning method that builds multiple decision trees and merges their predictions to improve accuracy and reduce overfitting. It is well-suited for regression tasks and has proven to be effective in various domains.

# Model Training
The Random Forest model was trained using the scikit-learn library in Python. The training data consisted of features such as opening price, daily high and low, and trading volume, while the target variable was the closing price of gold. The dataset was split into training and testing sets to evaluate the model's performance.

# Evaluation
The trained model was evaluated using various metrics, including Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared (R²) score. These metrics provide insights into the model's accuracy and ability to generalize to new, unseen data. Additionally, visualizations such as scatter plots and time-series plots were used to analyze the model's predictions compared to actual gold prices.

# Results
Performance metrics:

Mean Squared Error (MSE): 0.0142
Mean Absolute Error (MAE): 0.0716
R-squared (R²): 0.8364
These results indicate a strong model performance, with the R² value suggesting that approximately 83.64% of the variance in the gold prices is explained by the model. The relatively low MSE and MAE values further affirm the model's accuracy in predicting future gold prices.
In this image we can observe the first graphic is the actual gold price the second one the predicted price and the third one both combined is that accurate that the red overlaps the blue.

![image](https://github.com/dalr0p/AI-Gold-Prediction/assets/137183562/93abf2b7-a2cd-4718-a8e4-65ebe57d3c91)
