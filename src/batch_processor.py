import os
import cv2
from image_preprocessing import preprocess_image
from visualize_results import visualize_images

# Folders
input_folder = "output/"
enhanced_folder = os.path.join(input_folder, "enhanced")
visualization_folder = os.path.join(input_folder, "visualizations")

# Ensure output directories exist
os.makedirs(enhanced_folder, exist_ok=True)
os.makedirs(visualization_folder, exist_ok=True)

# Batch process all images in the `output` folder
def batch_process():
    image_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]

    if not image_files:
        print("❌ No images found in the output folder!")
        return

    print(f"✅ Found {len(image_files)} images. Processing...")

    for idx, image_file in enumerate(image_files, start=1):
        input_path = os.path.join(input_folder, image_file)
        enhanced_path = os.path.join(enhanced_folder, f"enhanced_{image_file}")
        visualization_path = os.path.join(visualization_folder, f"comparison_{idx}.png")

        # Preprocess image
        preprocess_image(input_path, enhanced_path)

        # Visualize original and processed images
        visualize_images(input_path, enhanced_path)

        # Save the side-by-side visualization
        original = cv2.imread(input_path)
        processed = cv2.imread(enhanced_path)

        if original is not None and processed is not None:
            combined = cv2.hconcat([original, processed])
            cv2.imwrite(visualization_path, combined)

        print(f"✅ Processed {image_file}: saved visualization at {visualization_path}")

    print("🎯 Batch processing completed successfully!")

# Execute batch processing
if __name__ == "__main__":
    batch_process()
