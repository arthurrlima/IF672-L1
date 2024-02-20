## Arthur Romaguera Lima -- ARL3
## Atividade Extra - Grafos - IF678 2023.2
import heapq
import pandas as pd

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

    def push(self, data):
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
        
class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        
    def add_vertice(self, value):
        self.vertices.add(value)
        self.arestas[value] = []
        
    def add_aresta(self, from_vertice, to_vertice, distance):
        self.arestas[from_vertice].append((to_vertice, distance))   # Grafo Direcionado
        # self.arestas[to_vertice].append((from_vertice, distance))  # Grafo Não Direcionado

def dijkstraHeap(Grafo, start, end):
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

def dijkstraLista(Grafo, start, end):
    queue = Lista()
    queue.push((0, start))
    visited = set()
    previous = {vertice: None for vertice in Grafo.vertices}
    distances = {vertice: float('infinity') for vertice in Grafo.vertices}
    distances[start] = 0

    while queue:
        current_distance, current_vertice = queue.pop()

        if current_vertice in visited:
            continue

        visited.add(current_vertice)

        if current_vertice == end:
            path = []
            while current_vertice is not None:
                path.insert(0, current_vertice)
                current_vertice = previous[current_vertice]

            cost = distances[end]
            return path, cost

        for neighbor, weight in Grafo.arestas[current_vertice]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertice
                    queue.push((new_distance, neighbor))

    return None, float('infinity')

# Driver
# Ler o DataFrame de um arquivo CSV, importando apenas as colunas desejadas
    
file_path = 'D:/code/Airports2.csv'  # Substitua pelo caminho correto do arquivo
df = pd.read_csv(file_path, usecols=['Origin_airport', 'Destination_airport', 'Distance'])

# Removendo linhas duplicadas com base nas colunas 'origem' e 'destino'
df_sem_duplicatas = df.drop_duplicates(subset=['Origin_airport', 'Destination_airport'])

# Exibindo o DataFrame resultante
print("\nDataFrame Sem Duplicatas:")
print(df_sem_duplicatas)


Grafo = Grafo()

# Carregando Vertices
for index, row in df_sem_duplicatas.iterrows():
    Grafo.add_vertice(row['Origin_airport'])
    Grafo.add_vertice(row['Destination_airport'])

# Carregando Arestas
for index, row in df_sem_duplicatas.iterrows():
    Grafo.add_aresta(row['Origin_airport'], row['Destination_airport'], int(row['Distance']))
    
# #Teste Manual
# Grafo.add_vertice('REC')
# Grafo.add_vertice('BSB')
# Grafo.add_vertice('SSA')
# Grafo.add_vertice('GIG')
# Grafo.add_vertice('GRU')

# Grafo.add_aresta('REC','SSA',100)
# Grafo.add_aresta('SSA','GRU',120)
# Grafo.add_aresta('GIG', 'GRU', 50)
# Grafo.add_aresta('BSB', 'GRU', 75)

# print(Grafo.arestas)

while(True):
    start_airport = input("Informe o aeroporto de origem: ")
    if start_airport == "quit":
        break
    end_airport = input("Informe o aeroporto de destino: ")


    #1A)
    path, cost = dijkstraLista(Grafo, start_airport, end_airport)

    if path:
        print("Estrutura: Lista")
        print(f"Menor caminho entre {start_airport} e {end_airport}: {path}")
        print(f"Custo do menor caminho: {cost}")
    else:
        print(f"Não há caminho entre {start_airport} e {end_airport}")


    #1B)
    path, cost = dijkstraHeap(Grafo, start_airport, end_airport)

    if path:
        print("\nEstrutura: Heap")
        print(f"Menor caminho entre {start_airport} e {end_airport}: {path}")
        print(f"Custo do menor caminho: {cost}")
    else:
        print(f"Não há caminho entre {start_airport} e {end_airport}")




