# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

# Load the dataset
df = pd.read_excel('C:\\Users\\marco\\Downloads\\AI\\Training\\final.xlsx')  # Update this to the path of your dataset

# Preprocess the data
# Define features and target variable
X = df.drop(['Date', 'Price'], axis=1)  # Dropping 'Date' and assuming 'Price' is the target
y = df['Price']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}, MAE: {mae}, R²: {r2}')

# Save the trained model
joblib.dump(rf_model, 'random_forest_gold_price_predictor.joblib')
