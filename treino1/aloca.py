"""
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
"""

def aloca(prefs):

    #create a list of the students sorted by number
    studentsList = sorted(prefs.keys())
    #[10000,10885,40000]

    #create a list of the available projects
    tmp = list(prefs.values())
    tmp1 = []
    
    for i in range(0,len(studentsList)): 
        tmp1 += tmp[i]

    projectList = list(dict.fromkeys(tmp1))

    #associate the students to the projects
    listaDeRenegados = []
    for i in studentsList:
        k = True
        for j in prefs[i]:
            if projectList.count(j):
                prefs[i] = j
                projectList.remove(j)
                k = False
                break
        if k:
            prefs[i] = []
            listaDeRenegados.append(i)
            del prefs[i]

    print(prefs)

    return sorted(listaDeRenegados)

