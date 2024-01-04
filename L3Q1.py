class Node:
    def __init__(self, data, nxt = None):
        self.data = data
        self.prox = nxt

    def __repr__(self):
        return '%s,%s' % (self.data, self.prox)

class Lista:
    def __init__(self, size=0):
        self.fst = None
        self.lst = None
        self.size = size
    
    def ins(self, key):
        cell = Node(key)
        if self.fst == None:
            self.fst = cell
            self.lst = cell
        else:
            cell.prox = self.fst
            self.fst = cell

        self.size += 1

    def rmv(self, key):
        if self.fst is None:
            return

        cur = self.fst
        if cur.data == key:
            self.fst = self.fst.prox
            self.size -= 1
            return "DELETADO"

        else:
            while(cur.prox != None):
                if cur.prox.data == key:
                    cur.prox = cur.prox.prox
                    self.size -= 1
                    return "DELETADO"
                else:
                    cur = cur.prox

    def isEmpty(self):
        return self.fst == None
    
    def doEmpty(self):
        self.fst = None
        self.lst = None

    def __repr__(self):
        return "[" + str(self.fst) + "]"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None]*size

    def insert(self, key):
        index = spreadfn(key, self.size)
        if self.array[index] is None:
            self.array[index] = Lista()
            
        self.array[index].ins(key)

    def delete(self, key):
        i = spreadfn(key, self.size)
        if self.array[i] is None:
            return

        return self.array[i].rmv(key) 
        
    def search(self, key):
        i = spreadfn(key, self.size)
        if self.array[i] is None:
            return "404 - NOT FOUND"

        else:
            j = 0
            cur = self.array[i].fst

            while(cur != None):
                j += 1
                if cur.data == key:
                    return "{0} {1}".format(i,j)
                else:
                    cur = cur.prox
            return "404 - NOT FOUND"
        

def spreadfn(string, tableSize):
    if not string:
        return

    result = 0
    for i in range(len(string)):
        result += ord(string[i])*(i+1)

    return (result*17)%tableSize

def main():
    entry = input()
    M, C = entry.split()

    tabela = HashTable(int(M))

    for i in range(int(C)):
        entry = input()
        func, arg = entry.split()

        if func == "POST":
            tabela.insert(arg)

    entry_N = int(input())

    for i in range(entry_N):
        entry = input()
        func, arg = entry.split()

        if func == "POST":
            tabela.insert(arg)
        elif func == "GET":
            print(tabela.search(arg))
        elif func == "DELETE":
            output = tabela.delete(arg)
            if output != None:
                print(output)


if __name__ == '__main__':
    main()
