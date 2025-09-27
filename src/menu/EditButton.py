import tkinter as tk


class EditButton:
    def __init__(self, find_button, text_area):
        self.edit_menu = tk.Menu(tearoff=0)
        self.edit_menu.add_command(label="Replace", command=find_button.check_adapter(text_area, "Replace"))
