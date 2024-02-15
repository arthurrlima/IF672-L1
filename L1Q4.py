class Vertice:

    def __init__(self, label):
        self.label = label
        self.adjacentes = []

    



class Grafo:

    def __init__(self, arestas, vertices):
        self.vertices = vertices
        self.arestas = arestas

    pass



def buscaProfudindade(g):
    marcado = g.V*[False]
    antecessor = g.V*[-1]
    
    for v in range(0,g.V):
        if not marcado[v]:
            self.dfs(v, antecessor, marcado)

    for i in range(0,g.V):
        print(antecessor[i])
        del marcado
        del antecessor

def dfs(self, u, antecessor, marcado):
    marcado[v] = True
    for u in g.adj(v):
        if not marcado[u]:
            antecessor[u] = V
            self.dfs(u, antecessor, marcado)

