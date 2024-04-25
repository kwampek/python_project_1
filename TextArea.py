import tkinter as tk
from EnumLinesBar import EnumLinesBar


class TextArea:
    def __init__(self, file_manager):
        self.text_field = tk.Text(file_manager.root, yscrollcommand=self.on_yscrollcommand, insertbackground='white')

        self.scrollbar = tk.Scrollbar(file_manager.root, orient=tk.VERTICAL)

        self.enumLinesBar = EnumLinesBar(file_manager.root)
        self.config(file_manager)

    def config(self, file_manager):
        self.text_field.config(bg='#292929', fg='white', padx=10, pady=10, selectbackground='#C0C0C0')
        self.scrollbar.config(command=self.on_yscrollcommand, troughcolor='black')
        self.scrollbar.grid(row=0, column=2, sticky='NS')

        self.text_field.grid(row=0, column=1, sticky='NSWE')
        self.text_field.bind('<<Modified>>', self.bind_edit(file_manager))
        file_manager.root.grid_columnconfigure(1, weight=1)  # растяжение
        file_manager.root.grid_rowconfigure(0, weight=1)

    def on_yscrollcommand(self, *args):
        self.scrollbar.set(*args)
        self.enumLinesBar.numbers.yview_moveto(args[0])

    def bind_edit(self, file_manager):
        """ Вернуть функцию, обновляющую все внутренние переменные при изменении файла """

        def on_edit(event=None):
            self.enumLinesBar.insert_numbers(self.text_field.get(1.0, tk.END))
            self.text_field.edit_modified(False)
            file_manager.edit_file()

        return on_edit

    def scroll_command(self, *args):
        self.text_field.yview(*args)
        self.enumLinesBar.numbers.yview(*args)
