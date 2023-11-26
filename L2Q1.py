class Nodo:
    def __init__(self, val):
        self.val = val
        self.esquerda = None
        self.direita = None
        self.altura = 1

class Arvore:

    def insert(self, raiz, chave):
        if not raiz:
            return Nodo(chave)
        elif chave == raiz.val:
            return raiz
        elif chave < raiz.val:
            raiz.esquerda = self.insert(raiz.esquerda, chave)
        else: 
            raiz.direita = self.insert(raiz.direita, chave)

        raiz.altura = 1 + max(self.calcAltura(raiz.esquerda), self.calcAltura(raiz.direita))
      
        fatorBalanc = self.calcFatorBalanc(raiz)

        if fatorBalanc > 1 and chave > raiz.direita.val:
            return self.rotEsquerda(raiz)

        if fatorBalanc < -1 and chave < raiz.esquerda.val:
            return self.rotDireita(raiz)

        if fatorBalanc > 1 and chave < raiz.direita.val:
            raiz.direita = self.rotDireita(raiz.direita)
            return self.rotEsquerda(raiz)

        if fatorBalanc < -1 and chave > raiz.esquerda.val:
            raiz.esquerda = self.rotEsquerda(raiz.esquerda)
            return self.rotDireita(raiz)

        return raiz

    def remove(self, raiz, chave):
        if not raiz:
            print("Valor {0} inexistente".format(chave))
            return raiz
 
        elif chave < raiz.val:
            raiz.esquerda = self.remove(raiz.esquerda, chave)
 
        elif chave > raiz.val:
            raiz.direita = self.remove(raiz.direita, chave)
 
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
 
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
 
            temp = self.menorChave(raiz.direita)
            raiz.val = temp.val
            raiz.direita = self.remove(raiz.direita, temp.val)
 
        if raiz is None:
            return raiz
 
        raiz.altura = 1 + max(self.calcAltura(raiz.esquerda), self.calcAltura(raiz.direita))
 
        fatorBalanc = self.calcFatorBalanc(raiz)
 
        if fatorBalanc > 1 and self.calcFatorBalanc(raiz.direita) >= 0:
            return self.rotEsquerda(raiz)

        if fatorBalanc < -1 and self.calcFatorBalanc(raiz.esquerda) <= 0:
            return self.rotDireita(raiz)

        if fatorBalanc > 1 and self.calcFatorBalanc(raiz.direita) < 0:
            raiz.direita = self.rotDireita(raiz.direita)
            return self.rotEsquerda(raiz)

        if fatorBalanc < -1 and self.calcFatorBalanc(raiz.esquerda) > 0:
            raiz.esquerda = self.rotEsquerda(raiz.esquerda)
            return self.rotDireita(raiz)

        return raiz


    def calcAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura
    
    def calcFatorBalanc(self, raiz):
        if not raiz:
            return 0
        return self.calcAltura(raiz.direita) - self.calcAltura(raiz.esquerda)
    
    def menorChave(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz
        return self.menorChave(raiz.esquerda)

    def rotEsquerda(self, z):
        y = z.direita 
        T2 = y.esquerda 
  
        y.esquerda = z 
        z.direita = T2 
       
        z.altura = 1 + max(self.calcAltura(z.esquerda), self.calcAltura(z.direita))
        y.altura = 1 + max(self.calcAltura(y.esquerda), self.calcAltura(y.direita))
  
        return y 
 
    def rotDireita(self, z):
        y = z.esquerda 
        T3 = y.direita 
  
        y.direita = z 
        z.esquerda = T3 
   
        z.altura = 1 + max(self.calcAltura(z.esquerda), self.calcAltura(z.direita)) 
        y.altura = 1 + max(self.calcAltura(y.esquerda), self.calcAltura(y.direita)) 

        return y

    def buscaChave(self, raiz, chave, nivel = 0):
        if not raiz:
            return "Valor {0} inexistente".format(chave)
        elif chave < raiz.val:
            return self.buscaChave(raiz.esquerda, chave, nivel+1)
        elif chave > raiz.val:
            return self.buscaChave(raiz.direita, chave, nivel+1)
        else: 
            return "Nivel de {0}: {1}".format(chave, nivel)

    def imprimeOrdem(self, raiz, arg):
        if arg == "PREORDEM":
            return('['+self.preOrdem(raiz)[0:-1]+']')

        elif arg == "EMORDEM":
            return('['+self.emOrdem(raiz)[0:-1]+']')

        elif arg == "POSORDEM":
            return('['+self.posOrdem(raiz)[0:-1]+']')

    def preOrdem(self, raiz):
        if not raiz:
            return ""
    
        return("{0},{1}{2}".format(raiz.val, self.preOrdem(raiz.esquerda), self.preOrdem(raiz.direita)))

    def emOrdem(self, raiz):
        if not raiz:
            return ""

        return("{0}{1},{2}".format(self.emOrdem(raiz.esquerda), raiz.val, self.emOrdem(raiz.direita)))

    def posOrdem(self, raiz):
        if not raiz:
            return ""

        return("{0}{1}{2},".format(self.posOrdem(raiz.esquerda), self.posOrdem(raiz.direita), raiz.val))


def main():

    avl = Arvore()
    raiz = None

    while True:
        entry = input()
        if entry == "FIM":
            break
        else:
            func, arg = entry.split()

            if func == "ADICIONA":
                raiz = avl.insert(raiz, int(arg))
            elif func == "REMOVE":
                raiz = avl.remove(raiz, int(arg))
            elif func == "NIVEL":
                print(avl.buscaChave(raiz, int(arg)))
            elif func == "PRINT":
                print(avl.imprimeOrdem(raiz, arg))   
            else:
                pass


if __name__ == '__main__':
    main()
