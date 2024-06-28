# Description: This module adjusts the hue and saturation of an image.
import cv2
import numpy as np

def adjust_saturation_hue(image_path, saturation_shift, hue_shift, output_path):
    """Adjust the hue and saturation of an image. 
    The hue shift is applied to the hue channel.
    The saturation shift is applied to the saturation channel.

    
    Args:
    image_path: The path to the input image.
    saturation_shift: The shift in saturation.
    hue_shift: The shift in hue.
    output_path: The path to save the adjusted image.
    
    Returns:
    A tuple. The first element is a boolean indicating if the image was adjusted successfully.
    The second element is a string with a message.
    """

    image = cv2.imread(image_path)
    if image is None:
        return False, "Error: Could not read image."

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    hsv_image[:, :, 0] = (hsv_image[:, :, 0].astype(int) + hue_shift) % 180

    saturation = hsv_image[:, :, 1].astype(int) + saturation_shift
    saturation = np.clip(saturation, 0, 255)
    hsv_image[:, :, 1] = saturation.astype(np.uint8)

    adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    cv2.imwrite(output_path, adjusted_image)
    return True, "Image adjusted successfully."
