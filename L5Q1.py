# Em uma rede social, há n usuários se comunicando entre si e m conexões de amizade. O processo de distribuição de notícias funciona da seguinte maneira:

# Um usuário i (1 <= i <= n) recebe a notícia de alguma fonte. Então, esse usuário passa a notícia para seus amigos, os amigos repassam para seus amigos e assim em diante. O processo acaba quando não há um par de amigos em que um sabe a notícia e o outro não.

# Para cada usuário i (1 <= i <= n), determine a quantidade de usuários que saberia a notícia se i iniciasse a distruição.


    # Na primeira linha você vai receber 2 valores n e m representando o número de usuários e de conexões entro os usuários.
    # Seguido por m linhas com 2 inteiros u e v representando os usuários conectados.

    # Imprima n inteiros. O i-th inteiro deve ser igual ao número de usuários que saberiam a notícia se o usuário i começar distribuindo-a.
class Vertice:
    def __init__(self, id, flag = False):
        self.id = id
        self.Vizinhos = set()
        self.flag = flag
        self.distance = float('inf')
        self.reachables = 0
    def __repr__(self) -> str:
        return str(self.id)


def propagar(root, v_start):
    print("visitando vizinhos[{0}] = {1}".format(v_start, v_start.Vizinhos))
    root.reachables +=1
    v_start.flag = True

    for v in v_start.Vizinhos:
        if v.flag == False:
            propagar(root, v)

    
def main():
    entry = input().split()

    n = int(entry[0])
    m = int(entry[1])

    vertices = [None]*n

    #carregando vertices
    for i in range(n):
        vertices[i] = Vertice(i+1)

    #carregando arestas
    for x in range(m):
        v1, v2 = input().split()
        v1, v2 = int(v1), int(v2)
        vertices[v1-1].Vizinhos.add(vertices[v2-1])
        vertices[v2-1].Vizinhos.add(vertices[v1-1])

    #calculando reachables
    for i in range(n):
        for v in vertices:
            v.flag = False

        propagar(vertices[i], vertices[i])
        print(vertices[i].reachables)

if __name__ == '__main__':
    main()
    



