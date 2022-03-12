import time

def fibo_gen(nmax):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif counter < nmax:
            counter += 1
            aux = n1 + n2
            n1, n2 = n2, aux
            yield aux
        else:
            break


if __name__ == '__main__':
    print('Esta es la sucesión de Fibonacci')
    num = int(input('Digite el número de elementos: '))
    print('Los elementos son: ')
    fibo = fibo_gen(num)
    for element in fibo:
        print(element)
        time.sleep(1)