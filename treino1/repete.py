'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):

    result = palavra
    to_Add = palavra

    e = len(palavra) - 1
    i = 1
    while e != 0:
        while i < len(palavra):
            if(result[e:] + result[i:] == palavra):
                to_Add = result[i:]
            i += 1
        e -= 1
        i = 1

    j = 1
    while j != n:
        result += to_Add
        j += 1

    return result