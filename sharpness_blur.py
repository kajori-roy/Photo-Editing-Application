# Description: This module contains functions to sharpen and blur an image using the unsharp mask technique and Gaussian blur respectively.

import cv2
import numpy as np

def sharpen_image(image_path):
    """
    Sharpen the image using the unsharp mask technique. 
    The unsharp mask technique involves creating a blurred version of the image and then 
    subtracting it from the original image to enhance the edges. 
    """

    image = cv2.imread(image_path)
    blurred_image = blur_image(image_path)
    mask = cv2.subtract(image, blurred_image)
    sharpened_image = cv2.add(image, mask)
    cv2.imwrite('output_images/sharpened_image.bmp', sharpened_image)

def blur_image(image_path):
    """
    Blur the image using a Gaussian filter.

    The Gaussian filter is a low-pass filter that is used to blur the image.
    The filter is applied to each pixel in the image to create a blurred version of the image.

    The filter size is 49x49 and the padding is done using the reflect mode.

    Args:image_path: The path to the input image.
    return: The blurred image.
    """

    img = cv2.imread(image_path)
    
    filter_size = 49
    
    pad = filter_size // 2
    height, width = img.shape[:2]
    img_padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REFLECT)
    blurred_img = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            for c in range(3):  
                sum_pixels = np.sum(img_padded[y:y+filter_size, x:x+filter_size, c])
                blurred_img[y, x, c] = sum_pixels / (filter_size ** 2)
    cv2.imwrite('output_images/blurred_image.bmp', blurred_img)
    return blurred_img


