from aloca import aloca
from apelidos import apelidos
from frequencia import frequencia
from factoriza import factoriza
from repete import repete
from isbn import isbn
from futebol import tabela

def main():
    """
    # frequencia
    print("<h3>frequencia</h3>")
    texto = " o tempo perguntou ao tempo quanto tempo o tempo tem"
    print("in:",texto)
    print("out:",frequencia(texto))
    """
    """
    #factoriza
    print("<h3>factoriza</h3>")
    print("in:",28)
    print("out:",factoriza(28))
    """
    """
    # repete
    print("<h3>repete</h3>")
    print("in:","amanha",2)
    print("out:",repete("a",3))
    """
    """
    # isbn
    print("<h3>isbn</h3>")
    livros = {
        "Todos os nomes":"9789720047572",
        "Ensaio sobre a cegueira":"9789896604011",
        "Memorial do convent":"9789720046711",
        "Os cus de Judas":"9789722036757"
    }
    print("in:",livros)
    print("out:",isbn(livros))
    """
    #tabela
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

if __name__ == '__main__':
    main()
