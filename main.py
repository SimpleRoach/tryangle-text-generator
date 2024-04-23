import tryangle as tr

def main():
    tryangle = tr.Tryangle(int(input('Enter a tryangle number: ')))
    tryangle.generate_tryangle()
    print(tryangle.result())

if __name__ == '__main__':
    main()
