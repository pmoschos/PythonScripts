import tkinter as tk
from PIL import Image, ImageTk
import random

class DiceRollerApp:
    """
    A simple dice rolling simulator app using Tkinter.
    This app displays a window where users can roll two dice.
    """

    def __init__(self, root):
        """
        Initialize the DiceRollerApp class.

        Args:
        root: A Tk root window.
        """
        self.root = root
        self.initialize_ui()

    def initialize_ui(self):
        """
        Set up the user interface for the dice roller app.
        This includes the window configuration, dice images, and buttons.
        """
        # Set window size and make it non-resizable
        self.root.geometry('550x350')
        self.root.resizable(False, False)
        self.root.title('Roll the Dice')
        self.root.configure(bg='#FFF5C2')

        # Title label
        self.label_title = tk.Label(self.root, text="Dice Roller", fg="#3081D0",
                                    bg="#FFF5C2", font="Helvetica 16 bold italic")
        self.label_title.pack()

        # Load dice images and create labels for them
        self.dice_images = self.load_dice_images()
        self.dice_image_label1 = tk.Label(self.root, image=None, bg='#FFF5C2')
        self.dice_image_label1.pack(side=tk.LEFT, expand=True)

        self.dice_image_label2 = tk.Label(self.root, image=None, bg='#FFF5C2')
        self.dice_image_label2.pack(side=tk.RIGHT, expand=True)

        # Roll button
        self.roll_button = tk.Button(self.root, text='Roll the Dice', fg='#000000', bg='#F4F27E', command=self.rolling_dice)
        self.roll_button.pack(side='bottom', anchor='center', pady=(0, 10))

    def load_dice_images(self):
        """
        Load dice images from the specified file paths.

        Returns:
        List[PhotoImage]: A list of Tkinter PhotoImage objects representing the dice.
        """
        dice_image_paths = ['./images/die1.png', './images/die2.png', 
                            './images/die3.png', './images/die4.png', 
                            './images/die5.png', './images/die6.png']
        return [ImageTk.PhotoImage(Image.open(image_path)) for image_path in dice_image_paths]

    def rolling_dice(self):
        """
        Randomly select and display images for two dice.
        This method is bound to the roll button.
        """
        selected_image1 = random.choice(self.dice_images)
        selected_image2 = random.choice(self.dice_images)
        
        self.dice_image_label1.configure(image=selected_image1)
        self.dice_image_label1.image = selected_image1

        self.dice_image_label2.configure(image=selected_image2)
        self.dice_image_label2.image = selected_image2

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
