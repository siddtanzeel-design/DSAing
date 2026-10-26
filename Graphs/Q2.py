#Checking if path exist between the source node and the destination
#(Undirected)

def dfs(src, dst, graph, vis):
    if src == dst:
        return True

    vis.add(src)
    ans = False
    for neighbor in graph[src]:
        if neighbor not in vis:
            ans = ans or dfs(neighbor, dst, graph, vis)

    return ans

graph = {
    "A":["B", "C"],
    "B":["A", "F", "D"],
    "C":["A"],
    "D":["B", "I", "G"],
    "E":["F", "H"],
    "F":["B", "E"],
    "G":["D", "H"],
    "H":["E", "G"],
    "I":["D"],
    "J":["K"],
    "K":["J"]
}
vis = set()
src, dst = input().split()

print(dfs(src, dst, graph, vis))