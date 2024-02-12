import os
import tkinter as tk
from tkinter import filedialog


# defining the replacement path
def replace_in_file(file_path, search_text, replace_text):
    with open(file_path, 'r') as file:
        data = file.read()

    modified_data = data.replace(search_text, replace_text)

    with open(file_path, 'w') as file:
        file.write(modified_data)


# using get method
def process_files():
    search_text = search_entry.get()

    replace_text = replace_entry.get()

    folder_path = folder_path_entry.get()

    output_folder = folder_path + "_replace"

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(folder_path):

        if filename.endswith(".txt"):  # Replace with the file extension of your choice

            file_path = os.path.join(folder_path, filename)

            output_file_path = os.path.join(output_folder, filename)

            replace_in_file(file_path, search_text, replace_text)

            os.rename(file_path, output_file_path)

    result_label.config(text="Files processed and renamed in folder: " + output_folder)


app = tk.Tk()

app.title("File Text Replacement")

app.geometry("300x300")

search_label = tk.Label(app, text="Search Text:")

search_label.pack()

search_entry = tk.Entry(app)

search_entry.pack()

replace_label = tk.Label(app, text="Replace Text:")

replace_label.pack()

replace_entry = tk.Entry(app)

replace_entry.pack()

folder_path_label = tk.Label(app, text="Select Folder:")

folder_path_label.pack()


def browse_folder():
    folder_path = filedialog.askdirectory()

    folder_path_entry.delete(0, tk.END)

    folder_path_entry.insert(0, folder_path)


folder_path_button = tk.Button(app, text="Browse", command=browse_folder)

folder_path_button.pack()

folder_path_entry = tk.Entry(app)

folder_path_entry.pack()

process_button = tk.Button(app, text="Process", command=process_files)

process_button.pack()

result_label = tk.Label(app, text="")

result_label.pack()

app.mainloop()