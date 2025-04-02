import cv2
import os
import matplotlib.pyplot as plt

# Paths
enhanced_folder = os.path.join("output", "enhanced")
processed_folder = os.path.join("output", "visualizations")

# List of image files
image_files = [f for f in os.listdir(enhanced_folder) if f.endswith('.png')]

if not image_files:
    print("❌ No enhanced images found!")
else:
    for image_file in image_files:
        enhanced_path = os.path.join(enhanced_folder, image_file)
        processed_path = os.path.join(processed_folder, f"processed_{image_file}")

        enhanced = cv2.imread(enhanced_path)
        processed = cv2.imread(processed_path)

        # Display images side by side
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        axs[0].imshow(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))
        axs[0].set_title("Enhanced Image")
        axs[1].imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
        axs[1].set_title("Strikeout Removed")

        plt.show()
