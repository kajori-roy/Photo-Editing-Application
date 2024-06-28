# Description: This module deletes all files in the output_images directory.

import os

def delete_images():
    """Delete all files in the output_images directory.
    """
    directory = os.path.join(os.getcwd(), 'output_images')

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
