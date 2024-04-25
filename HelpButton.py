import tkinter as tk
import webbrowser

class HelpButton:
    def __init__(self):
        self.openMenu = tk.Menu()
        self.openMenu.add_cascade(label="Open", command=self.open)

    def open(event):
        webbrowser.open("https://github.com/kwampek/python_project_1/blob/main/README.md")

