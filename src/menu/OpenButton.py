import tkinter as tk
from tkinter import filedialog


class OpenButton:
    @staticmethod
    def open_file(text_area, file_manager):
        filepath = filedialog.askopenfilename()
        if filepath != "":
            file_manager.set_opened_file_path(filepath)
            with open(filepath, "r") as file:
                text = file.read()
                text_area.text_field.delete("1.0", tk.END)
                text_area.text_field.insert("1.0", text)
