import tkinter as tk

from src.menu.EditButton import EditButton
from src.menu.FileMenu import FileMenu
from src.menu.FindButton import FindButton
from src.menu.HelpButton import HelpButton


class MenuBar:
    def __init__(self, root, text_area, file_manager):
        self.main_menu = tk.Menu(root)
        self.file_menu = FileMenu(text_area, file_manager)
        self.find_menu = FindButton(text_area)
        self.edit_menu = EditButton(self.find_menu, text_area)
        self.help_menu = HelpButton()
        self.add_cascades()
        root.config(menu=self.main_menu)

    def add_cascades(self):
        self.main_menu.add_cascade(label='File', menu=self.file_menu.file_menu)
        self.main_menu.add_cascade(label='Find', menu=self.find_menu.find_menu)
        self.main_menu.add_cascade(label='Edit', menu=self.edit_menu.edit_menu)
        self.main_menu.add_command(label='Help', command=self.help_menu.open)
