import tkinter as tk

from tkinter import filedialog


class SaveButton:
    @staticmethod
    def save_file(text_area, filepath):
        if filepath != "":
            text = text_area.text_field.get("1.0", tk.END)
            with open(filepath, "w") as file:
                file.write(text)

    @staticmethod
    def save_as_file(text_area, file_manager):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            SaveButton.save_file(text_area, filepath)
            file_manager.set_opened_file_path(filepath)

    @staticmethod
    def general_save(text_area, file_manager):
        if file_manager.opened_file_path != "":
            file_manager.save_file()
            SaveButton.save_file(text_area, file_manager.opened_file_path)
            return
        SaveButton.save_as_file(text_area, file_manager)

    @staticmethod
    def general_save_adapter(text_area, file_manager):
        def general(event=False):
            return SaveButton.general_save(text_area, file_manager)

        return general
