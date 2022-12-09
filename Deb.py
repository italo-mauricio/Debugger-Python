from math import log, pow, exp

'''
    Today i'm going to be taking some common programming exercises and coming
    up with as many solutions as i can

    I've already polished and debugged the code here so don't feel bad if you don't
    write code like this. 


'''
def mostre_acerto(name_test):
    print(f"{name_test}:\t Passou ✅")
def mostra_erro(name_test):
    print(f"{name_test}:\t Não Passou ❌")

def multi_test(func):
    '''
        this is a test function to make sure our
        solutions are correct. Always a good habit to have.
    
    '''
    if func(5, 6) == 5*6:
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)

def multi_recursi(num1, num2):

    '''
        this works by adding num1 together onde for each
        recursive call, and then ensuring the number of recursive calls
        we wake is equal to num 2 
    
    
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

    