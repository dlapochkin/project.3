import random
import string


def main():
    """
    Main function
    :return: None
    """
    alphabet = [x for x in string.ascii_lowercase]
    rt1 = rotor1(alphabet)
    rt2 = rotor2(alphabet)
    rt3 = rotor3(alphabet)
    refl = [x for x in 'yruhqsldpxngokmiebfzcwvjat']
    magic(alphabet, rt1, rt2, rt3, refl)


def module(number):
    """
    Modulo addition 26
    :param number: entered number
    :return: modulo 26 number
    """
    if number >= 26:
        return number - 26
    else:
        return number


def rotor1(alphabet):
    """
    Randomly creates alphabet for the first rotor
    :param alphabet: latin alphabet
    :return: rotor's alphabet
    """
    rotor = alphabet.copy()
    random.shuffle(rotor)
    return rotor


def rotor2(alphabet):
    """
    Randomly creates alphabet for the second rotor
    :param alphabet: latin alphabet
    :return: rotor's alphabet
    """
    rotor = alphabet.copy()
    random.shuffle(rotor)
    return rotor


def rotor3(alphabet):
    """
    Randomly creates alphabet for the third rotor
    :param alphabet: latin alphabet
    :return: rotor's alphabet
    """
    rotor = alphabet.copy()
    random.shuffle(rotor)
    return rotor


def keys(raw, alphabet):
    """
    Makes encryption keys list
    :param raw: raw input
    :param alphabet: latin alphabet
    :return: encryption keys
    """
    raw = raw.lower()
    key = raw.split()
    for item in key:
        if item not in alphabet:
            return False
    return key


def enigma(alphabet, rt1, rt2, rt3, refl, keys, answer):
    """
    Enigma algorithm
    :param alphabet: latin alphabet
    :param rt1: first rotor's alphabet
    :param rt2: second rotor's alphabet
    :param rt3: third rotor's alphabet
    :param refl: reflector's alphabet
    :param keys: encryption keys
    :param answer: encoded message
    :return: encrypted message
    """
    message = []
    key1 = alphabet.index(keys[-1])
    key2 = alphabet.index(keys[-2])
    key3 = alphabet.index(keys[-3])
    for ltr in answer.lower():
        if not (ltr in string.punctuation or ltr == ' ' or ltr in string.digits):
            meta1 = rt1[module(alphabet.index(ltr) + key1)]
            meta2 = rt2[module(alphabet.index(meta1) + key2 - key1)]
            meta3 = rt3[module(alphabet.index(meta2) + key3 - key2)]
            meta4 = refl[module(alphabet.index(meta3) - key3)]
            meta5 = alphabet[rt3.index(rt3[module(alphabet.index(meta4) + key3)])]
            rev = alphabet[rt3.index(meta5)]
            meta6 = alphabet[rt2.index(rt2[module(alphabet.index(rev) + key2 - key3)])]
            rev = alphabet[rt2.index(meta6)]
            meta7 = alphabet[rt1.index(rt1[module(alphabet.index(rev) + key1 - key2)])]
            rev = alphabet[rt1.index(meta7)]
            out = alphabet[alphabet.index(rev) - key1]
            message.append(out)
    return 'Зашифрованное/расшифрованное сообщение: ' + ''.join(message)


def magic(alphabet, rt1, rt2, rt3, refl):
    """
    Interactive function
    :param alphabet: latin alphabet
    :param rt1: first rotor's alphabet
    :param rt2: second rotor's alphabet
    :param rt3: third rotor's alphabet
    :param refl: reflector's alphabet
    :return: None
    """
    while True:
        answer = input('''Введите одну из перечисленных ниже команд:
alphabet: вывести заданный алфавит (по умолчанию генерируется автоматически)
change: переопределить алфавит
start: зашифровать/расшифровать сообщение с использованием заданного алфавита
/end: завершение программы (на любом шаге)
/back: вернуться к предыдущему шагу (на любом шаге)

''')
        if answer == '/end' or answer == '/back':
            quit()
        elif answer == 'alphabet':
            print('Алфавит первого ротора:', ''.join(rt1))
            print('Алфавит второго ротора:', ''.join(rt2))
            print('Алфавит третьего ротора:', ''.join(rt3))
            print('Алфавит рефлектора:', ''.join(refl), '\n')
            continue
        elif answer == 'change':
            print('Алфавит должен содержать 26 букв латинского алфавита. Буквы не могут повторяться.')
            rt1 = list(input('Введите алфавит первого ротора: '))
            rt2 = list(input('Введите алфавит второго ротора: '))
            rt3 = list(input('Введите алфавит третьего ротора: '))
            print('')
            continue
        elif answer == 'start':
            while True:
                answer = input('Введите ключи шифрования (три латинские буквы через пробел): ')
                if answer == '/back':
                    break
                elif answer == '/end':
                    quit()
                elif len(answer) == 5 and keys(answer, alphabet):
                    key = keys(answer, alphabet)
                    while True:
                        text = 'Введите сообщение для последующего шифрования/расшифрования ' + \
                               '(ключи заданы как ' + ', '.join([x.upper() for x in key]) + '): '
                        answer = input(text).lower()
                        if answer == '/back':
                            break
                        elif answer == '/end':
                            quit()
                        else:
                            print(enigma(alphabet, rt1, rt2, rt3, refl, key, answer))
                else:
                    print('Ошибка ввода, повторите попытку.')
                    continue
        else:
            print('Ошибка ввода, повторите попытку.')
            continue


main()