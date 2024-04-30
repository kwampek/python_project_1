import tkinter as tk

class EnumLinesBar:
    def __init__(self, root):
        self.numbers = tk.Text(root, width=1, pady=10, bg='#292929', fg='#595959', state=tk.DISABLED, relief=tk.FLAT)
        self.count_lines = 1
        self.numbers_width = self.numbers.winfo_width()
        self.insert_numbers("")
        self.numbers.grid(row=0, column=0, sticky='NS')

    def insert_numbers(self, text):
        count_of_lines = text.count('\n') + 1
        if (self.count_lines == count_of_lines):
            return

        self.count_lines = count_of_lines
        if (len(str(self.count_lines)) != self.numbers_width):
            self.numbers_width = len(str(self.count_lines))

        self.numbers.config(state=tk.NORMAL)  # make numbers_width respond to keyboard and mouse events
        self.numbers.config(width=len(str(self.count_lines)))
        print(self.count_lines, self.numbers_width)
        self.numbers.delete(1.0, tk.END)
        self.numbers.insert(1.0, '\n'.join(map(str, range(1, count_of_lines))))
        self.numbers.config(state=tk.DISABLED)
