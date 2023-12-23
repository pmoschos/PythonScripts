import json
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from xml.etree.ElementTree import parse
from xmljson import badgerfish as bf

def convert_xml_to_json(xml_file, json_file, result_display):
    try:
        tree = parse(xml_file)
        json_content = bf.data(tree.getroot())
        pretty_json = json.dumps(json_content, indent=4)  # Pretty format JSON

        with open(json_file, 'w', encoding='utf-8') as outfile:
            outfile.write(pretty_json)

        result_display.configure(state='normal')  # Enable editing temporarily
        result_display.insert(tk.END, pretty_json + '\n\n')
        result_display.configure(state='disabled')  # Disable editing
    except Exception as e:
        result_display.configure(state='normal')
        result_display.insert(tk.END, f'Error: {e}\n\n')
        result_display.configure(state='disabled')

def select_file(file_label, selected_xml_file):
    file_path = filedialog.askopenfilename(filetypes=[('XML files', '*.xml')])
    if file_path:
        selected_xml_file[0] = file_path
        file_label.config(text=f'Selected file: {file_path.split("/")[-1]}')

def save_file(selected_xml_file, result_display):
    if selected_xml_file[0]:
        save_path = filedialog.asksaveasfilename(defaultextension='.json',
                                                 filetypes=[('JSON files', '*.json')])
        if save_path:
            convert_xml_to_json(selected_xml_file[0], save_path, result_display)
    else:
        messagebox.showwarning("Warning", "No XML file selected.")

def copy_to_clipboard(result_display):
    app.clipboard_clear()
    text = result_display.get('1.0', tk.END)
    app.clipboard_append(text)
    messagebox.showinfo("Info", "Content copied to clipboard.")

def main():
    global app
    app = tk.Tk()
    app.title('XML to JSON Converter')
    app.geometry('650x480')
    app.resizable(False, False)
    app.config(background='#FFF5C2')

    selected_xml_file = [None]

    frame = tk.Frame(app, bg='#FFF5C2')
    frame.pack(padx=10, pady=10)

    file_label = tk.Label(frame, text='No file selected.', bg='#FFF5C2')
    file_label.pack()

    select_button = tk.Button(frame, text='Select XML File',
                              command=lambda: select_file(file_label, selected_xml_file))
    select_button.pack()

    convert_button = tk.Button(frame, text='Convert',
                               command=lambda: save_file(selected_xml_file, result_display))
    convert_button.pack()

    result_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=20, bg='white', state='disabled')
    result_display.pack(padx=10, pady=10)

    copy_button = tk.Button(frame, text='Copy', command=lambda: copy_to_clipboard(result_display))
    copy_button.pack()

    app.mainloop()

if __name__ == '__main__':
    main()
