"""A Hue and Saturation Adjustment window."""


import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from adjust_hue_saturation import adjust_saturation_hue  # Ensure this is implemented correctly

class HueSaturationEditor:
    """A Hue and Saturation Adjustment window.
    
    Attributes: 
    top: The top-level window.
    image_path: The path to the original image.
    temp_path: The path to the temporary adjusted image.
    display_image: The displayed image.
    adjusted_image: The adjusted image.
    image_frame: The frame to display the image.
    image_label: The label to display the image.
    controls_frame: The frame to display the controls.
    saturation_scale: The scale to adjust the saturation.
    hue_scale: The scale to adjust the hue.
    exit_button: The button to exit the editor.

    Methods:
    close_editor: Close the editor window.
    load_image: Load the original image and display it.
    adjust_image: Adjust the image based on the saturation and hue values.
    update_display_image: Update the displayed image with the adjusted image.


    """

    def __init__(self, master, image_path):
        """Initialize the Hue and Saturation Adjustment window."""
        self.top = tk.Toplevel(master)
        self.top.title("Hue and Saturation Adjustment")

        self.image_path = image_path
        self.temp_path = os.path.join(os.getcwd(), "output_images", "temp_adjusted_image.jpg")
        self.display_image = None
        self.adjusted_image = None
        

        # Image display frame
        self.image_frame = tk.Frame(self.top)
        self.image_frame.pack(fill=tk.BOTH, expand=True)
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        # Controls frame
        self.controls_frame = tk.Frame(self.top)
        self.controls_frame.pack(fill=tk.X)

        # Saturation scale
        self.saturation_scale = tk.Scale(self.controls_frame, from_=-100, to=100, orient='horizontal', label='Saturation', command=self.adjust_image)
        self.saturation_scale.pack(side=tk.LEFT, padx=5)

        # Hue scale
        self.hue_scale = tk.Scale(self.controls_frame, from_=-180, to=180, orient='horizontal', label='Hue', command=self.adjust_image)
        self.hue_scale.pack(side=tk.LEFT, padx=5)

        # Exit button
        self.exit_button = tk.Button(self.controls_frame, text="Exit", command=self.close_editor)
        self.exit_button.pack(side=tk.RIGHT, padx=5)

        # Load the original image
        self.load_image()

    def close_editor(self):
        """
        Close the editor window.
        """
        self.top.destroy()
        self.top.quit()
        

    def load_image(self):
        """
        Load the original image and display it.
        """
        self.original_image = Image.open(self.image_path)
        self.display_image = ImageTk.PhotoImage(self.original_image.resize((550, 550), Image.Resampling.LANCZOS))
        self.image_label.configure(image=self.display_image)
        self.adjusted_image = self.original_image

    def adjust_image(self, val):
        """
        Adjust the image based on the saturation and hue values.
        Args:
        val: The value of the scale.
        """
        saturation_shift = self.saturation_scale.get()
        hue_shift = self.hue_scale.get()
        adjust_saturation_hue(self.image_path, saturation_shift, hue_shift, self.temp_path)
        self.update_display_image()

    def update_display_image(self):
        """Update the displayed image with the adjusted image."""
        self.adjusted_image = Image.open(self.temp_path)
        self.display_image = ImageTk.PhotoImage(self.adjusted_image.resize((550, 550), Image.Resampling.LANCZOS))
        self.image_label.configure(image=self.display_image)


def hsv_adjustment(root,image_path):
    """Open the Hue and Saturation Adjustment window."""
    app = HueSaturationEditor(root, image_path)
    root.mainloop()
