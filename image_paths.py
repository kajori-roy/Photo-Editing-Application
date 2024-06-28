# Description: This file contains functions that create directories for saving images.

import os
import shutil


def make_output_path():
    """Create the output_images directory if it does not exist."""

    directory = os.path.join(os.getcwd(), 'output_images')
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    else:
        print(f"Directory '{directory}' already exists.")


def make_saved_path():
    """Create the saved_images directory if it does not exist."""

    directory = os.path.join(os.getcwd(), 'saved_images')
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    else:
        print(f"Directory '{directory}' already exists.")

def make_histogram_path():
    """Create the histograms directory if it does not exist."""

    directory = os.path.join(os.getcwd(), 'histograms')
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    else:
        print(f"Directory '{directory}' already exists.")


    

