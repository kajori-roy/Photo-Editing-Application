# Description: This module contains functions to apply histogram stretching to a color image.

import cv2
import numpy as np
import matplotlib.pyplot as plt


def auto_level_color_image(img, output_image):
    """
    Apply histogram stretching to a color image. This function stretches
    the histogram of each channel of the input image to cover the full 
    intensity range [0, 255].

    Args:
        img: Path to the input image.
        output_image: Name of the output image file.
        
        Returns:
        Path to the output image.
        
    """

    plot_histogram(img,"original_histogram.png")
    image = cv2.imread(img)
    channels = cv2.split(image)
    leveled_channels = []

    for channel in channels:
        min_val, max_val, _, _ = cv2.minMaxLoc(channel)
        if max_val - min_val > 0:
            stretched = 255 * (channel - min_val) / (max_val - min_val)
            leveled_channels.append(np.clip(stretched, 0, 255).astype(np.uint8))
        else:
            leveled_channels.append(channel)

    leveled_img = cv2.merge(leveled_channels)
    output_file = 'output_images/'+ output_image
    cv2.imwrite(output_file, leveled_img)
    plot_histogram(output_file, "auto_level_histogram.png")
    return output_file

def plot_histogram(img, output_image):
    image = cv2.imread(img)
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    for channel, color in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    output_plot = 'histograms/'+ output_image
    plt.savefig(output_plot)
    








