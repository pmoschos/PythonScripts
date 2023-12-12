import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import rarfile
import os
import sys

def open_file_dialog():
    target = filedialog.askopenfilename(
        title="Select a zip or rar file",
        filetypes=[("Zip and RAR Files", "*.zip;*.rar")]
    )
    if target:
        try:
            if target.endswith('.zip'):
                with zipfile.ZipFile(target, 'r') as zip_ref:
                    extract_path = os.path.dirname(target)
                    zip_ref.extractall(extract_path)
                    messagebox.showinfo("Success", f"Zip files extracted to {extract_path}")
            elif target.endswith('.rar'):
                with rarfile.RarFile(target, 'r') as rar_ref:
                    extract_path = os.path.dirname(target)
                    rar_ref.extractall(extract_path)
                    messagebox.showinfo("Success", f"Rar files extracted to {extract_path}")
        except (zipfile.BadZipFile, rarfile.Error):
            messagebox.showerror("Error", "The provided file is not a valid zip or rar file.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def setup_gui():
    root = tk.Tk()
    root.title("Unzip and Unrar Program")

    window_width = 400
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    welcome_label = tk.Label(root, text="Welcome to the Unzip and Unrar Program", font=("Helvetica", 14))
    welcome_label.pack(pady=20)

    open_button = tk.Button(root, text="Select Zip or Rar File", command=open_file_dialog, font=("Helvetica", 12))
    open_button.pack()

    return root

def main():
    root = setup_gui()
    root.mainloop()

if __name__ == "__main__":
    main()
