class Nodo:
    def __init__(self, objkt, proximo = None):
        self.conteudo = objkt
        self.prox = proximo

    def __repr__(self):
        return "%s -> %s" % (self.conteudo,self.prox)


class Lista:
    def __init__(self, size=0):
        self.fst = None
        self.lst = None
        self.size = size
    
    def ins(self, objkt):
        newNodo = Nodo(objkt)
    
        if self.fst == None:
            self.fst = newNodo
            self.lst = self.fst
            self.size+=1
        else:
            newNodo.prox = self.lst
            self.lst = newNodo
            self.size+=1

    def rmv(self):
        if not self.fst == None:
            self.fst = self.fst.prox
            self.size-=1

    def isEmpty(self):
        return self.fst == None

    def isPresent(self, objkt):
        if self.fst == None:
            return False
        
        cur = self.lst
        while(cur != None):
            if cur.conteudo == objkt:
                return True
            else:
                cur = cur.prox
        return False
    
    def doEmpty(self):
        self.fst = None
        self.lst = None
        self.size=0

    def __repr__(self):
        return "[" + str(self.lst) + "]"

    def __iter__(self):
        self.head = self.lst
        return self
    def __next__(self):
        if self.head == None:
            raise StopIteration
        
        x = self.head
        self.head = self.head.prox
        return x.conteudo

class Vertice:
    def __init__(self, id):
        self.id = id
        self.adjacentes = Lista()
    
    def addAdjacente(self, adjacente):
        if self.adjacentes.isPresent(adjacente) == False:
            self.adjacentes.ins(adjacente)

    def __repr__(self):
        return "'%s'" % (self.id)

class Grafo:
    def __init__(self, directed = False):
        self.vertices = Lista()

    def newVertice(self, v):
        if self.vertices.isPresent(v) == False:
            print("Adicionando Vertice: {0} ao grafo.".format(v))
            self.vertices.ins(v)
        
    def newAresta(self, v1, v2):
        print("{2} is in v:{0} , {3} is in v: {1}".format(self.vertices.isPresent(v1), self.vertices.isPresent(v2), v1, v2))
        print (self.vertices)
        if self.vertices.isPresent(v1) == True and self.vertices.isPresent(v2) == True:
            print("Adicionando Aresta entre: {0} e {1}".format(v1,v2))
            v1.addAdjacente(v2)
            v2.addAdjacente(v1)

    def findPath(self, v1, v2):
        pass



grafo = Grafo()
v1 = Vertice(1)
v2 = Vertice(2)
v3 = Vertice(3)
v4 = Vertice(4)
v5 = Vertice(5)



grafo.newVertice(v1)
grafo.newVertice(v2)
grafo.newVertice(v3)
grafo.newVertice(v4)
grafo.newVertice(v5)

grafo.newAresta(v1, v5)
grafo.newAresta(v3, v4)
grafo.newAresta(v2, v4)

for v in grafo.vertices:
    print("{0}: {1}".format(v.id, v.adjacentes))
