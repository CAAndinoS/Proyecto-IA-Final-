import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# Load and preprocess the data
data = pd.read_csv("https://drive.google.com/u/0/uc?id=12V9a2jg-pw0JPNngvlFIKfIqFZTXmAN8&export=download")

# Replacing "No" and "Yes" values with 0 and 1 in columns with categorical data
data["gender"] = data["gender"].map({"male": 0, "female": 1, "other": 2})
data["hypertension"] = data["hypertension"].map({"No": 0, "Yes": 1})
data["heart_disease"] = data["heart_disease"].map({"No": 0, "Yes": 1})
data["smoking_history"] = data["smoking_history"].map({"not current": 0, "former": 1, "No Info": 2, "current": 3, "never": 4, "ever": 5})

# Separate features and target variable
X = data.drop("diabetes", axis=1)
y = data["diabetes"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Get the number of features (fields) used to train the model
num_train_features = X_train.shape[1]
print("Number of fields used to train the model:", num_train_features)

# Train the XGBoost model
model = XGBClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model on the test set
accuracy = model.score(X_test, y_test)
print("Model accuracy on the test set:", accuracy)

# Save the trained model to a .pkl file
joblib.dump(model, "model.pkl")
print("XGBoost model saved successfully.")



