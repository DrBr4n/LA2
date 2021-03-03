'''
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
'''

def aloca(prefs):   
    renegados = []
    
    blacklist = []

    for key in sorted(prefs.keys()):
        semProj = True
        for value in prefs[key]:
            if value not in blacklist:
                blacklist.append(value)
                semProj = False
                break
        if semProj:
            renegados.append(key)

    return sorted(renegados)
