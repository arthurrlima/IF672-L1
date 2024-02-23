
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
    def __init__(self, id, flag = False):
        self.id = id
        self.Vizinhos = set()
        self.flag = flag
        self.distance = float('inf')
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
            v2.Vizinhos.add(v1)
            #self.Arestas.ins(Aresta(v1, v2, w))
            return True
        return False

    def BFSadapted(self, inicio, vFim):
        queue = Lista()
        inicio.distance = 0
        queue.ins(inicio)

        while queue:
            s = queue.pop()
            if not s:
                break

            for v in s.Vizinhos:
                if v.flag == False:
                    v.flag = True
                    v.distance = s.distance+1
                    if v == vFim:
                        return v.distance
                    queue.ins(v)
        return None     

def main():
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
                        grafo.new_aresta(matriz[i][j], matriz[i-1][j])
                        pass
                if j>0:
                    if matriz[i][j-1] != 1:
                        grafo.new_aresta(matriz[i][j], matriz[i][j-1])
                        pass
    oi, oj = origin
    fi, fj = destin

    if not grafo.BFSadapted(matriz[oi][oj], matriz[fi][fj]):
        print("Labirinto Impossivel")
    else:
        print(matriz[fi][fj].distance)

if __name__ == '__main__':
    main()