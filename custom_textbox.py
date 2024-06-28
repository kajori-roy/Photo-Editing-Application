# Description: A custom dialog box to resize an image.
import tkinter as tk
from tkinter import simpledialog

class CustomDialog(simpledialog.Dialog):
    """A custom dialog box to resize an image.
    
    Attributes:
    width_entry: The entry widget for the width.
    height_entry: The entry widget for the height.

    Methods:
    body: Create the dialog box.
    apply: Return the width and height entered by the user.

    """
    
    def body(self, master):

        """Create the dialog box.

        Args:
        master: The parent window.

        Returns:
        The entry widget for the width/height.
        """

        self.title("Resize Image")
        tk.Label(master, text="Width:").grid(row=0)
        tk.Label(master, text="Height:").grid(row=1)

        self.width_entry = tk.Entry(master)
        self.height_entry = tk.Entry(master)

        self.width_entry.grid(row=0, column=1)
        self.height_entry.grid(row=1, column=1)
        
        return self.width_entry  # Initial focus on the width entry

    def apply(self):
        """
        Return the width and height entered by the user.
        
        Returns:
        The width and height entered by the user.
        """
        self.result = (self.width_entry.get(), self.height_entry.get())

        

def resize(root):
    """Open a dialog box to resize the image.
    
    Args:
    root: The root window.
    
    Returns:
    The width and height entered by the user.

    """
    dialog = CustomDialog(root)
    if dialog.result:
        width, height = dialog.result
        return [width, height]
    root.mainloop()
