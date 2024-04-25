import tkinter as tk
from OpenButton import OpenButton
from SaveButton import SaveButton


class FileMenu(OpenButton, SaveButton):
    def __init__(self, text_area, file_manager):
        self.file_menu = tk.Menu(tearoff=0)
        self.file_menu.add_command(label="Open", command=FileMenu.open_file_adapter(text_area, file_manager))
        self.file_menu.add_command(label="Save", command=SaveButton.general_save_adapter(text_area, file_manager))
        self.file_menu.add_command(label="SaveAs", command=self.save_as_file_adapter(text_area, file_manager))

    @staticmethod
    def open_file_adapter(text_area, file_manager):
        def open_adapt(event=False):
            return OpenButton.open_file(text_area, file_manager)

        return open_adapt

    def save_as_file_adapter(self, text_area, file_manager):
        def save_adapt(event=False):
            return self.save_as_file(text_area, file_manager)

        return save_adapt
