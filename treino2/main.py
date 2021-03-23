from continente import maior
from area import area

def main(): 
    
    #maior:
    #vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
    #print("in:", vizinhos)
    #print("out:", maior(vizinhos))

    print("<h3>area</h3>")
    mapa = ["..*..",
            ".*.*.",
            "*....",
            ".*.*.",
            "..*.."]
    print("in:",(3,2))
    print('\n'.join(mapa))
    print("out:",area((3,2),mapa))


if __name__ == '__main__':
    main()