import cv2
import os
import pickle
import numpy as np

# Paths
model_path = os.path.join("models", "svm_model.pkl")
input_folder = os.path.join("output", "enhanced")
output_folder = os.path.join("output", "visualizations")

# Ensure the folders exist
os.makedirs(output_folder, exist_ok=True)

# Load the SVM model
try:
    with open(model_path, "rb") as f:
        svm_model = pickle.load(f)
    print("✅ SVM model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading SVM model: {e}")
    exit()

# Process all enhanced images
image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

if not image_files:
    print("❌ No enhanced images found!")
else:
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"❌ Error reading image: {image_file}")
            continue

        print(f"✅ Processing: {image_file}")

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        adaptive_thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
        )

        # Morphological operations
        kernel = np.ones((1, 20), np.uint8)  # Larger kernel for strike removal
        cleaned = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

        # Contour detection for visualization
        contours, _ = cv2.findContours(
            cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Draw contours for visualization
        vis_image = image.copy()
        cv2.drawContours(vis_image, contours, -1, (0, 255, 0), 2)

        # Save the processed image and visualization
        output_path = os.path.join(output_folder, f"processed_{image_file}")
        visualization_path = os.path.join(output_folder, f"visual_{image_file}")

        cv2.imwrite(output_path, cleaned)
        cv2.imwrite(visualization_path, vis_image)

        print(f"✅ Processed image saved: {output_path}")
        print(f"✅ Visualization saved: {visualization_path}")

print("🎯 Strikeout removal with visualization completed!")
