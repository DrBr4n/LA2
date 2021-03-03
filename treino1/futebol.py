'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):

    #populate dict_Stats -> team:[respective goals, dif between scored and suffered, points]
    dict_Stats = {}

    for game in jogos:
        dict_Stats[game[0]] = [0,0,0]
        dict_Stats[game[2]] = [0,0,0]
    
    for game in jogos:
        dict_Stats[game[0]] = [dict_Stats[game[0]][0] + game[1], dict_Stats[game[0]][1] + game[1] - game[3], dict_Stats[game[0]][2] + 0]
        dict_Stats[game[2]] = [dict_Stats[game[2]][0] + game[3], dict_Stats[game[2]][1] + game[3] - game[1], dict_Stats[game[2]][2] + 0]
        if game[1] > game[3] : dict_Stats[game[0]][2] += 3
        elif game[1] < game[3] : dict_Stats[game[2]][2] += 3
        else:
            dict_Stats[game[0]][2] += 1
            dict_Stats[game[2]][2] += 1 

    teams_Stats = list(dict_Stats.items())

    #sort alphabetically
    sorted_Stats = sorted(teams_Stats, key = lambda x : x[0])
    #sort by goals diff
    sorted_Stats.sort(key = lambda x : x[1][1], reverse = True)
    #sort on points
    sorted_Stats.sort(key = lambda x : x[1][2], reverse = True)

    print(sorted_Stats)

    #format sorted_Stats to result[team,points]
    result = []
    for score in sorted_Stats:
        result.append((score[0],score[1][2]))

    return result