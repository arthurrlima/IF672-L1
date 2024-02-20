class Nodo:
    def __init__(self, objkt, proximo = None):
        self.conteudo = objkt
        self.prox = proximo

    def __repr__(self):
        if not None:
            if self.prox != None:
                return "%s %s"%(self.conteudo,self.prox)
            else:
                return "%s"% self.conteudo

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
            newNodo.prox = self.fst
            self.fst = newNodo
            self.size+=1

    def rmv(self):
        if not self.fst == None:
            self.fst = self.fst.prox
            self.size-=1

    def isEmpty(self):
        return self.fst == None

    def isPresent(self, id):
        if self.fst == None:
            return False
        
        cur = self.fst
        while(cur != None):
            if cur.conteudo == id:
                return True
            else:
                cur = cur.prox
        return False
    
    def doEmpty(self):
        self.fst = None
        self.lst = None
        self.size=0

    def __repr__(self):
        return str(self.fst)

    def __iter__(self):
        self.head = self.fst
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
        return "%s" % (self.id)

class Grafo:
    def __init__(self, size,  directed = False):
        self.vertices = [None]*size
        self.occ = 0

    def newVertice(self, v):
        if self.vertices[v] == None:
            self.vertices[v] = Vertice(v)
            self.occ += 1
        
    def newAresta(self, v1, v2):
        if self.vertices[v1].id == v1 and self.vertices[v2].id == v2:
            self.vertices[v1].addAdjacente(v2)
            self.vertices[v2].addAdjacente(v1)

    def dfs(self, v):
        visited = Lista()
        self.buscaProfudindade(v, visited)

        return str(visited)[::-1].rstrip('\n')
        
    def buscaProfudindade(self, v, visited):
        visited.ins(v)
    
        for adj in self.vertices[v].adjacentes:
            if adj not in visited:
                self.buscaProfudindade(adj, visited)

    def findPath(self, v1, v2):
        pass

def main():

    size = int(input())
    G = Grafo(size)

    for i in range(size-1, -1, -1):
        G.newVertice(i)

    while (True):
        entry = input()
        v1, v2, flag = entry.split()
        v1 = int(v1)
        v2 = int(v2)
        flag = int(flag)

        G.newAresta(v1, v2)

        if flag == 0:
            break

    for v in G.vertices:
        if (v.adjacentes.isEmpty()):
            print("{0}: Lista Vazia".format(v.id))
        else:
            print("{0}: {1}".format(v.id, v.adjacentes), end = "")
            print(" ")
            
    print()
    output = G.dfs(0)
    print(output, end = "")
    print(" ",end="")

if __name__ == '__main__':
    main()
