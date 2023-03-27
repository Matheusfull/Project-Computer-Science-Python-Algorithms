def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # raise NotImplementedError
    """ low_index = 0
    high_index = len(word) -1 """

    if len(word) == 0:
        return False

    if word[low_index] != word[high_index]:
        return False

    """ if low_index == high_index: assim não pode porque
    o teste da trybe coloca um índex high_index negativo
    e com isso a cada interação ele vai ficar cada vez mais negativo
    e jamais será igual ao low_index. Lá vai eu perder tempo
    até entender isso..."""
    if low_index >= high_index:
        return True

    low_index += 1
    high_index -= 1
    # print(next_index, previous_index)
    return is_palindrome_recursive(word, low_index, high_index)


# print(is_palindrome_recursive("anam", 0, 2)) # se eu colocar assim da true,
# temos um falso positivo
# print(len("ana") -1)
