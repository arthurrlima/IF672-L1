class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s,%s' % (self.dado, self.anterior)


class Pilha:
    def __init__(self):
        self.topo = None
        
    def insere(self, novo_dado):
        """Insere um elemento no final da pilha."""

    # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)

    # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo

    # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo


    def pop(self):
        """Remove o elemento que está no topo da pilha."""

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

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



# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.
def newBox(box):
    if box != 0:
        if pilha.topo == None:
            pilha.insere(box)
            print("Insere o valor {0} no topo da pilha: {1}".format(box, pilha))
        
        else:   
            if checaPar(pilha.topo.dado, box):
                sBox = doSub(pilha.topo.dado, box)
                pilha.pop()
                newBox(sBox)
            else:
                pilha.insere(box)
                print("Insere o valor {0} no topo da pilha: {1}".format(box, pilha))
    else:
    
def newGame():
    result = []

    while True:
        box = input()
    
        if box:
            if box == "0":
                print (pilha)
            else:
                newBox(int(box))
        
            



nGames = int(input())

newGame()

# Remove elementos na pilha.
while pilha.topo != None:
    pilha.pop()
    print("Removendo elemento que está no topo da pilha: ", pilha)
