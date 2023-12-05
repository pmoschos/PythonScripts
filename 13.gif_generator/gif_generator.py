import glob
import os
from tkinter import filedialog, Tk, Label, Button, StringVar

from PIL import Image

def convert_images_to_gif(image_folder, gif_filename, frame_duration, status_label):
    """
    Converts a series of images in a folder to a GIF.
    Updates the status label with the progress.

    Parameters:
    image_folder (str): Path to the folder containing images.
    gif_filename (str): Filename for the output GIF.
    frame_duration (int): Duration between frames in milliseconds.
    status_label (tkinter.Label): Label to display status messages.
    """
    image_files = glob.glob(os.path.join(image_folder, "*.png"))  # Change file extension if necessary

    frames = []
    for image_file in image_files:
        with Image.open(image_file) as img:
            frames.append(img.convert("RGBA"))

    if frames:
        frames[0].save(gif_filename, format="GIF", append_images=frames[1:], save_all=True, duration=frame_duration, loop=0)
        status_label.set("GIF created successfully in the selected folder!")
    else:
        status_label.set("No images found in the selected folder.")

def select_folder(folder_path, status_label):
    """
    Opens a dialog to select a folder and sets the folder path.

    Parameters:
    folder_path (tkinter.StringVar): Variable to store the folder path.
    status_label (tkinter.Label): Label to display status messages.
    """
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)
        status_label.set("Folder selected: " + folder_selected)
    else:
        status_label.set("Folder selection cancelled.")

def setup_gui():
    """
    Sets up the GUI for the application.
    """
    root = Tk()
    root.title("Image to GIF Converter")

    # Setting the window size to 150x200 pixels
    root.geometry("200x100")

    # Setting the window not resizable
    root.resizable(False, False)

    folder_path = StringVar()
    status_label = StringVar()
    status_label.set("Select a folder to start")

    Label(root, text="Select a folder with JPEG images").pack()
    Button(root, text="Select Folder", command=lambda: select_folder(folder_path, status_label)).pack()
    Label(root, textvariable=status_label).pack()

    Button(root, text="Convert to GIF", command=lambda: convert_images_to_gif(folder_path.get(), "generated_gif/output.gif", 200, status_label)).pack()

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
