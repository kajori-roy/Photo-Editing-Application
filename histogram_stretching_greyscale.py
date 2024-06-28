import cv2
import numpy as np

def auto_level_image(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale for simplicity
    # Skip this step if you want to process a colored image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the minimum and maximum pixel values
    min_val, max_val, _, _ = cv2.minMaxLoc(gray)

    # Stretch the histogram
    stretched = 255 * (gray - min_val) / (max_val - min_val)
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)

    # Save or show the result
    cv2.imwrite(output_path, stretched)
    cv2.imshow("Stretched Image", stretched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = 'image1.bmp'
output_image_path = '/output/image1_stretched.bmp'
auto_level_image(input_image_path, output_image_path)
