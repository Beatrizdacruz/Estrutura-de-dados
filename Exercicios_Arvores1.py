# python versão 3.9.7
# árvore de busca binária

# texto usado nos testes do código:
textoExemplo = '''todos os dias e um vai e vem
a vida se repete na estacao
tem gente que chega pra ficar
tem gente que vai pra nunca mais
tem gente que vem e quer voltar
tem gente que vai e quer ficar
tem gente que veio so olhar
tem gente a sorrir e a chorar'''

# Para lista encadeada:
class NoLinha:
    def __init__(self, linha):
        self.linha = linha
        self.proxLinha = None

class  NoPalavra:
    def __init__ (self, palavra):
        self.palavra = palavra
        self.ocorrs = 1 #por default, já sabe-se que ocorrreu pelo menos uma vez.
        self.proxPalavra = None
        self.linhas = None
        self.proxTam = None

    def addLinha(self, linha):
        novaLinha = NoLinha(linha)
        if self.linhas is None:
            self.linhas = novaLinha
            self.proxTam = novaLinha
        else:
            self.proxTam.proxLinha = novaLinha
            self.proxTam = novaLinha


class LeituraTexto:
    def __init__(self):
        self.primeiraP = None
        self.ultimaP = None


    # Função para evitar repetição de palavras nos nós:
    def verificaSePalavraExisteNo(self, palavra):
        proxPalavra = self.primeiraP
        while proxPalavra != None:
            if proxPalavra.palavra == palavra:
                return proxPalavra
            proxPalavra = proxPalavra.proxPalavra
        return False
    
    # ADICIONA AS PALAVRAS AOS NÓS ORDENANDO POR ORDEM ALFABÉTICA
    def adicionaNoELinhaOrdenada(self, palavra, linha):
        noExistente = self.verificaSePalavraExisteNo(palavra)
        if noExistente:
            noExistente.ocorrs += 1
            noExistente.addLinha(linha)
        else:
            novoNo = NoPalavra(palavra)
            novoNo.addLinha(linha)
            if self.primeiraP == None:
                self.primeiraP = novoNo
                self.ultimaP = novoNo
            else:
                noAnt = None
                proxNo = self.primeiraP
                while proxNo != None and palavra > proxNo.palavra:
                    noAnt = proxNo
                    proxNo = proxNo.proxPalavra
                if noAnt == None:
                    novoNo.proxPalavra = self.primeiraP
                    self.primeiraP = novoNo
                elif proxNo == None:
                    noAnt.proxPalavra = novoNo
                    self.ultimaP = novoNo
                else:
                    noAnt.proxPalavra = novoNo
                    novoNo.proxPalavra = proxNo
    # ---------------------------------------------------------

    # 1. lista linhas em que uma determinada palavra ocorre:
    def listaLinhasQuePalavraOcorre(self, palavra):
        proxNoPalavra = self.primeiraP
        saidaLinhas = ''
        linhaAnterior = None
        while proxNoPalavra != None:
            if proxNoPalavra.palavra == palavra:
                noLinha = proxNoPalavra.linhas
                while noLinha != None:
                    if noLinha.linha != linhaAnterior:
                        saidaLinhas += f' {noLinha.linha}'
                        linhaAnterior =  noLinha.linha
                        noLinha = noLinha.proxLinha
                    else:
                        noLinha = noLinha.proxLinha
            proxNoPalavra = proxNoPalavra.proxPalavra
        print(saidaLinhas)
    # ---------------------------------------------------------
    # 2. lista palavras por número de letras:
    def listaPalavrasPorNLetras(self, n):
        proxNo = self.primeiraP
        while proxNo != None:
            if len(proxNo.palavra) == n:
                print(proxNo.palavra)
            proxNo = proxNo.proxPalavra
    # ---------------------------------------------------------
    # 3. lista palavras em ordem alfabética:
    def recursao(self, no): #add recursao para printar os nós de trás para frente.
        if no == None:
            return
        self.recursao(no.proxPalavra)
        print(no.palavra)

    def palavrasOrdemAlfabetica(self, opcao, palavrinha3, palavrinha4):
        proxNo = self.primeiraP
        if opcao == 'c':
            while proxNo != None:
                if proxNo.palavra >= palavrinha3 or proxNo.palavra <= palavrinha4:
                    print(proxNo.palavra)
                proxNo = proxNo.proxPalavra
        if opcao == 'd':
            while proxNo != None:
                if proxNo.palavra <= palavrinha3 or proxNo.palavra >= palavrinha4: #tem problema aqui
                    self.recursao(proxNo)
                proxNo = proxNo.proxPalavra
    # ---------------------------------------------------------
    # 4. número de vezes em que uma palavra ocorre:
    def nVezezQuePalavraOcorre(self, palavra):
        proxNo = self.primeiraP
        while proxNo != None:
            if proxNo.palavra == palavra:
                print(f"{proxNo.palavra} {proxNo.ocorrs}")
                return proxNo.ocorrs
            proxNo = proxNo.proxPalavra
    # ---------------------------------------------------------
    # 5. lista todas as palavras:
    def listarTodasAsPalavras(self):
        proxNo = self.primeiraP
        while proxNo != None:
            print(proxNo.palavra)
            proxNo = proxNo.proxPalavra
    # ---------------------------------------------------------

# Código base para rodar os demais:
def main():
    contaLinhas = 1
    linhas = int(input())
    ler = LeituraTexto()
    for i in range(linhas):
        texto = input()
        palavraFormada = ''
        for caractere in texto:
            if caractere == ' ':
                if palavraFormada:
                    ler.adicionaNoELinhaOrdenada(palavraFormada, contaLinhas)
                    palavraFormada = ''
            else:
                palavraFormada += caractere

        if palavraFormada:
            ler.adicionaNoELinhaOrdenada(palavraFormada, contaLinhas)
        contaLinhas += 1

    buscador1 = None
    while buscador1 != 'e':
        buscador1 = str(input())
        if buscador1 == 'l':
            buscaPalavra = str(input())
            ler.listaLinhasQuePalavraOcorre(buscaPalavra)
        if buscador1 == 'x':
            n = int(input())
            ler.listaPalavrasPorNLetras(n)
        if buscador1 == 'o':
            opcao = str(input())
            palavrinha3 = str(input())
            palavrinha4 = str(input())
            ler.palavrasOrdemAlfabetica(opcao, palavrinha3, palavrinha4)
        if buscador1 == 'n':
            palavraABuscar = str(input())
            ler.nVezezQuePalavraOcorre(palavraABuscar)
        if buscador1 == 'a':
            ler.listarTodasAsPalavras()




main()