from math import log, pow, exp


def mostre_acerto(name_test):
    print(f"{name_test}:\t Passou ✅")
def mostra_erro(name_test):
    print(f"{name_test}:\t Não Passou ❌")

def multi_test(func):
    # testa a função
    if func(5, 6) == 5*6:
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)

def multi_recursi(num1, num2):
    if num2 == 1:
        return num1 
    else:
        return num1 + multi_recursi(num1, num2 -1)

multi_test(multi_recursi)


def multi_loop(num1, num2):
    sum = 0
    for i in range(num2):
        sum += num1
    return sum

multi_test(multi_loop)


def multi_exp(num1, num2):
    return log(pow(exp(num1), num2))

multi_test(multi_exp)