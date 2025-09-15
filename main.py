def main():
    run = True
    while run == True:
        op = int(input("willst du addieren(1), subtrahieren(2), multiplizieren(3),dividieren(4) oder beenden(5)?"))

        if op == 5:
            run = False

        else:
            x = int(input("Enter a number 1: "))
            y = int(input("Enter a number 2: "))

        if op == 1:
            print(f"{x} + {y} = {add(x, y)}")

        elif op == 2:
            print(f"{x} - {y} = {sub(x, y)}")

        elif op == 3:
            print(f"{x} * {y} = {mul(x, y)}")

        elif op == 4:
            print(f"{x} / {y} = {div(x, y)}")









def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y


if __name__ == '__main__':
    main()
