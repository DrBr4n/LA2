'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    words = texto.split()
    
    words.sort()

    words = sorted(words, key = lambda w : words.count(w) ,reverse = True)
 
    result = []

    for word in words:
        if word not in result:
            result.append(word)

    return result



