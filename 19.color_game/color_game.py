import tkinter
import random
from tkinter import font

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)  # Disable resizing.

        self.colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
                       'Yellow', 'Orange', 'White', 'Purple', 'Brown']
        self.score = 0
        self.highest_score = 0
        self.time_left = 30

        self.instructions_font = font.Font(family='Helvetica', size=12, weight='bold')

        self.create_widgets()

    def create_widgets(self):
        self.instructions_label = tkinter.Label(self.root, text="Type in the color of the words, not the word text!\n",
                                                font=self.instructions_font)
        self.instructions_label.pack()

        self.score_label = tkinter.Label(self.root, text="Press Enter to start!\n", font=('Helvetica', 12))
        self.score_label.pack()

        self.current_score_label = tkinter.Label(self.root, text=f"Current Score: {self.score}", font=('Helvetica', 12))
        self.current_score_label.pack()

        self.highest_score_label = tkinter.Label(self.root, text=f"Highest Score: {self.highest_score}",
                                                 font=('Helvetica', 12))
        self.highest_score_label.pack()

        self.time_label = tkinter.Label(self.root, text=f"Time left: {self.time_left}", font=('Helvetica', 12))
        self.time_label.pack()

        self.color_label = tkinter.Label(self.root, font=('Helvetica', 60))
        self.color_label.pack()

        self.user_input = tkinter.Entry(self.root)
        self.user_input.bind('<Return>', self.start_game)
        self.user_input.pack()
        self.user_input.focus_set()

        self.feedback_label = tkinter.Label(self.root, text="", font=('Helvetica', 12))
        self.feedback_label.pack()

        self.restart_button = tkinter.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.possible_answers_label = tkinter.Label(self.root, text=f"\nPossible Answers\n{', '.join(self.colors)}",
                                                    font=('Helvetica', 12))
        self.possible_answers_label.pack()

        self.timer = None  # Timer variable

    def start_game(self, event=None):
        if self.time_left == 30:
            self.countdown()
            self.next_color()
        self.user_input.bind('<Return>', self.check_answer)

    def check_answer(self, event=None):
        user_answer = self.user_input.get().lower()
        #correct_answer = self.color_label.cget("text").lower()
        correct_answer = self.color_label.cget("fg").lower()
        if user_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Wrong!", fg="red")
        self.current_score_label.config(text=f"Current Score: {self.score}")
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.highest_score_label.config(text=f"Highest Score: {self.highest_score}")

        if self.time_left > 0:
            self.next_color()

    def next_color(self):
        self.user_input.focus_set()
        random.shuffle(self.colors)
        color_to_type = self.colors[0]
        text_color = self.colors[1]

        self.color_label.config(fg=text_color, text=color_to_type)
        self.user_input.delete(0, tkinter.END)

        self.possible_answers_label.config(text=f"\nPossible Answers\n{', '.join(self.colors)}")

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left}")
            self.timer = self.time_label.after(1000, self.countdown)
        else:
            self.feedback_label.config(text="Game Over!", fg="red")

    def restart_game(self):
        self.score = 0
        self.time_left = 30
        self.score_label.config(text="Press Enter to start!\n")
        self.current_score_label.config(text=f"Current Score: {self.score}")
        self.time_label.config(text=f"Time left: {self.time_left}")
        self.feedback_label.config(text="")
        self.possible_answers_label.config(text=f"Possible Answers\n{', '.join(self.colors)}")
        if self.timer:
            self.time_label.after_cancel(self.timer)  # Cancel the timer
        self.start_game()

def main():
    root = tkinter.Tk()
    game = ColorGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
