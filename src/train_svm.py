import pickle
from sklearn.svm import SVC
from sklearn.datasets import make_classification

# Create sample data (replace with your real data)
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_informative=2, n_redundant=0, random_state=42)

# Train SVM model
svm_model = SVC(kernel='linear', C=1.0)
svm_model.fit(X, y)

# Save the model using pickle with the current version
with open("models/svm_model.pkl", "wb") as f:
    pickle.dump(svm_model, f)

print("✅ New SVM model trained and saved successfully!")
