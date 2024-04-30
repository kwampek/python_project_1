import tkinter as tk


class FindButton:
    def __init__(self, text_area):
        self.find_menu = tk.Menu(tearoff=0)
        self.find_menu.add_command(label="Find", command=self.check_adapter(text_area))
        self.find_window = None

    def check_adapter(self, text_area, title="Find"):
        """ Вернуть функцию, создающую окно поиска и замены """

        def check(event=None):
            if not self.find_window:
                window = tk.Tk()
                window.title(title)
                window.resizable(False, False)
                self.find_window = window
                self.find_window.protocol("WM_DELETE_WINDOW", self.on_close_adapt(text_area))

            find_entry = tk.Entry(self.find_window)
            find_entry.grid(row=0, column=0, sticky='NSEW')
            find_button = tk.Button(self.find_window, text="Find", command=self.find_all(find_entry, text_area))
            find_button.grid(row=1,
                             column=0,
                             sticky='EW')

            replace_entry = tk.Entry(self.find_window)
            replace_entry.grid(row=0, column=1, sticky='NSEW')
            replace_button = tk.Button(self.find_window, text="Replace",
                                       command=self.replace_all(find_entry, replace_entry, text_area))
            replace_button.grid(row=1,
                                column=1,
                                sticky='EW')

        return check

    @staticmethod
    def find_all(entry, text_area):
        """ Вернуть функцию, отвечающую за поиск и выделение текста в поле entry """

        def find_all_dec():
            text_area.text_field.tag_remove('found', '1.0', tk.END)
            find_text = entry.get()
            if find_text:
                match_indices = []
                start_index = '1.0'
                while start_index:
                    start_index = text_area.text_field.search(find_text, start_index, tk.END, regexp=True)
                    if start_index:
                        end_index = f'{start_index}+{len(find_text)}c'
                        text_area.text_field.tag_add('found', start_index, end_index)
                        match_indices.append((start_index, end_index))
                        start_index = end_index

                text_area.text_field.tag_config('found', background='#3B6491')

                if match_indices:
                    text_area.text_field.see(match_indices[0][0])
                    text_area.text_field.mark_set(tk.ACTIVE, match_indices[0][0])

        return find_all_dec

    @staticmethod
    def replace_all(find_entry, replace_entry, text_area):
        """ Вернуть функцию, отвечающую за замену """

        def replace_all_dec(event=None):
            text_area.text_field.tag_remove('found', '1.0', tk.END)
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            new_text = text_area.text_field.get('1.0', tk.END).replace(find_text, replace_text)
            text_area.text_field.replace('1.0', tk.END, new_text)
            FindButton.find_all(replace_entry, text_area)()

        return replace_all_dec

    def on_close_adapt(self, text_area):
        def on_close():
            text_area.text_field.tag_remove('found', '1.0', tk.END)
            if self.find_window:
                self.find_window.destroy()
            self.find_window = None

        return on_close
