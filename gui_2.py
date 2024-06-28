# Main GUI code

from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import atexit
import os
import sys

# Modules
import hue_saturation_window
import rotate
import custom_textbox
from resize_image import resize_image
import sharpness_blur
from save_image import save_file
from delete_all_files import delete_images
from image_paths import make_output_path, make_saved_path , make_histogram_path
from dithering import dither
import grayscale
import histogram_stretching_color_mod as auto_level
from huffman_coding import huffman_main

# Resource path for icon 

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller
    
    Args:
        relative_path: Relative path of the resource
    
    Returns:
        Absolute path of the resource
    
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# GUI
root = Tk()
root.title("Kajori's Photo Editor")
icon_path =  "cute_cam.ico"
root.iconbitmap(resource_path(icon_path))
root.geometry("1200x600")  

# Frames
left_frame = Frame(root, width=200, bg='gray')
left_frame.grid(row=0, column=0, sticky='ns')

image_frame = Frame(root)
image_frame.grid(row=0, column=1, sticky='nsew')

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Global variables
original_image = None
edited_image = None
original_image_path = None
image_tag = None
output_file = None

def display_message(message):
    for widget in image_frame.winfo_children():
        widget.destroy()
    Label(image_frame, text=message, font= ("Arial", 30)).pack()



def open_image():
    """Open an image and display it in the image frame."""

    global original_image, original_image_path, edited_image
    original_image_path = None
    count = 0
    for widget in image_frame.winfo_children():
        widget.destroy()
        edited_image = None
        delete_images()
    file_path = filedialog.askopenfilename(title="Open Image", filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")))
    if file_path:
        img = Image.open(file_path)
        if img.mode != "RGB":
            count += 1
            display_message("Image is not in RGB mode")
        if img.width > 1024 or img.height > 768 or img.width < 1 or img.height < 1:
            count += 1
            display_message("Image size too large")
        if count == 0:
            original_image_path = file_path
            img.thumbnail((img.width, img.height)) 
            original_image = ImageTk.PhotoImage(img)
            display_images()

def save_image():
    """Save the edited image to a file."""
    make_saved_path()
    global edited_image, output_file, original_image_path, image_tag
    if original_image_path:
        if edited_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=(("BMP Files", "*.bmp"), ("All Files", "*.*")))
            if save_path:
                if output_file:
                    save_file(output_file, save_path)
        else:
            image_tag = "No edited image to save"
            display_images()
                    

    else:
        display_message("Open an image first")

def rotate_image():
    """Rotate the image by 90 degrees."""
    global edited_image, original_image_path, output_file
    if original_image_path:
        rotate.rotate(original_image_path)
        output_file = os.getcwd()+ "/output_images/"+ "rotated_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
    else:
        display_message("Open an image first")

def sharpen_image():
    """Sharpen the image."""
    global edited_image, original_image_path, output_file
    if original_image_path:
        sharpness_blur.sharpen_image(original_image_path)
        output_file = os.getcwd()+ "/output_images/"+ "sharpened_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
    else:
        display_message("Open an image first")


def blur_image():
    """Blur the image."""
    global edited_image, original_image_path, output_file
    if original_image_path:
        sharpness_blur.blur_image(original_image_path)
        output_file = os.getcwd()+ "/output_images/"+ "blurred_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
    else:
        display_message("Open an image first")

def hsv_adjustment():
    """Open the hue and saturation adjustment window."""
    global edited_image, original_image_path, output_file
    if original_image_path:
        hue_saturation_window.hsv_adjustment(root, original_image_path)
        output_file = os.getcwd()+ "/output_images/"+ "temp_adjusted_image.jpg"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
        
    else:
        display_message("Open an image first")

def get_formatted_cwd():
    # Get the current working directory
    cwd = os.getcwd()
    # Split the path into parts
    parts = cwd.split(os.sep)
    # Format the path for display
    formatted_cwd = "\\".join(["" * index + part for index, part in enumerate(parts)])
    return formatted_cwd

def resize_image_gui():
    """Open a dialog box to resize the image."""
    make_saved_path()
    global original_image_path , edited_image, image_tag , output_file
    if original_image_path:
        image_size = custom_textbox.resize(root)
        if image_size == None:
            return

        img_width = int(image_size[0])
        img_height = int(image_size[1])
        if img_width == 0 or img_height == 0:
            display_message("Invalid input")
            return
        if img_width > 10000 or img_height > 10000:
            display_message("Image size too large")
            return
        if img_width < 1 or img_height < 1:
            display_message("Invalid input")
            return
        resize_image(img_width, img_height, original_image_path)
        output_file =os.getcwd()+ "/output_images/"+ "resized_image.bmp"
        saved_image_path = os.getcwd()+ "/saved_images/"+ "resized_image.bmp"
        save_file(output_file, saved_image_path)
        edited_image = None
        saved_image_path = get_formatted_cwd() + "\n \\saved_images\\"+ "resized_image.bmp"
        image_tag = (f"Resized image to {img_width}x{img_height} and saved as resized_image.bmp in \n {saved_image_path}.")
        display_images()
    else:
        display_message("Open an image first")

def huffman_coding():
    """Perform Huffman encoding on the image."""
    global original_image_path , edited_image, image_tag , output_file
    if original_image_path:
        huffman = huffman_main(original_image_path)
        
        output_file =os.getcwd()+ "/output_images/"+ "huffman_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        image_tag = (f"Entropy of the image: {huffman[0]:.2f} bits \n Average Huffman code length: {huffman[1]:.2f} bits")
        display_images()

    else:
        display_message("Open an image first")


def auto_level_image():
    """Perform histogram stretching on the image."""
    global edited_image, original_image_path , output_file
    if original_image_path:
        
        auto_level.auto_level_color_image(original_image_path, "auto_level_image.bmp")
        output_file =os.getcwd()+ "/output_images/"+ "auto_level_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
    else:
        display_message("Open an image first")

def ordered_dithering():
    """Perform ordered dithering on the image."""
    global edited_image, original_image_path, output_file
    if original_image_path:
        
        dither(original_image_path, "dithered_image.bmp")
        output_file =os.getcwd()+ "/output_images/"+ "dithered_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
    else:
        display_message("Open an image first")

def exit_program():
    """Exit the program."""
    root.quit()
    root.destroy()
    root.quit()
    sys.exit()

def grayscale_image():
    """Convert the image to grayscale."""
    global edited_image, original_image_path, output_file
    if original_image_path:
        
        grayscale.grayscale(original_image_path, "grayscale_image.bmp")
        output_file = os.getcwd()+ "/output_images/"+ "grayscale_image.bmp"
        img = Image.open(output_file)
        img.thumbnail((550, 550))  
        edited_image = ImageTk.PhotoImage(img)
        display_images()
    else:
        display_message("Open an image first")

def display_images():
    """Display the original and edited images in the image frame."""
    global image_tag
    for widget in image_frame.winfo_children():
        widget.destroy()

    if image_tag:
        Label(image_frame, text=image_tag, font=("Arial", 20)).pack(pady=10)
        image_tag = None
    if original_image:
        Label(image_frame, image=original_image).pack(side="left", padx=(10, 5), pady=10)

    if edited_image:
        Label(image_frame, image=edited_image).pack(side="right", padx=(5, 10), pady=10)


# Create output directory

make_output_path()
make_histogram_path()

# Buttons
Button(left_frame, text="Open Image", command=open_image, width=20).pack(pady=10)
Button(left_frame, text="Grayscale", command=grayscale_image, width=20).pack(pady=10)
Button(left_frame, text="Auto Level", command=auto_level_image, width=20).pack(pady=10)
Button(left_frame, text="Dither", command=ordered_dithering, width=20).pack(pady=10)
Button(left_frame, text="Huffman Encoding", command=huffman_coding, width=20).pack(pady=10)
Button(left_frame, text="Save Image", command=save_image, width=20).pack(pady=10)
Button(left_frame, text="Sharpen Image", command=sharpen_image, width=20).pack(pady=10)
Button(left_frame, text="Blur Image", command=blur_image, width=20).pack(pady=10)
Button(left_frame, text="Resize Image", command=resize_image_gui, width=20).pack(pady=10)
Button(left_frame, text="Rotate Image", command=rotate_image, width=20).pack(pady=10)
Button(left_frame, text="Hue and Saturation", command=hsv_adjustment, width=20).pack(pady=10)
Button(left_frame, text="Exit", command=exit_program, width=20).pack(pady=10)

root.mainloop()

# Delete all images in the output_images directory on exit
atexit.register(delete_images)
