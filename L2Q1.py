class Nodo:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class Arvore:

    def insert(self, pai, chave):
        if not pai:
            return Nodo(chave)
        
        elif chave < pai.chave:
            pai.esquerda = self.insert(pai.esquerda, chave)
        else: 
            pai.direita = self.insert(pai.direita, chave)

        #Atualiza Altura do pai
        pai.altura = 1 + max(self.calcAltura(pai.esquerda), self.calcAltura(pai.direita))

        #balancea se necessario e atualiza as alturas
        fatorBalanc = self.calcFatorBalanc(pai)
        if fatorBalanc > 1:
            if chave < pai.esquerda.chave:
                return self.rotDireita(pai)
            else:
                pai.esquerda = self.rotEsquerda(pai.esquerda)
                return self.rotDireita(pai)
 
        if fatorBalanc < -1:
            if chave > pai.direita.chave:
                return self.rotEsquerda(pai)
            else:
                pai.direita = self.rotDireita(pai.direita)
                return self.rotEsquerda(pai)
 
        return pai


    def calcAltura(self, pai):
        if not pai:
            return 0
        return pai.altura
    
    def calcFatorBalanc(self, pai):
        if not pai:
            return 0
        return self.calcAltura(pai.esquerda) - self.calcAltura(pai.direita)

    def rotEsquerda(self, b):
        a = b.direita
        T2 = a.esquerda
        a.esquerda = b
        b.direita = T2
        b.altura = 1 + max(self.calcAltura(b.esquerda), self.calcAltura(b.direita))
        a.altura = 1 + max(self.calcAltura(a.esquerda), self.calcAltura(a.direita))
        return a
 
     
    def rotDireita(self, b):
        a = b.esquerda
        T3 = a.direita
        a.direita = b
        b.esquerda = T3
        b.altura = 1 + max(self.calcAltura(b.esquerda), self.calcAltura(b.direita))
        a.altura = 1 + max(self.calcAltura(a.esquerda), self.calcAltura(a.direita))
        return a


    def buscaChave(self, pai, chave, nivel = 0):
        if not pai:
            return
        elif chave < pai.chave:
            return self.buscaChave(pai.esquerda, chave, nivel+1)
        elif chave > pai.chave:
            return self.buscaChave(pai.direita, chave, nivel+1)
        else: 
            return nivel


    def preOrdem(self, pai):
        if not pai:
            return

        # Visita o pai
        print("{0}".format(pai.chave), end=",")
        # Visita as subArvores em preOrdem da esquerda pra direita
        self.preOrdem(pai.esquerda)
        self.preOrdem(pai.direita)

    def emOrdem(self, pai):
        if not pai:
            return

        # Visita a subArvore esquerda em Ordem
        self.emOrdem(pai.esquerda)
        # isita o pai
        print ("{0}".format(pai.chave), end=",")
        # Visita a subArvore direita em Ordem
        self.emOrdem(pai.direita)

    def posOrdem(self, pai):
        if not pai:
            return
        
        # Visitar a subArvore esquerda
        self.posOrdem(pai.esquerda)
        # Visita a subArvore direita
        self.posOrdem(pai.direita)
        # Visita o pai
        print(pai.chave, end=",")


print("SOF")
arvo = Arvore()
pai = None
pai = arvo.insert(pai, 10)
pai = arvo.insert(pai, 5)
pai = arvo.insert(pai, 12)
pai = arvo.insert(pai, 7)
pai = arvo.insert(pai, 11)

arvo.preOrdem(pai)
print('\n')
print('\n')
pai = arvo.insert(pai, 8)

arvo.preOrdem(pai)

procuraChave = 7

print(arvo.buscaChave(pai, procuraChave))
