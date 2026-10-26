graph = {
    "a":["b", "d"],
    "b":[],
    "c":[],
    "d":["e", "g"],
    "e":["c"],
    "f":[],
    "g":["f"]
}

def bfs(graph, source_node):
    queue = []

    queue.append(source_node)
    while queue:
        node = queue.pop(0)
        print(node)

        for n in graph[node]:
            queue.append(n)

bfs(graph, "a")