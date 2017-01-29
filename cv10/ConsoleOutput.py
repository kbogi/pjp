from Output import Output

class ConsoleOutput(Output):
    def write(self, line):
        print(line)
