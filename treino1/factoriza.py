'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''
def factoriza(n):

    nn = n

    factores = [4]

    while nn > 1:
        for num in range(2, n + 1):
            if nn % num == 0:
                factores.append(num)
                nn = nn / num
                break

    factores = set(factores)

    soma = 0

    #ver se algum os factores é primo
    primo = True
    for num in factores:
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
            else: primo = True
        if primo : soma += num
    return soma