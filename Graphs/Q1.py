#Checking if path exists between the source node and the destination
#(Directed Acyclic Graph - DAG)

def hasPath(src, dst, graph):
    if src == dst:
        return True

    ans = False
    for neighbors in graph[src]:
        ans = ans or hasPath(neighbors, dst, graph)

    return ans


graph = {
    "A":["B", "C"],
    "B":["F", "D"],
    "C":[],
    "D":["I", "G"],
    "E":["H"],
    "F":["E"],
    "G":["H"],
    "H":[],
    "I":[]
}

src, dst = input().split()
print(hasPath(src, dst, graph))