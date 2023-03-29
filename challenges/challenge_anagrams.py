def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    # raise NotImplementedError
    # se as duas string forem iguais retorna True
    # caso contrário retorna False
    if not first_string and not second_string:
        return '', '', False

    string1 = list(first_string.lower())
    string2 = list(second_string.lower())

    order1 = sort_letters(string1)
    order2 = sort_letters(string2)

    if order1 == order2:
        return ''.join(order1), ''.join(order2), True
    else:
        return ''.join(order1), ''.join(order2), False


def sort_letters(letters):
    if len(letters) <= 1:
        return letters

    reference = letters[0]

    rigth = [el for el in letters[1:] if el < reference]
    left = [el for el in letters[1:] if el >= reference]

    return sort_letters(rigth) + [reference] + sort_letters(left)

# print(sort_letters('matheus'))
# print(is_anagram('matheus', 'matehsu'))
