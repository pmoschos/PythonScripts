import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from PyDictionary import PyDictionary

class DictionaryApp:
    """
    A Tkinter-based application that serves as a simple dictionary.
    It allows users to search for meanings of words.
    """
    def __init__(self, root):
        """
        Initialize the application with the root window and set up the GUI.
        """
        self.root = root
        self.root.title("Dictionary")
        self.root.geometry("500x400")
        self.root.configure(bg="#FFF5C2")

        self.dictionary = PyDictionary()
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface components of the application.
        """
        # Heading Label
        heading_label = tk.Label(self.root, text="DICTIONARY", 
                                 font=("Helvetica", 35, "bold"), 
                                 foreground='Blue', bg="#FFF5C2")
        heading_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Frame for search box and search button
        frame = tk.Frame(self.root, bg="#FFF5C2")
        tk.Label(frame, text="Enter Word", font=("Helvetica", 15, "bold"), bg="#FFF5C2").pack(side=tk.LEFT)
        self.word_entry = ttk.Entry(frame, font=("Helvetica", 15))
        self.word_entry.pack(side=tk.LEFT, padx=10)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        search_button = tk.Button(self.root, text="Search Word", font=("Helvetica", 15, "bold"), 
                                  relief=tk.RIDGE, borderwidth=3, cursor="hand2", 
                                  foreground='Green', command=self.get_meaning)
        search_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Text Widget for Meaning Display with Scrollbar
        self.meaning_text = scrolledtext.ScrolledText(self.root, font=("Helvetica", 12), bg="#FFF5C2", wrap=tk.WORD)
        self.meaning_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configure grid layout for resizing
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.meaning_text.grid_columnconfigure(0, weight=1)

    def get_meaning(self):
        """
        Fetch and display the meaning of the word entered by the user.
        """
        word = self.word_entry.get()
        response = self.dictionary.meaning(word)
        self.meaning_text.delete('1.0', tk.END)  # Clear existing text

        if response:
            meaning = "\n".join(["{}: {}".format(pos, ", ".join(definitions)) for pos, definitions in response.items()])
        else:
            meaning = "Invalid word or error fetching meaning."

        self.meaning_text.insert(tk.END, meaning)

def main():
    """
    Main function to start the dictionary application.
    """
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
