# Description: This module contains functions to Rotate the image.
import cv2
import os
import numpy as np

def rotate(original_image_path):
    """Rotate the image by 90 degrees clockwise.
    
    Args:
        original_image_path: The path to the original image.

    Returns:    None   
    """
    angle = 90

    rotated_image_path = 'output_images/rotated_image.bmp'
    if os.path.exists(rotated_image_path):
        image_path = rotated_image_path
    else:
        image_path = original_image_path

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        exit()


    height, width = image.shape[:2]

    
    angle_rad = np.radians(angle)

    
    new_width = int(abs(width * np.cos(angle_rad)) + abs(height * np.sin(angle_rad)))
    new_height = int(abs(height * np.cos(angle_rad)) + abs(width * np.sin(angle_rad)))

    
    rotated_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    
    original_center = (width / 2, height / 2)
    new_center = (new_width / 2, new_height / 2)

    for y_new in range(new_height):
        for x_new in range(new_width):
            
            x_old = (x_new - new_center[0]) * np.cos(-angle_rad) - (y_new - new_center[1]) * np.sin(-angle_rad) + original_center[0]
            y_old = (x_new - new_center[0]) * np.sin(-angle_rad) + (y_new - new_center[1]) * np.cos(-angle_rad) + original_center[1]

            
            x_old, y_old = int(round(x_old)), int(round(y_old))
            if 0 <= x_old < width and 0 <= y_old < height:
                rotated_image[y_new, x_new] = image[y_old, x_old]

    

    cv2.imwrite(rotated_image_path, rotated_image)

