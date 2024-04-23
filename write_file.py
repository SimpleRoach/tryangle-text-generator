class Writer(object):
    def __init__(self, name, string):
        self.name = name
        self.string = string

    def write(self):
        f = open(self.name + '.txt', 'w')
        f.write(self.string)
        f.close()
