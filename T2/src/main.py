import re
import sys
import threading

from algs4.cc import CC
from algs4.graph import Graph

def ler_dataset(linhas, pos):
    n = int(linhas[pos])
    pos += 1

    G = Graph(n)
    ja_inserida = set() 

    for _ in range(n):
        nums = [int(x) for x in re.findall(r"\d+", linhas[pos])]
        pos += 1

        v = nums[0]        
        vizinhos = nums[2:]  
        for w in vizinhos:
            aresta = (min(v, w), max(v, w))
            if aresta not in ja_inserida:
                ja_inserida.add(aresta)
                G.add_edge(v, w)

    return G, pos



class Pontes(CC):
    def __init__(self, G):
     
        self.pre = [0] * G.V    
        self.low = [0] * G.V    
        self.pai = list(range(G.V))
        self.cnt = 0           
        self.pontes = []       

        super().__init__(G)    

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count    
        self.pre[v] = self.cnt
        self.cnt += 1
        self.low[v] = self.pre[v]

        for w in G.adj[v]:
            if not self.marked[w]:
                self.pai[w] = v
                self.dfs(G, w)
                self.low[v] = min(self.low[v], self.low[w])
                if self.low[w] > self.pre[v]:
                    self.pontes.append((min(v, w), max(v, w)))
            elif w != self.pai[v]:
                self.low[v] = min(self.low[v], self.pre[w])


def main():
    linhas = [l for l in sys.stdin.read().splitlines() if l.strip()]
    pos = 0
    saida = []

    while pos < len(linhas):
        G, pos = ler_dataset(linhas, pos)
        pontes = sorted(Pontes(G).pontes) 

        saida.append("%d critical links" % len(pontes))
        for a, b in pontes:
            saida.append("%d - %d" % (a, b))
        saida.append("") 

    print("\n".join(saida))



if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(128 * 1024 * 1024) 
    t = threading.Thread(target=main)
    t.start()
    t.join()
