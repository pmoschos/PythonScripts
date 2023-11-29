from tkinter import *
from tkinter import filedialog
import calendar
from PIL import ImageGrab

def display_calendar():
    """
    This function creates a new window to display the calendar for a selected year.
    It fetches the year from the year_entry widget, generates a calendar for that year,
    and displays it in a Label widget.
    """
    global calendar_window
    calendar_window = Toplevel(main_gui)
    calendar_window.title("Calendar For The Year")
    calendar_window.geometry("555x666")
    calendar_window.resizable(False, False)
    calendar_window.config(background="#DDF2FD")

    selected_year = int(year_entry.get())  # Get the year entered by the user

    header_label = Label(calendar_window, text='Calendar', bg='#164863',
                         fg='white', font=("Helvetica", 28, 'bold'))
    header_label.grid(row=1, column=1, columnspan=2, sticky='nsew')

    calendar_data = calendar.calendar(selected_year)  # Generate calendar data
    calendar_display = Label(calendar_window, text=calendar_data,
                             font="Consolas 10 bold", justify=LEFT, bg="#DDF2FD")
    calendar_display.grid(row=2, column=1, columnspan=2, sticky='nsew', padx=20)

def save_calendar_as_png():
    """
    This function saves the displayed calendar as a PNG file.
    It prompts the user to choose a file path and name, then captures the calendar window
    and saves it as an image. If no calendar is open, it prints an error message.
    """
    if 'calendar_window' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                                 filetypes=[("PNG files", "*.png")])
        if file_path:
            x = calendar_window.winfo_rootx()
            y = calendar_window.winfo_rooty()
            x1 = x + calendar_window.winfo_width()
            y1 = y + calendar_window.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            print(f"Saved calendar as '{file_path}'")
        else:
            print("Save operation cancelled.")
    else:
        print("No calendar to save. Please generate a calendar first.")

if __name__ == "__main__":
    # Main application setup
    main_gui = Tk()
    main_gui.config(background="#9BBEC8")
    main_gui.title("Calendar")
    main_gui.geometry("250x300")
    main_gui.resizable(False, False)

    # Centering the widgets in the main window
    main_gui.grid_columnconfigure(0, weight=1)
    main_gui.grid_columnconfigure(2, weight=1)

    # Setting up widgets in the main window
    app_label = Label(main_gui, text="Calendar", bg="#164863",
                      fg='white', font=("Helvetica", 28, 'bold', 'underline'))
    app_label.grid(row=1, column=1, pady=(10, 20), sticky='ew')

    year_label = Label(main_gui, text="Enter Year", bg="#427D9D", fg='white')
    year_entry = Entry(main_gui)
    year_label.grid(row=2, column=1, pady=(0, 10), sticky='ew')
    year_entry.grid(row=3, column=1, pady=(0, 20), sticky='ew')

    show_button = Button(main_gui, text="Show Calendar", fg="white",
                         bg="#164863", relief="groove", bd=2, cursor="hand2",
                         command=display_calendar)
    show_button.grid(row=4, column=1, pady=(0, 10), sticky='ew')

    save_button = Button(main_gui, text="Save as .png", bg="#164863", fg='white',
                         relief="groove", bd=2, cursor="hand2",
                         command=save_calendar_as_png)
    save_button.grid(row=5, column=1, pady=(0, 10), sticky='ew')

    close_button = Button(main_gui, text="CLOSE", bg="#164863", fg='white', 
                          relief="groove", bd=2, cursor="hand2", command=exit)
    close_button.grid(row=6, column=1, pady=(0, 20), sticky='ew')

    main_gui.mainloop()
