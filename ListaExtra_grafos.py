import heapq
#import pandas as pd

class vertice:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def ins(self, data):
        new_vertice = vertice(data)
        if self.is_empty():
            self.head = new_vertice
            self.tail = new_vertice
        else:
            self.tail.next = new_vertice
            self.tail = new_vertice

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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Vertex:
    def __init__(self, id, w=0):
        self.id = id
        self.w = w
        self.vizinhos = Lista()
        

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        
    def add_vertice(self, value):
        self.vertices.add(value)
        self.arestas[value] = []
        
    def add_aresta(self, from_vertice, to_vertice, distance):
        self.arestas[from_vertice].append((to_vertice, distance))   
        self.arestas[to_vertice].append((from_vertice, distance))  # considering undirected Grafo

def dijkstra(Grafo, start, end):
    heap = [(0, start)]
    visitados = set()
    anterior = {vertice: None for vertice in Grafo.vertices}
    distances = {vertice: float('infinity') for vertice in Grafo.vertices}
    distances[start] = 0

    while heap:
        current_distance, current_vertice = heapq.heappop(heap)

        if current_vertice in visitados:
            continue

        visitados.add(current_vertice)

        if current_vertice == end:
            path = []
            while current_vertice is not None:
                path.insert(0, current_vertice)
                current_vertice = anterior[current_vertice]

            cost = distances[end]
            return path, cost

        for neighbor, weight in Grafo.arestas[current_vertice]:
            if neighbor not in visitados:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    anterior[neighbor] = current_vertice
                    heapq.heappush(heap, (new_distance, neighbor))

    return None, float('infinity')

# Exemplo de uso
Grafo = Grafo()
Grafo.add_vertice("JFK")
Grafo.add_vertice("LAX")
Grafo.add_vertice("ORD")
Grafo.add_vertice("DFW")
Grafo.add_vertice("MIA")

Grafo.add_aresta("JFK", "LAX", 2500)
Grafo.add_aresta("JFK", "ORD", 800)
Grafo.add_aresta("LAX", "ORD", 1800)
Grafo.add_aresta("ORD", "DFW", 900)
Grafo.add_aresta("DFW", "MIA", 1300)

start_airport = input("Informe o aeroporto de origem: ")
end_airport = input("Informe o aeroporto de destino: ")

path, cost = dijkstra(Grafo, start_airport, end_airport)

if path:
    print(f"Menor caminho entre {start_airport} e {end_airport}: {path}")
    print(f"Custo do menor caminho: {cost}")
else:
    print(f"Não há caminho entre {start_airport} e {end_airport}")


# Ler o DataFrame de um arquivo CSV, importando apenas as três primeiras colunas
    
file_path = 'caminho/do/arquivo.csv'  # Substitua pelo caminho correto do seu arquivo
df = pd.read_csv(file_path, usecols=['origem', 'destino', 'distancia'])

# Exibindo o DataFrame original
print("DataFrame Original:")
print(df)

# Removendo linhas duplicadas com base nas colunas 'origem' e 'destino'
df_sem_duplicatas = df.drop_duplicates(subset=['origem', 'destino'])

# Exibindo o DataFrame resultante
print("\nDataFrame Sem Duplicatas:")
print(df_sem_duplicatas)
