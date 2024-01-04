def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
 
        heapify(arr, n, largest)
        
def createheap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def reverseheapify(heap, i):
    lower = i
    if i!=0:
        p = (i-1)//2
        if heap[p] < heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            lower = p
            reverseheapify(heap, lower)

def deleteheap(heap,valor):
    f = heap.index(valor)
    heap[-1], heap[f] = heap[f], heap[-1]
    last = heap.pop()
    n = len(heap)
    p = (f-1)//2
    if f!=0 and heap[p]<heap[f]:   
        reverseheapify(heap, f)
    else:
        heapify(heap,n,f)
 
def extractmax(arr):
    n = len(arr)
    arr[0], arr[-1] = arr[-1], arr[0]
    valor = arr.pop()
    heapify(arr, n, 0)
    print(valor)
    print(arr)
   
def createheap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr
 
def heapSort(arr):
    createheap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

def insertheap(heap, valor):
    heap.append(valor)
    n = len(heap)-1
    reverseheapify(heap, n)
    print(heap)

heap = []


# Fileiras F 
# Cadeiras Q

# caso assento disponivel -> primeiro assento disponivel de Finicio ate Ffim 

# caso assento ocupado -> 
#     p1 = pessoa com menor prioridade dentre todase pessoas sentadas, fp1 = fileira de p1, 

#     se prioridade pessoa cadastrada > p1:
#         fp1.remove(p1)
#         fp1.insere(PC)

#     else:
#         PC assiste sem assento. 

# def removeEvento(Pessoa):
#     if Pessoa is seated:
#         remove <pessoa>
#         insere <pessoa com maior prioridade> da <fila de espera>
#     else:
#         remove <pessoa> da <fila de espera>


    
# ao cadastrar Pessoa recebe numero de cadastro com base na ordem do cadastro, ou seja, a primeira pessoa recebe 1, segunda 2, etc 
# em casos de prioridades iguais, quem foi cadastrado primeiro tera maior prioridade nesse caso

# O código deve ter uma tabela hash que será utilizada nos comandos de entrada “VER”. Cada pessoa cadastrada é identificada unicamente através de seu nome e número de cadastro.
# A entrada inicia com um inteiro F, correspondente ao número de fileiras de assentos do teatro, e um inteiro Q, que representa a quantidade de assentos de cada fileira (Todas as fileiras têm quantidade de assentos iguais), separados por espaço.

# F Q

# OBS: Nos casos de teste, a quantidade de pessoas totais (sentadas + sem assento) nunca irá ultrapassar 2(F*Q).*

# Em seguida, será dado um inteiro N, correspondente à quantidade de comandos que serão dados ao sistema.

# N

# Em seguida, serão dados N comandos, que podem ser:

# CAD X P -> Cadastra a pessoa com nome X e prioridade P.
# REM X C -> Remove a pessoa de nome X e número de cadastro C do evento.
# VER X C -> Verifica a situação da pessoa de nome X e número de cadastro C.


class Pessoa:
    def __init__(self, nome, prioridade, cadastro):
        self.nome = nome
        self.prioridade = prioridade
        self.cadastro = cadastro

    def __repr__(self):
        return '%s,%s' % (self.nome, self.cadastro)




def main():

# A entrada inicia com um inteiro F, correspondente ao número de fileiras de assentos do teatro, e um inteiro Q, 
# que representa a quantidade de assentos de cada fileira (Todas as fileiras têm quantidade de assentos iguais), separados por espaço.
# F Q
    entry = input()
    F, Q = entry.split()
    F, Q = int(F), int(Q)


    #INICIA TEATRO
    tabela = HashTable(int(M))

    #COMANDOS
    entry = input()
    func, arg1, arg2 = entry.split()

    if func == "CAD":
        pass
        #Cadastra (Pessoa X, Prioridade P)

        # X (C) foi alocado(a) na fileira f -> Caso a pessoa foi elegível para ocupar algum assento,
        # deve-se imprimir esta mensagem com X sendo o nome da pessoa, C sendo o seu número de cadastro e f sendo o número da fileira em que ela foi inserida.

        # X (C) nao foi alocado(a) em nenhuma fileira -> Caso a pessoa cadastrada não seja elegível para ocupar um assento, 
        # conforme explicado acima. (Assistirá o evento sem assento até então)
            
    elif func == "REM":
        pass
        #Remove (Pessoa X, Cadastro C)

        # Removido(a) -> Caso a pessoa seja encontrada e removida do evento 
        # Inexistente -> Caso a pessoa não seja encontrada na lista de cadastrados do evento
        
    elif func == "VER":
        pass
        #Verifica situação (Pessoa X, Cadastro C)

        # Sem assento -> Caso a pessoa verificada não esteja alocada em algum assento de alguma fileira.

        # Sentado(a) na fileira f -> Caso a pessoa verificada esteja ocupando algum assento, 
        # deve ser impressa esta mensagem com “f” sendo o número da fileira que ela está.

        # Inexistente -> Caso a pessoa não esteja cadastrada no evento
        


if __name__ == '__main__':
    main()