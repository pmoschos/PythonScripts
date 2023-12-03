from PIL import Image
from tkinter import filedialog
from tkinter import Tk, Label, Entry, Button

def resize_image(image_path, new_width, new_height):
    try:
        image = Image.open(image_path)
        print(f"Current size: {image.size}")

        resized_image = image.resize((new_width, new_height))
        resized_image.save(f'resized_image_{new_width}_{new_height}.jpeg')
        print("Image resized and saved successfully.")
    except IOError:
        print("Error occurred while opening or saving the image.")

def on_submit():
    try:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        resize_image(filepath, new_width, new_height)
    except ValueError:
        print("Please enter valid width and height values.")

def on_file_select():
    global filepath
    filepath = filedialog.askopenfilename()
    file_label.config(text=f"Selected File: {filepath}")

# GUI setup
root = Tk()
root.title("Image Resizer")

file_label = Label(root, text="No file selected")
file_label.pack()

select_button = Button(root, text="Select Image", command=on_file_select)
select_button.pack()

width_label = Label(root, text="Enter Width:")
width_label.pack()

width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text="Enter Height:")
height_label.pack()

height_entry = Entry(root)
height_entry.pack()

submit_button = Button(root, text="Resize Image", command=on_submit)
submit_button.pack()

root.mainloop()
