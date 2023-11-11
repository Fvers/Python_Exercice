DEFAULT_VALUE = -1


def input_is_invalid():
    return int(numb_to_guess) < 0


if __name__ == '__main__':
    numb_to_guess = input('Veuillez renseigner un nombre positif a deviner: ')
    user_try = DEFAULT_VALUE
    try_number = 0
    if input_is_invalid():
        raise Exception('Le nombre doit être un entier positif')
    while user_try != numb_to_guess:
        user_try = input('Devinez le nombre: ')
        try_number += 1
        if user_try > numb_to_guess:
            print('C\'est moins')
        elif user_try < numb_to_guess:
            print('C\'est plus')
    if user_try == numb_to_guess:
        print("C'est gagné en " + str(try_number) + " essais !")
