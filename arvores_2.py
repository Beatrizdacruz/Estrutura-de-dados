# python versão 3.9.7

class No:
    def __init__(self, nome, funcao, addInfo):
        self.nome = nome
        self.esquerda = None
        self.direita = None
        self.funcao = funcao
        self.addInfo = addInfo

# 1. insere pessoa:
def procurarNome(raiz, nome):
    while raiz != None and raiz.nome != nome:
        if nome < raiz.nome:
            raiz = raiz.esquerda
        else:
            raiz = raiz.direita
    return raiz


def inserirNo(raiz, nome, funcao, addInfo):
    procuraNome = procurarNome(raiz, nome)
    if procuraNome != None:
        print(f'nome já existente: {nome}')
        return raiz
    else:
        print(f'nome inserido no cadastro: {nome}')
        novoNo = No(nome, funcao, addInfo)
        if raiz == None:
            return novoNo
        noAtual = raiz
        pai = None

        while noAtual != None:
            pai = noAtual
            if nome < noAtual.nome:
                noAtual = noAtual.esquerda
            elif nome > noAtual.nome:
                noAtual = noAtual.direita
            else:
                return raiz
        if nome < pai.nome:
            pai.esquerda = novoNo
        else:
            pai.direita = novoNo
        
        return raiz


# 2. lista nomes das pessoas:
def listaNomes(raiz):
    if raiz == None:
        print('cadastro vazio')
    else:
        paraListarNome(raiz)

def paraListarNome(no):
    if no != None:
        paraListarNome(no.esquerda)
        print(no.nome)
        paraListarNome(no.direita)


# 3. consulta departamento ou curso:
def consultaDeptoOuCurso(raiz, nome):
    no = procurarNome(raiz, nome)
    if no != None:
        if no.funcao == 'p' or no.funcao =='f':
            print("Departamento:", no.addInfo)
        if no.funcao == 'a':
            print("Curso:", no.addInfo)
    else:
        print(f"Nome inexistente no cadastro: {nome}")


# 4. lista nomes por classe:
def listaNomesPorClasse(raiz, classe):
    if raiz == None:
        print("não há pessoa na classe indicada")
        return

    else:
        encontrado = False
        noAtual = raiz
        anterior = None

        while noAtual != None:
            if noAtual.esquerda == None:
                if noAtual.funcao == classe:
                    print(noAtual.nome)
                    encontrado = True
                noAtual = noAtual.direita
            else:
                anterior = noAtual.esquerda

                while anterior.direita != None and anterior.direita != noAtual:
                    anterior = anterior.direita

                if anterior.direita == None:
                    anterior.direita = noAtual
                    noAtual = noAtual.esquerda
                else:
                    anterior.direita = None
                    if noAtual.funcao == classe:
                        print(noAtual.nome)
                        encontrado = True
                    noAtual = noAtual.direita

        if encontrado == False:
            print("não há pessoa na classe indicada")


# 5. consulta categoria associada a nome: 
def consultaAssociadaNome(raiz, nome):
    node = procurarNome(raiz, nome)
    if node != None:
        if node.funcao == 'p':
            print("Categoria: professor")
        if node.funcao == 'a':
            print("Categoria: aluno")
        if node.funcao == 'f':
            print("Categoria: funcionario")
    else:
        print(f"Nome inexistente no cadastro: {nome}")


# 6.Imprime a árvore:
# tentei usar a recursão para imprimir os nós
def preOrdem(raiz):
    if raiz != None:
        if raiz.esquerda != None:
            fesq = raiz.esquerda.nome
        else:
            fesq = 'nil'
        if raiz.direita != None:
            fdir = raiz.direita.nome
        else:
            fdir = 'nil'
        print(f'nome: {raiz.nome} fesq: {fesq} fdir: {fdir}')
        preOrdem(raiz.esquerda)
        preOrdem(raiz.direita)


# função principal para chamar as funções
def main():
    buscador1 = None
    raiz = None
    while buscador1 != 'e':
        buscador1 = input()
        
        if buscador1 == 'i':
            line2 = input()
            line3 = input()
            line4 = input()
            raiz = inserirNo(raiz, line2, line3, line4)
        if buscador1 == 'l':
            listaNomes(raiz)
        if buscador1 == 'd':
            nome = input()
            consultaDeptoOuCurso(raiz, nome)

        if buscador1 == 'a':
            classe = input()
            listaNomesPorClasse(raiz, classe)

        if buscador1 == 'c':
            nome = input()
            consultaAssociadaNome(raiz, nome)    
        if buscador1 == 'p':
            preOrdem(raiz)

main()
