def palindrome(letter: str) -> bool:
    letter = letter.replace(' ','').lower()
    return letter == letter[::-1]


def main():
    letter: str = input('Escriba una palabra: ')
    print(palindrome(letter))


if __name__ == '__main__':
    main()
