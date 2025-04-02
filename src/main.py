import os

# Run the full pipeline
print("🚀 Running Strikeout Recognition Pipeline...")

os.system("python src/preprocessing.py")
os.system("python src/graph_builder.py")
os.system("python src/svm_classifier.py")
os.system("python src/strikeout_removal.py")

print("🎯 Pipeline completed! Check the 'output' folder for results.")
