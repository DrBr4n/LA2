'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''
def check_adjs(x, y, mapa, adjs):

    if (y+1) < len(mapa[0]) and (y+1) > 0:
        if (mapa[x][y+1] == "." and (x,y+1) not in adjs):
            adjs.add((x,y+1))
            check_adjs(x, y+1, mapa, adjs)
    if (y-1) < len(mapa[0]) and (y-1) > 0:
        if (mapa[x][y-1] == "." and (x,y-1) not in adjs):
            adjs.add((x,y-1))
            check_adjs(x, y-1, mapa, adjs)
    if (x+1) < len(mapa) and (x+1) > 0:
        if (mapa[x+1][y] == "." and (x+1,y) not in adjs):
            adjs.add((x+1,y))
            check_adjs(x+1, y, mapa, adjs)
    if (x+1) < len(mapa) and (x-1) > 0:
        if (mapa[x-1][y] == "." and (x-1,y) not in adjs):
            adjs.add((x-1,y))
            check_adjs(x-1, y, mapa, adjs)

    return adjs

def area(p,mapa):
    x = p[0]
    y = p[1]

    adjs = set()
    adjs.add(p)
    adjs = check_adjs(p[0],p[1],mapa, adjs)

    return adjs


"""
..*.."
.*.*."
*...*"
.*.*."
..*.."
    def test_area_2(self):
        with test_timeout(self,1):
..*..
.*.*.
*....
.*.*.
..*..
            self.assertEqual(area((3,2),mapa),12)


"""
