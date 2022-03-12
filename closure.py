# Hola 3 -> HolaHolaHola
# Platzi 4 -> PlatziPlatziPlatziPlatzi


def make_repeater(n):
    def repeater(string):
        assert type(string) == str, 'Solo se aceptan cadenas'
        return n * string
    return repeater

def main():
    repeat_3 = make_repeater(3)
    print(repeat_3('Hola'))

    repeat_4 = make_repeater(4)
    print(repeat_4('Platzi'))


if __name__=='__main__':
    main()