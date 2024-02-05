class Vertice:
    
    def __init__(self, id):
        self.id = id
        self.adjacentes = []
    
    def addAdjacente(self, adjacente):
        if adjacente not in self.adjacentes:
            self.adjacentes.append(adjacente)

    def __repr__(self) -> str:
        return "v({0})".format(self.id)

class Grafo:

    def __init__(self, directed = False):
        self.vertices = []

    def newVertice(self, v):
        if v.id not in self.vertices:
            self.vertices.append(v)
        
    def newAresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            v1.addAdjacente(v2)
            v2.addAdjacente(v1)

    def findPath(self, v1, v2):
        pass



grafo = Grafo()
v1 = Vertice(1)
v2 = Vertice(2)

grafo.newVertice(v1)
grafo.newVertice(v2)

grafo.newAresta(v1, v2)

for v in grafo.vertices:
    print(v)
    print(v.adjacentes)

