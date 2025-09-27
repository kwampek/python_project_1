import tkinter as tk

from src.interface.FileManager import FileManager
from src.interface.TextArea import TextArea
from src.menu.MenuBar import MenuBar
from src.menu.SaveButton import SaveButton


class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.set_icon()

        self.fileManager = FileManager(self.root)
        self.textArea = TextArea(self.fileManager)
        self.menu_bar = MenuBar(self.root, self.textArea, self.fileManager)
        self.add_hot_keys()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # конфигурация деструктора окна

    def run(self):
        self.root.title("myNotepad")
        self.root.mainloop()

    def add_hot_keys(self):
        self.root.bind('<Control-f>', self.menu_bar.find_menu.check_adapter(self.textArea))
        self.root.bind('<Control-s>', SaveButton.general_save_adapter(self.textArea, self.fileManager))

    def set_icon(self):
        photo = tk.PhotoImage(file='assets/icon.png')
        self.root.iconphoto(False, photo)

    def on_close(self):
        SaveButton.general_save_adapter(self.textArea, self.fileManager)
        if self.menu_bar.find_menu.find_window:
            self.menu_bar.find_menu.find_window.destroy()
        self.root.destroy()
