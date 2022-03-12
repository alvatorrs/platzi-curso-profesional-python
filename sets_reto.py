#Reto con sets [1,1,2,2,4] -> [1,2,4]

def remove_duplicates(some_list):
    without_duplicates = list(set(some_list))
    return without_duplicates


def main():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))


if __name__=='__main__':
    main()