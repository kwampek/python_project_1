class FileManager:
    def __init__(self, root):
        self.root = root
        self.opened_file_path = ''
        self.opened_file_name = 'Untitled'

    def set_opened_file_path(self, file_path):
        self.opened_file_path = file_path
        self.opened_file_name = self.opened_file_path.split('/')[-1]
        self.root.title(self.opened_file_name)

    def edit_file(self):
        self.root.title("*" + self.opened_file_name)

    def save_file(self):
        self.root.title(self.opened_file_name)
