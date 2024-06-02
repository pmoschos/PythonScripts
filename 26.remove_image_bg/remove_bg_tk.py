from tkinter import Tk, Label, Entry, Button, filedialog
from rembg import remove # pip install rembg
from PIL import Image

def remove_background(input_path: str, output_path: str):
    try:
        # Open the input image file
        with open(input_path, 'rb') as f:
            input_image = f.read()

        # Remove the background
        output_image = remove(input_image)

        # Save the output image
        with open(output_path, 'wb') as f:
            f.write(output_image)
        
        print("Background removed and image saved successfully.")
    except IOError:
        print("Error occurred while opening or saving the image.")

def on_submit():
    try:
        output_filename = output_entry.get()
        if not output_filename:
            print("Please enter a valid output filename.")
            return

        output_path = f"{output_filename}.png"
        remove_background(filepath, output_path)
    except ValueError:
        print("An error occurred during the background removal process.")

def on_file_select():
    global filepath
    filepath = filedialog.askopenfilename()
    file_label.config(text=f"Selected File: {filepath}")

# GUI setup
root = Tk()
root.title("Background Remover")

file_label = Label(root, text="No file selected")
file_label.pack()

select_button = Button(root, text="Select Image", command=on_file_select)
select_button.pack()

output_label = Label(root, text="Enter Output Filename (without extension):")
output_label.pack()

output_entry = Entry(root)
output_entry.pack()

submit_button = Button(root, text="Remove Background", command=on_submit)
submit_button.pack()

root.mainloop()
