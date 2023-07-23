from time import sleep

def sumar1(a, b):
    print(a)
    print(b)
    a += 1
    b += 1
    
    if a != 100:
        sumar1(a, b)


def main():
    sumar1(1, 2)

if __name__== '__main__':
    main()
    