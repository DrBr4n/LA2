'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):

    result = []

    for book in livros:
        nums = []
        for num in livros[book]:
            nums.append(int(num))
        print(nums)

        summ = 0
        indx = 0
        for num in nums:
            if (indx % 2 == 0): summ += num
            else: summ += num*3
            indx += 1 
    
        if(summ % 10 != 0): 
            result.append(book)

    return sorted(result)