class Tryangle:
    def __init__(self, size):
        self.tryangle = []
        self.string = ""
        self.size = size

    def generate_tryangle(self):
        for i in range(self.size):
            self.tryangle.append(i)
        return self.tryangle

    def result(self):
        for i in self.tryangle:
            for j in self.tryangle[:i+1]:
                self.string += str(j) + "\t"
            self.string += "\n"
        return self.string

test = Tryangle(int(input("Enter size of tryangle: ")))
test.generate_tryangle()
print(test.result())
