import speedtest
import tkinter as tk
from tkinter import ttk
from threading import Thread

def test_internet_speed():
    """
    Function to test and display the internet download, upload speeds and ping.
    """
    # Start the progress bar
    progress_bar.start(10)

    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get best server based on ping
    st.get_best_server()

    # Perform the speed test
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping

    # Convert speeds from bps to Mbps
    download_speed_mbps = round(download_speed / (10**6), 2)
    upload_speed_mbps = round(upload_speed / (10**6), 2)

    # Stop the progress bar
    progress_bar.stop()

    # Update the labels in the UI
    download_label.config(text=f"Download Speed: {download_speed_mbps} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed_mbps} Mbps")
    ping_label.config(text=f"Ping: {ping} ms")

def start_test():
    """
    Function to start the speed test in a separate thread.
    """
    Thread(target=test_internet_speed).start()

def create_ui():
    """
    Function to create the Tkinter UI.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Internet Speed Test")

    # Set the bold font
    bold_font = ("Helvetica", 10, "bold")

    # Create a frame for layout
    frame = ttk.Frame(root, padding="30")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Add labels to the frame
    global download_label, upload_label, ping_label, progress_bar
    download_label = ttk.Label(frame, text="Download Speed: Testing...", font=bold_font)
    upload_label = ttk.Label(frame, text="Upload Speed: Testing...", font=bold_font)
    ping_label = ttk.Label(frame, text="Ping: Testing...", font=bold_font)

    download_label.grid(column=0, row=0, sticky=tk.W)
    upload_label.grid(column=0, row=1, sticky=tk.W)
    ping_label.grid(column=0, row=2, sticky=tk.W)

    # Add a progress bar
    progress_bar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
    progress_bar.grid(column=0, row=3, pady=(10, 0))

    # Add a button to start the test
    test_button = ttk.Button(frame, text="Test Speed", command=start_test)
    test_button.grid(column=0, row=4, pady=(10, 0))

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_ui()
