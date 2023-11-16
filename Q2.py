class Carro:
    def __init__(self, size, prox_carro = None):
        self.size = size
        self.prox = prox_carro

    
    def __repr__(self):
        return '%s,%s' % (self.size, self.prox)



class Lista:
    def __init__(self, size=0):
        self.fst = None
        self.lst = None
        self.size = size
    
    def ins(self, size):
        newCarro = Carro(size)
        if self.fst == None:
            self.fst = newCarro
            self.lst = newCarro
        else:
            self.lst.prox = newCarro
            self.lst = newCarro

    def rmv(self):
        if not self.fst == None:
            self.fst = self.fst.prox

    def isEmpty(self):
        return self.fst == None
    
    def doEmpty(self):
        self.fst = None
        self.lst = None

    def __repr__(self):
        return "[" + str(self.fst) + "]"


def carregaBalsa(balsa, porto):
    carga = 0

    while porto.isEmpty() == False:
        if carga + porto.fst.size <= balsa.size:
            balsa.ins(porto.fst)
            carga += porto.fst.size
            print("removendo: " + str(porto.fst.size))
            porto.rmv()
            print(porto)
        else:
            break
    
def travessia(balsa, porto):
    n = 0
    while porto.isEmpty() == False:
        carregaBalsa(balsa, porto)
        n+=1
        balsa.doEmpty()
    return n

def newGame(size, n):
    balsa = Lista(size)
    m_esq = Lista()
    m_dir = Lista()

    for i in range(n):
        car = input()
        tam, lado = car.split()

        if lado.capitalize == "ESQUERDO":
            m_esq.ins(int(tam))
        else:
            m_dir.ins(int(tam))

    

    #começa do lado esquerdo
    result = travessia(balsa, m_esq) + travessia(balsa, m_dir)
    return result

def main():
    nTests = int(input())
    outputList = ""


    for n in range(nTests):

        size, nCars = input().split()

        result = newGame(int(size)*100, int(nCars))

        output = "Caso {0}: {1}".format(n+1, result)

        outputList = outputList + output + "\n" 

    print(outputList.strip())

if __name__ == '__main__':
    main()




# balsa = Lista(50)
# porto = Lista()

# porto.ins(10)
# porto.ins(10)
# porto.ins(10)
# porto.ins(20)
# porto.ins(20)
# porto.ins(20)

# print(porto.isEmpty())
# print(balsa.size)

# result = travessia(balsa,porto)



# print(result)




# def main():
#     nGames = int(input())
#     outputList = ""

#     for n in range(nGames):
#         #n rounds:



        
# if __name__ == '__main__':
#     main()
