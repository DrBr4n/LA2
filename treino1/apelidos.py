'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):

    ordN = sorted(nomes, key = str.lower)

    names = []

    for name in ordN:
        names.append(name.split())
        
    namesOrdMatrix = sorted(names, key = lambda x : len(x) - 1)

    namesOrd = []
    for subname in namesOrdMatrix:
        namesOrd.append(" ".join(subname))

    return namesOrd
