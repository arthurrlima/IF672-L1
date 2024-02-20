
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return "%s->%s" % (self.data, self.next)

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def ins(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def peek(self):
        return None if self.is_empty() else self.head.data

    def __repr__(self):
        return '['+str(self.head)+']'

class Grafo:
    def __init__(self) -> None:
        self.Vertices = set()
        self.Arestas = Lista()
        
    def new_vertice(self, vertice):
        if isinstance(vertice, Vertice):
            self.Vertices.add(vertice)
            return True
        return False
    
    def new_aresta(self, v1, v2, w = 0):
        if (v1 in self.Vertices and v2 in self.Vertices and True):
            v1.Vizinhos.ins(v2)
            v2.Vizinhos.ins(v1) #não direcionado
            self.Arestas.ins(Aresta(v1, v2, w))
            return True
        return False

class Aresta:
    def __init__(self, v1, v2, p=0):
        self.v1 = v1
        self.v2 = v2
        self.peso = p
    def __repr__(self) -> str:
        return "({0},{1}){2}".format(self.v1, self.v2, self.peso)
        
class Vertice:
    def __init__(self, id):
        self.id = id
        self.Vizinhos = Lista()
    def __repr__(self) -> str:
        return self.id


grafo = Grafo()

v1 = Vertice('REC')
v2 = Vertice('BSB')

grafo.new_vertice(v1)
grafo.new_vertice(v2)
grafo.new_aresta(v1,v2)

print(grafo.Arestas)
print(grafo.Vertices)







#Driver
linha, coluna = input().split()
linha, coluna = int(linha), int(coluna)

matriz = [None]*linha

for l in range(linha):
    matriz[l] = [None]*coluna
    entry = input()
    matriz[l] = entry.split()

for i in range(linha):
    for j in range(coluna):
        #current
        cur = matriz[i][j]
        if cur != 1:
            if cur == 2:
                start = cur
            elif cur == 3:
                end = cur
            #vizinhos;
            if i < linha-1:
                if matriz[i+1][j] == 0:
                    matriz[i][j].insereVizinho(matriz[i+1][j])
                    matriz[i+1][j].insereVizinho(matriz[i][j])
            if j < coluna-1:
                if matriz[i][j+1]== 0:
                    matriz[i][j+1].insereVizinho(matriz[i][j])
                    matriz[i][j].insereVizinho(matriz[i][j+1])


