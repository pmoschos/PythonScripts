# Background Remover GUI with Tkinter

![Total Views](https://views.whatilearened.today/views/github/pmoschos/pmoschos.svg)

## Script Overview 📘

The script includes functions to handle file selection, background removal, and user interaction through a graphical user interface (GUI) built with Tkinter. The background removal is performed using the `rembg` library.

### :computer: Script Code

```python
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
```

# Key Features 🌟
- **GUI Development**: Learn how to create a graphical user interface using Tkinter, a standard GUI library in Python.
- **File Handling**: Understand how to handle file selection and saving through Tkinter's filedialog.
- **Image Processing**: See how to use the rembg library to remove the background from an image.
- **User Interaction**: Learn how to handle user inputs and interactions in a GUI application.

# Installation and Setup 🚀
No installation is required beyond the necessary Python libraries, which can be installed using pip:

```bash
pip install rembg Pillow
```

## Console Output Example 📋
When you run the script, the GUI window will appear, allowing you to select an image file and specify an output filename. The background will be removed from the selected image, and the output will be saved with the specified filename.

## 📸 Screenshots
![image](https://github.com/pmoschos/PythonScripts/assets/133533759/b7a690b1-ea26-409e-9436-58d11e3a1ee1)

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>