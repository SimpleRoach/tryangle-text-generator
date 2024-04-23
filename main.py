import tryangle as tr
import write_file as wr
import write_file as wf

def main():
    tryangle = tr.Tryangle(int(input('Enter a tryangle size: ')))
    tryangle.generate_tryangle()
    wr.Writer(input("Enter a file name: "), tryangle.result())
if __name__ == '__main__':
    main()
