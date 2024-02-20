import sys

class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
        self.next = None

    def __repr__(self):
        return '%s->%s' % (self.vertex, self.next)

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def ins(self, vertex, weight=0):
        new_node = Node(vertex, weight)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            

    def pop(self):
        if not self.tail:
            return None

        popped_node = self.tail
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

        return popped_node.vertex

    def __iter__(self):
        current = self.head
        while current:
            yield current.vertex
            current = current.next

    def __repr__(self):
        return "[" + str(self.head) + "]"


# #testando a estrutura Lista
# vertices = Lista()

# vertices.ins(1)
# vertices.ins(2)
# print(vertices)
# vertices.pop()
# print(vertices)
# vertices.ins(3)
# vertices.ins(5)
# print(vertices)

class MinHeap:
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
   
    def parent(self, pos): 
        return pos//2
 
    def leftChild(self, pos): 
        return 2 * pos 
   
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    def minHeapify(self, pos): 
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def push(self, element): 
        if self.size >= self.maxsize: 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def pop(self): 
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped







class Vertice:
    def __init__(self, id):
        self.id = id
        self.adjacentes = Lista()

    def __repr__(self):
        return str(self.id)
    
class Aresta:
    def __init__(self, v1, v2, w=0):
        self.v1 = v1
        self.v2 = v2
        self.w = w
    
    def __repr__(self):
        return "(%s,%s) w: %s" % (self.v1, self.v2, self.w)




v1 = Vertice(1)
v2 = Vertice(2)

a1 = Aresta(v1, v2)
#print(a1)

vertices = Lista()
vertices.ins(v1)
vertices.ins(v2)

#print(vertices)

class Grafo:
    def __init__(self, v=None, a=None):
        self.vertices = set()
        self.arestas = set()

    def add_vertice(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            return True
        return False

    def add_aresta(self, a):
        if (a.v1 in self.vertices and a.v2 in self.vertices and True):
            self.arestas.add(a)
            v1.adjacentes.ins(v2)
            v2.adjacentes.ins(v1)
            return True
        return False

    def __repr__(self):
        return "v: {0}, a: {1}".format(self.vertices, self.arestas)

#Testando Grafo
G = Grafo()

G.add_vertice(v1)
G.add_vertice(v2)
G.add_aresta(a1)
G.add_aresta(Aresta(v2, v1))
print(G)



def relaxar(u, v, w, antecessor, p):
    if p[v] > p[u] + w:
        antecessor[v] = u
        p[v] = p[u]+w

def dijkstra(G, s, w):

    antecessor = [-1]*len(G.vertices)
    p = [None]*len(G.vertices)

    p[s] = 0
    S = set()
    pq = minheap(G.vertices)

    while not pq.isEmpty():
        u = pq.pop()
        S.add(u)
        
        for v in u.adjacentes:
            relaxar(u,v,w, antecessor, p)



        






# def main():

#     entry = input()
#     Q,R,N = entry.split()
#     Q,R,N = int(Q), int(R), int(N)

#     # Q é o número total de quadras em Refeci numeradas de 0 a Q-1 (2 <= Q <= 300)
#     # R é o total de ruas existentes inicialmente
#     # N é o número de eventos, em ordem crescente de tempo, numerados 0 a N-1.


#     #constroi grafo
#     for i in range(R):

#         entry = input()

#     #comandos
#     for j in range(N):
#         entry = input()
#         if entry[0] == '1':
#             #new rua
#         #else:
#             #consulta
#             pass

    


#     while (True):
#         entry = input()
#         v1, v2, flag = entry.split()
#         v1 = int(v1)
#         v2 = int(v2)
#         flag = int(flag)

#         G.newAresta(v1, v2)

#         if flag == 0:
#             break

#     for v in G.vertices:
#         if (v.adjacentes.isEmpty()):
#             print("{0}: Lista Vazia".format(v.id))
#         else:
#             print("{0}: {1}".format(v.id, v.adjacentes), end = "")
#             print(" ")
            
#     print()
#     output = G.dfs(0)
#     print(output, end = "")
#     print(" ",end="")

# if __name__ == '__main__':
#     main()