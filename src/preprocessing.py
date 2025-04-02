import cv2
import os
import numpy as np

# Folders for input and output
input_folder = "raw_images"
output_folder = os.path.join("output", "enhanced")

# Ensure output folders exist
os.makedirs(output_folder, exist_ok=True)

def preprocess_image(input_path, output_path):
    """Enhanced Preprocessing with Adaptive Threshold and Morphology"""
    
    image = cv2.imread(input_path)

    if image is None:
        print(f"❌ Error: Could not read image at {input_path}")
        return

    print(f"✅ Processing image: {input_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding (better for varied lighting)
    adaptive_thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # Morphological transformations to detect lines
    kernel = np.ones((1, 10), np.uint8)  # Horizontal kernel for strike lines
    dilated = cv2.dilate(adaptive_thresh, kernel, iterations=1)

    # Invert colors for better processing
    inverted = cv2.bitwise_not(dilated)

    # Save preprocessed image
    cv2.imwrite(output_path, inverted)
    print(f"✅ Enhanced image saved at: {output_path}")

def batch_preprocess():
    """ Batch preprocess all images from raw_images to output/enhanced. """
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("❌ No images found in raw_images.")
        return

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, f"enhanced_{image_file}")

        preprocess_image(input_path, output_path)

    print("🎯 Batch preprocessing completed!")

if __name__ == "__main__":
    batch_preprocess()
