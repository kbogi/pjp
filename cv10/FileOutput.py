from Output import Output


class FileOutput(Output):
    def __init__(self, soubor):
        self.file = open(soubor, 'w', encoding='utf-8')

    def write(self, line):
        self.file.write(line + '\n')
