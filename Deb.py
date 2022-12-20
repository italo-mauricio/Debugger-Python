from math import log, pow, exp, ceil
from functools import reduce

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


def maior_funcional(numlist):
    '''
        this is a neat trick

    reduce() is a technique from functional programming where a function that takes
    two arguments is applied to the first two items in a list, then apllied again 
    to the result of the first call and the next item in the list, and so on and so forth

    In the words:
    mylist = [1,2,3,4,5,6]
    result = mylist[0]
    result = f(result, mylist[1])
    result = f(result, mylist[2])

    result = f(result, mylist[n])
    
    '''
    return reduce(lambda x, y: x if x > y else y, numlist)

test_maior(maior_funcional)


'''
    exercise 3: check if a string a palindrome permutation
    ex: "tacocat", "acocatt", and "cattaco" would all be true

'''

def palindro_test(func):
    if (func('tacocat')
        and func('acocatt')
        and not func('tacodog')):
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)

def palindro_loop(letters):
    '''
        Since a palindrome permutation is basically just a rotated
        palindrome, we can simply check if any rotation is a palindrome

        if any rotation of the string is a palindrome, then the string must be
        a palindrome permutation
    
    
    
    
    
    '''
    def rotate(s):
        return s[1:] + s[0]

    def palindro(s):
        while len(s) > 1:
            if s[0] != s[-1]:
                return False
            else:
                s = s[1:-1]
        return True
    
    temp_str = str(letters)
    for _ in letters:
        if palindro(temp_str):
            return True
        temp_str = rotate(temp_str)

    return False


palindro_test(palindro_loop)



def palindro_stack(letters):
    '''
        if string, such as 'acoatt', is a palindrome permutation then it's double,
        'acocattacoacatt', will contain the original unrotated palindrome.

        So we can iterate over 'accocattacocatt' while keeping track of the few letters
        in a stack. If we find that the next few letters are the same as what we have in
        the stack, then 'acocatt' is a palindrome.
    
    '''
    stack_size = ceil(len(letters)/2)
    stack = ''
    repeat = letters + letters
    for idx, l in enumerate(letters + letters):
        stack = l + stack
        stack = stack[-stack_size:]
        if stack == repeat[idx: (idx + stack_size)]:
            return True
        return False

palindro_test(palindro_stack)


# exercicse 4: Determine if all the characteres in a string are unique


def test_unique(func):
    if func('asdf') and not func('asdfa'):
        mostre_acerto(func.__name__)
    else:
        mostra_erro(func.__name__)


def unique_char(chars):
    return len(chars) == len(set(chars))

test_unique(unique_char)

def is_unique_sort(chars):
    prev = ''
    for char in sorted(list(chars)):
        if char == prev:
            return False
        prev = char
    return True

test_unique(is_unique_sort)

def is_unique_count(chars):
    for char in chars:
        if chars.count(char) > 1:
            return False
    return True

test_unique(is_unique_count)

def is_unique_alpha(chars):
    alpha = list(set('thequickbrownfoxjumpsoverthelazydog'))
    alpha_size = len(alpha)
    alpha = [c for c in alpha if c not in chars]
    result = (alpha_size - len(chars)) == len(alpha)
    return result

test_unique (is_unique_alpha)
