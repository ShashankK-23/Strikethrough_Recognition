import pickle
import os
import numpy as np

# Paths
model_path = os.path.join("models", "svm_model.pkl")

# Load the SVM model
try:
    with open(model_path, "rb") as f:
        svm_model = pickle.load(f)
    print("✅ SVM model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading SVM model: {e}")
    exit()

# Provide test data with 2 features
test_data = np.array([[1.5, 2.8]])

try:
    prediction = svm_model.predict(test_data)
    print(f"🔍 Prediction: {prediction}")
except Exception as e:
    print(f"❌ Error during prediction: {e}")
