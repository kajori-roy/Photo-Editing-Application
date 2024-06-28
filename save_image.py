# Description: This module contains the function to save the edited image to the specified destination.

import cv2

def save_file(output_file , destination_filepath):
    """Save the edited image to the specified destination."""

    image = cv2.imread(output_file)
    destination_directory = destination_filepath
    cv2.imwrite(destination_directory, image)