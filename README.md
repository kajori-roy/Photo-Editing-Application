# Mini-Photoshop Application

## Overview

The Mini-Photoshop application is a simplified version of Adobe Photoshop designed for basic image manipulation tasks. Developed as part of the CMPT 820 Multimedia Systems course at Simon Fraser University, this project aims to provide a user-friendly graphical interface for performing essential image editing operations.

## Features

### Core Operations
- **Open File:** Load images into the application for editing.
- **Grayscale Conversion:** Convert images to grayscale.
- **Ordered Dithering:** Apply ordered dithering to simulate grayscale images on binary displays.
- **Auto Level Adjustment:** Enhance image contrast using histogram stretching.
- **Huffman Coding:** Perform image compression using Huffman coding.

### Optional Features
- **Blur Effect:** Apply Gaussian blur to images.
- **Sharpening:** Enhance image details using the unsharp mask technique.
- **Image Rotation:** Rotate images by 90 degrees clockwise.
- **Image Resizing:** Resize images to specified dimensions.
- **Hue and Saturation Adjustment:** Adjust the hue and saturation of images.
- **Save Image:** Save edited images to a specified location.

## Tools and Technologies Used
- **Python:** Primary programming language for the project.
- **OpenCV:** Library for computer vision and image processing tasks.
- **Tkinter:** Standard GUI toolkit for Python.
- **NumPy:** Fundamental package for scientific computing with Python.

## Installation
1. Clone the repository:

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python main.py
    ```
2. Use the GUI to open an image and apply various editing operations.

## Project Structure
- `main.py`: Main entry point for the application.
- `core_operations/`: Directory containing implementations of core image processing operations.
- `optional_features/`: Directory containing implementations of additional image processing features.
- `gui/`: Directory containing GUI-related code.
- `images/`: Directory for storing sample images and processed results.

## Challenges and Solutions
- **Manual Implementation of Image Processing Functions:** Developed custom functions for resizing, rotation, and hue/saturation adjustments without relying on high-level OpenCV functions.
- **Memory Leak:** Ensured graceful exit of the UI and process through proper use of `root.quit()` and `sys.exit()`.
- **GUI Responsiveness and Usability:** Optimized operations for efficiency and provided feedback mechanisms to keep users informed.

## Results and Discussion
The application successfully implements the core and optional image processing features, demonstrating a comprehensive understanding of multimedia systems and their applications in software development. The project highlights the importance of user-friendly interfaces in making advanced image processing accessible to a broader audience.



## Contact
**Kajori Roy**  
Email: [rkajori21@gmail.com](mailto:rkajori21@gmail.com)  
LinkedIn: [Kajori Roy](https://www.linkedin.com/in/kajori-roy-823b83147/)  
GitHub: [kajori-roy](https://github.com/kajori-roy)
