class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s,%s' % (self.dado, self.anterior)


class Pilha:
    def __init__(self):
        self.topo = None
        self.size = 0
        
    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        self.size += 1


    def pop(self):
        assert self.topo, "Pilha !Vazia"

        self.topo = self.topo.anterior
        self.size -= 1

    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
def checaPar(x,y):
    if x%2 == y%2:
        return True
    else:
        return False
    
def doSub (x,y):
    if x >= y:
        return x-y
    else:
        return y-x

def newBox(pilha, box):
    if box != 0:
        if pilha.topo == None:
            pilha.insere(box)
        
        else:   
            if checaPar(pilha.topo.dado, box):
                sBox = doSub(pilha.topo.dado, box)
                pilha.pop()
                newBox(pilha, sBox)
            else:
                pilha.insere(box)
    else:
        return pilha
    
def newGame(pilha):
    while True:
        box = input()
        if box:
            if box == "0":
                return pilha
            else:
                newBox(pilha,int(box))
        

def main():
    nGames = int(input())
    outputList = ""

    for n in range(nGames):
        result = newGame(Pilha())
        output = "Pilha {0}: {1} {2}".format(n+1, result.size, result.topo.dado)
        print(output)   

if __name__ == '__main__':
    main()
