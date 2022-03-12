'''Programa que mide el tiempo de ejecución de una función'''
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1,1000000):    #cuando no deseamos conocer el valor del iretados colocamos un _
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre = 'Alvaro'):
    print(f'Hola {nombre}')


def main():
    random_func()
    suma(2,7)
    saludo()


if __name__=='__main__':
    main()