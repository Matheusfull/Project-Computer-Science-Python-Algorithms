def is_palindrome_iterative(word):
    """Faça o código aqui"""
    # raise NotImplementedError
    if len(word) == 1:
        return True

    if word == '':
        return False

    mid = 0
    first_half = ''
    second_half = ''

    if len(word) % 2 == 0:
        mid = int((len(word)) / 2)
        first_half = word[:mid]
        second_half = word[mid:]
    else:
        mid = int((len(word) + 1) / 2)
        first_half = word[:mid-1]
        second_half = word[mid:]

    if list(first_half) == list(reversed(second_half)):
        return True
    else:
        return False


# print(is_palindrome_iterative("ESxSE"))
