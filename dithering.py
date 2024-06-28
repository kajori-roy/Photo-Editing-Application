# Description: This module contains the the function for dithering an image using ordered dithering.

import cv2
import numpy as np
import os
import grayscale

def ordered_dithering(img, matrix):
    """
    Perform ordered dithering on the input image using 
    the specified dither matrix.
    Bayer matrices are commonly used for ordered dithering.
    

    Args:
        img: The input color image.
        matrix: The dither matrix to use for ordered dithering.
    
    Returns:
        The dithered image.
    """
    norm_matrix = matrix / np.max(matrix) * 255
    threshold_matrix = np.tile(norm_matrix, (img.shape[0] // matrix.shape[0] + 1, img.shape[1] // matrix.shape[1] + 1))
    threshold_matrix = threshold_matrix[:img.shape[0], :img.shape[1]]

    dithered_img = np.where(img > threshold_matrix, 255, 0)
    return dithered_img.astype(np.uint8)

def dither(image_path, output_file):
    """
    Perform ordered dithering on the input image using a 4x4 Bayer matrix.
    The dithered image is saved to the output file.

    Args:
        image_path: The path to the input image.
        output_file: The name of the output file to save the dithered image.

    Returns:
        None
    """
    # img = cv2.imread(image_path)
    
    gray_img = grayscale.grayscale(image_path, 'gray_image.bmp')
    
    # 4x4 Bayer matrix
    bayer_matrix_4x4 = np.array([
        [ 0,  8,  2, 10],
        [12,  4, 14,  6],
        [ 3, 11,  1,  9],
        [15,  7, 13,  5]
    ])
    
    dithered_img = ordered_dithering(gray_img, bayer_matrix_4x4)
    
    combined_img = np.concatenate((gray_img, dithered_img), axis=1)
    
    output_path= os.getcwd() + '/output_images/'+ output_file
    cv2.imwrite(output_path , combined_img)


    