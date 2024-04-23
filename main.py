import tryangle as tr
import write_file as wr


def main():
    tryangle = tr.Tryangle(int(input('Enter a tryangle number: ')))
    tryangle.generate_tryangle()
    write = wr.Writer(input("Enter a file name: "), tryangle.result())
    write.write()

if __name__ == '__main__':
    main()
