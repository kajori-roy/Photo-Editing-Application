# Description: This module resizes an image to the specified width and height.

import cv2
import numpy as np

def resize_image(width, height, image_path):
    """Resize the image to the specified width and height. 

    
    Args:
        width: The width of the resized image.
        height: The height of the resized image.
        image_path: The path to the image to be resized.
        
        Returns:    None
        
        """

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image could not be read.")
        return

    original_height, original_width = img.shape[:2]

    
    width_scale = original_width / width
    height_scale = original_height / height

    
    resized_img = np.zeros((height, width, 3), dtype=np.uint8)

    for y_new in range(height):
        for x_new in range(width):
            
            x_old = int(x_new * width_scale)
            y_old = int(y_new * height_scale)

            
            x_old = min(x_old, original_width - 1)
            y_old = min(y_old, original_height - 1)

            
            resized_img[y_new, x_new] = img[y_old, x_old]

    cv2.imwrite('output_images/resized_image.bmp', resized_img)


