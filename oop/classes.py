# создаем новый класс
class TextReader(object):
    def __init__(self, filename):
        self.filename = filename

    def read_text(self):
        with open(self.filename, 'r') as f:
            print(f.read())
