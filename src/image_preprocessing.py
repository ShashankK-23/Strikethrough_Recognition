import cv2
import numpy as np
import os

# Ensure the output directories exist
output_folder = os.path.join("output", "enhanced")
os.makedirs(output_folder, exist_ok=True)

def preprocess_image(image_path, output_path):
    """
    Preprocess the image with adaptive thresholding and Gaussian blur.
    
    Args:
    - image_path (str): Path to the input image.
    - output_path (str): Path to save the processed image.
    """
    image = cv2.imread(image_path)

    if image is None:
        print(f"❌ Error: Could not read image at {image_path}")
        return

    print("✅ Image loaded successfully!")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive thresholding
    binary = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )

    # Save preprocessed image
    cv2.imwrite(output_path, binary)
    print(f"✅ Preprocessed image saved at: {output_path}")
