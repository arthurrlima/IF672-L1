
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
        self.len = 0

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
        self.len += 1

    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.len -= 1
        return data

    def peek(self):
        return None if self.is_empty() else self.head.data

    def __repr__(self):
        return '['+str(self.head)+']'

class Vertice:
    def __init__(self, id):
        self.id = id
        self.Vizinhos = set()
    def __repr__(self) -> str:
        return str(self.id)
class Aresta:
    def __init__(self, v1, v2, p=0):
        self.v1 = v1
        self.v2 = v2
        self.peso = p
    def __repr__(self) -> str:
        return "({0},{1}){2}".format(self.v1, self.v2, self.peso)

class Grafo:
    def __init__(self) -> None:
        self.Vertices = set()
        self.Arestas = Lista()
        
    def new_vertice(self, verticeId):
        if not verticeId:
            return None
        
        v = Vertice(verticeId)
        self.Vertices.add(v)
        return v
        
    def new_aresta(self, v1, v2, w = 0):
        if (v1 in self.Vertices and v2 in self.Vertices and True):
            v1.Vizinhos.add(v2)
            v2.Vizinhos.add(v1) #não direcionado
            self.Arestas.ins(Aresta(v1, v2, w))
            return True
        return False

    def bfs(self, vOrig, vDest):
        if vOrig not in self.Vertices or vDest not in self.Vertices:
            return False
        
        visited = set()
        fila = Lista()
        caminho = Lista()
        caminho.ins(vOrig)

        fila.ins([vOrig, caminho])
        
        while not fila.is_empty():
            cur, path = fila.pop()

            if cur == vDest:
                return path.len-1
            
            if cur not in visited:
                visited.add(cur)

                for vizinho in cur.Vizinhos:
                    path.ins(vizinho)
                    fila.ins([vizinho, path])
        
        return False

grafo = Grafo()

v1 = Vertice('REC')
v2 = Vertice('BSB')

grafo.new_vertice(v1)
grafo.new_vertice(v2)
grafo.new_aresta(v1,v2)

print(grafo.Arestas)
print(grafo.Vertices)







#Driver


# Cada celula da matriz = Vertice()
# id = valor
# if i > 0, adiciona i-1 a Vertice.Adjacentes #não-direcionado
# if j > 0, adiciona j-1 a Vertice.Adjacentes #não direcionado

di, dj = input().split()
di, dj = int(di), int(dj) 
matriz = [-1]*di
grafo = Grafo()

for i in range(di):
    entry_linha = input().split()
    matriz[i] = [-1]*dj
    for j in range(len(entry_linha)):
        matriz[i][j] = int(entry_linha[j])
        

        if matriz[i][j] != 1:
            if matriz[i][j] == 2:
                origin = (i,j)
            elif matriz[i][j] == 3:
                destin = (i,j)
            matriz[i][j] = grafo.new_vertice((i, j))

            if i>0:
                if matriz[i-1][j] != 1:
                    print(matriz[i-1][j])

                    matriz[i][j].Vizinhos.add(matriz[i-1][j])
                    matriz[i-1][j].Vizinhos.add(matriz[i][j])
                    grafo.new_aresta(matriz[i][j], matriz[i-1][j])
                    pass
            if j>0:
                if matriz[i][j-1] != 1:
                    print(matriz[i][j-1])

                    matriz[i][j].Vizinhos.add(matriz[i][j-1])
                    matriz[i][j-1].Vizinhos.add(matriz[i][j])
                    grafo.new_aresta(matriz[i][j], matriz[i][j-1])
                    pass




            



print(matriz)
print(grafo.Vertices)
print(grafo.Arestas)
print(origin, destin)
oi, oj = origin
fi, fj = destin

print(grafo.bfs(matriz[oi][oj],matriz[fi][fj]))












# linha, coluna = input().split()
# linha, coluna = int(linha), int(coluna)

# matriz = [None]*linha

# for l in range(linha):
#     matriz[l] = [None]*coluna
#     entry = input()
#     matriz[l] = entry.split()

# for i in range(linha):
#     for j in range(coluna):
#         #current
#         cur = matriz[i][j]
#         if cur != 1:
#             if cur == 2:
#                 start = cur
#             elif cur == 3:
#                 end = cur
#             #vizinhos;
#             if i < linha-1:
#                 if matriz[i+1][j] == 0:
#                     matriz[i][j].insereVizinho(matriz[i+1][j])
#                     matriz[i+1][j].insereVizinho(matriz[i][j])
#             if j < coluna-1:
#                 if matriz[i][j+1]== 0:
#                     matriz[i][j+1].insereVizinho(matriz[i][j])
#                     matriz[i][j].insereVizinho(matriz[i][j+1])


