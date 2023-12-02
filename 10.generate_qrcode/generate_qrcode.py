import tkinter as tk
from PIL import Image, ImageTk
import pyqrcode
import png

# Your QR code generation
link = "https://github.com/pmoschos"
qr_code = pyqrcode.create(link)
qr_code.png("pmoschos.png", scale=5)

# Tkinter setup
root = tk.Tk()
root.title("QR Code Display")

# Load the QR code image
image = Image.open("pmoschos.png")
photo = ImageTk.PhotoImage(image)

# Displaying the image in a label widget
label = tk.Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

# Run the application
root.mainloop()
