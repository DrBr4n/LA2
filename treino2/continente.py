'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def dfs_path(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_path(adj,d,vis,pai)
    return pai


def maior(vizinhos):

    graph_dict = {}

    for fronteira in vizinhos:
        for pais in fronteira:
            if pais in graph_dict:
                for p in fronteira:
                    if p != pais:
                        graph_dict[pais].add(p)
            else:
                tmp = fronteira.copy()
                tmp.remove(pais)
                graph_dict[pais] = set(tmp)

    #computar maior grafo
    biggest = 0
    for pais in graph_dict:
        tmp = len(dfs_path(graph_dict, pais, set(),{})) + 1
        print(dfs_path(graph_dict, pais, set(),{}))
        if tmp > biggest: biggest = tmp

    return biggest