class Nodo:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 0

class Arvore:





    def calcAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura
    
    def calcFatorBalanc(self, raiz):
        if not raiz:
            return 0
        return self.calcAltura(raiz.esquerda) - self.calcAltura(raiz.direita)


    def insert(self, raiz, chave):
        if not raiz:
            return Nodo(chave)
        
        elif chave < raiz.chave:
            raiz.esquerda = self.insert(raiz.esquerda, chave)
        else: 
            raiz.direita = self.insert(raiz.direita, chave)

        #Atualiza Altura da Raiz
        raiz.altura = 1 + max(self.getHeight(raiz.left), self.getHeight(raiz.right))


    def preOrdem(self, raiz):
        if not raiz:
            return
        
        print("{0}".format(raiz.valor), end="")
        self.preOrdem(raiz.esquerda)
        self.preOrdem(raiz.direita)
