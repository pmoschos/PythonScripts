import tkinter as tk
from tkinter import filedialog, messagebox, Label, Entry, Button, Frame
from pytube import YouTube

def fetch_and_download_video(video_link, destination_folder):
    """
    Fetches and downloads a YouTube video in MP4 format.

    Args:
    video_link (str): The URL of the YouTube video.
    destination_folder (str): The folder path where the video will be saved.

    Returns:
    None
    """
    try:
        video = YouTube(video_link)
        video_stream = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        video_stream.download(output_path=destination_folder)
        messagebox.showinfo("Download Complete", "The video has been downloaded successfully.")
    except Exception as error:
        messagebox.showerror("Download Failed", f"An error occurred: {error}")

def choose_directory():
    """
    Opens a dialog to select a directory and returns the chosen directory path.

    Returns:
    str: The path of the selected directory.
    """
    return filedialog.askdirectory()

def initiate_download():
    """
    Initiates the download process by fetching the URL and save directory.
    """
    video_link = url_input_field.get()
    destination_folder = choose_directory()
    if destination_folder:
        fetch_and_download_video(video_link, destination_folder)

def reset_input_field():
    """
    Clears the text from the URL input field.
    """
    url_input_field.delete(0, tk.END)

# Setting up the main application window
app_window = tk.Tk()
app_window.title("Easy YouTube Downloader")
app_window.resizable(False, False)  # Makes the window unresizable

# Adding and arranging widgets in the window
Label(app_window, text="YouTube Video URL:").pack(padx=10, pady=10)
url_input_field = Entry(app_window, width=60)
url_input_field.pack(padx=10, pady=5)

# Frame for centering the buttons
button_frame = Frame(app_window)
button_frame.pack(pady=20)

download_btn = Button(button_frame, text="Start Download", command=initiate_download)
download_btn.pack(side=tk.LEFT, padx=10)

reset_btn = Button(button_frame, text="Reset", command=reset_input_field)
reset_btn.pack(side=tk.RIGHT, padx=10)

# Running the application
app_window.mainloop()