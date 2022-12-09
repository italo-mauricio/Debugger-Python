from math import log, pow, exp

'''
    Debugando pequenos programas no python

'''
def mostre_acerto(name_test):
    print(f"{name_test}:\t Passou ✅")
def mostra_erro(name_test):
    print(f"{name_test}:\t Não Passou ❌")

def multi_test(func):
    '''
       
        esta é uma função de teste para garantir que nosso
        soluções estão corretas. Sempre um bom hábito de se ter.
    
    '''
    if func(5, 6) == 5*6:
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)

def multi_recursi(num1, num2):

    '''
        isso funciona adicionando num1 juntos onde para cada
        chamada recursiva e, em seguida, garantindo o número de chamadas recursivas
        nós acordamos é igual a num 
    
    
    '''
    if num2 == 1:
        return num1 
    else:
        return num1 + multi_recursi(num1, num2 -1)

multi_test(multi_recursi)


def multi_loop(num1, num2):

    '''
        this one is fairly straightforeward. We simply add num1 to itself
        in a loop.   
    '''
    sum = 0
    for i in range(num2):
        sum += num1
    return sum

multi_test(multi_loop)


def multi_exp(num1, num2):

    '''
        This one takes advantage of the properties of exponents and logarithms 
    and is really just an algebra trick, Pretty cool, right?

    We know that e^(a*b) = (e^a) ^ b
    so if we apply the natural logarithm to both sides we get a*b = ln((e^a)}^b) 
    
    '''
    return log(pow(exp(num1), num2))

multi_test(multi_exp)


# exercicio 2, encontre o maior número em uma lista

def test_maior(func):
    if func ([8, 6, 7, 5, 309]) == 309:
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)

def maior_loop(numlist):
    '''
        This one is simples, just iterate over the list while keeping
    track of the largest element so far, then return the result you're done.
    
    '''
    maior = numlist[0]
    for num in numlist:
        if maior < num:
            maior = num
    return maior

test_maior(maior_loop)


def maior_simple(numlist):
    return max(numlist)

test_maior(maior_simple)


def maior_recursi(numlist):

    '''
        esta solução recursiva é um pouco complicada

        o caso base é quando há apenas 2 números na lista, então simplesmente retornamos o maior.

        para casos recursivos, retiramos o número mais à esquerda da lista e fazemos uma chamada recursiva com o resto da lista


        então comparamos o número mais à esquerda com o resultado da chamada recursiva e
        em seguida, retorne o maior.
    
    
    '''
    if len(numlist) == 2:
        if numlist[0] < numlist[1]:
            return numlist[1]
        else:
            return numlist[0]
    leftmost = numlist[0]
    largest_on_right = maior_recursi(numlist[1:])
    if largest_on_right > leftmost:
        return largest_on_right
    else:
        return leftmost 

    
test_maior(maior_recursi)