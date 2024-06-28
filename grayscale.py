# Description: This modulecontains the function to convert an image to grayscale.

import cv2
import numpy as np

def grayscale(image, output_file_name):
    """Convert the image to grayscale.
    
    Args:
        image: The path to the image file.
        output_file_name: The name of the output file.
        
    Returns:
        The path to the output file.
    """

    
    image = cv2.imread(image)
    # Convert the image to grayscale manually
    # OpenCV loads an image in BGR format, so we need to consider that
    height, width, _ = image.shape
    grayscale_img = np.zeros((height, width), np.uint8)
    
    for i in range(height):
        for j in range(width):
            b, g, r = image[i, j]
            y = int(0.114 * b + 0.587 * g + 0.299 * r)
            grayscale_img[i, j] = y

    output_file = 'output_images/'+ output_file_name 
    cv2.imwrite(output_file, grayscale_img)
    return grayscale_img

    