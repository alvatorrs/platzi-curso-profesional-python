#Decorador que calcula el descuento de un producto por mayoreo

def descuento_producto(porcentaje: float):
    def descuento(func):
        def wrapper(*args, **kwargs):
            total_cost = func(*args, **kwargs) - func(*args, **kwargs)*(porcentaje/100)
            print(f'El costo total con el 10% de descuento es de: {total_cost} pesos')
        return wrapper
    return descuento


@descuento_producto(10)
def costo(precio: float, cantidad: int):
    return cantidad * precio


def main():
    print('Bienvenido, favor de colocar los siguientes datos')
    print('Recuerde que el descuento solo aplica para más de 4 productos')
    try:
        precio = float(input('Coloque el precio unitario del producto: '))
        cantidad = int(input('Coloque la cantidad del producto: '))
        if cantidad >= 5:
            costo(precio, cantidad)
        else:
            print(f'El costo total es de {precio * cantidad} pesos')
    except ValueError:
        print('Favor de colocar una cantidad numérica')


if __name__=='__main__':
    main()