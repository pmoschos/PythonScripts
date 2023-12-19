import tkinter as tk
from tkinter import ttk
from playsound import playsound
from gtts import gTTS

def main_program(user_input):
    """
    Generate an MP3 file from the user input using gTTS and save it.
    """
    tts = gTTS(text=user_input, lang='en')
    tts.save('output.mp3')

def on_run_button_clicked(entry_widget):
    """
    Triggered when the Run button is clicked.
    It captures the user input from the provided entry widget,
    runs the main program to generate an MP3 file,
    and plays the generated audio.
    """
    user_input = entry_widget.get()
    main_program(user_input)
    playsound('output.mp3')

def main():
    """
    Main function to setup the GUI and start the application.
    """
    root = tk.Tk()
    root.geometry('350x150')  # Set window size
    root.resizable(False, False)  # Make window non-resizable
    root.title("Text-to-Speech Program")
    root.configure(bg='#FFF5C2')  # Set background color

    # Instruction Label
    instruction_label = tk.Label(root, text="Enter text to convert to speech:", 
                                 fg="#3081D0", bg="#FFF5C2", font="Helvetica 14 bold italic")
    instruction_label.pack(pady=(10, 0))

    # User Input Field
    user_input_entry = ttk.Entry(root, font="Helvetica 12")
    user_input_entry.pack(pady=(5, 20))

    # Run Button
    run_button = tk.Button(root, text="Generate and Play Speech", fg='#000000', 
                           bg='#F4F27E', command=lambda: on_run_button_clicked(user_input_entry))
    run_button.pack(side='bottom', anchor='center', pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    main()
