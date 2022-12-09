def mostre_acerto(name_test):
    print(f"{name_test}:\t Passou ✅")
def mostra_erro(name_test):
    print(f"{name_test}:\t Não Passou ❌")

def multi_test(func):
    # testa a função
    if func(5, 8) == 5*6:
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)

def multi_recursi(num1, num2):
    if num2 == 2:
        return num1
    else:
        return num1 + multi_recursi(num1, num2 -1)

multi_test(multi_recursi)