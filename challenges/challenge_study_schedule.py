def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    number_student = 0
    for init, end in permanence_period:
        # print(init, end)
        if not isinstance(init, int) or not isinstance(end, int):
            return None

        if init <= target_time <= end:
            number_student += 1

    return number_student


""" permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_period, 2)) """

"""Faça o código aqui. Deus seja louvado sempre"""
# raise NotImplementedError
# 1 - pego o intervalo de tempo
# 2 - pego o primeiro horário do intervalo e passo por cada índice do array
# 3 - aquele índice que conter o horário, target_time, será contabilizado
# 4 - Coloco essa contalilidade num array
# 5 - retorno o maior contador - compreensão errada do readme
""" eu vou jogar um horário e ele vai passar por cada intervalo de
    tempo do permanence_period, se ele estiver contido, acrescenta um contado
    e por fim retorna esse contador"""
