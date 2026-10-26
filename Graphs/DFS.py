graph = {
    "a":["b", "d"],
    "b":[],
    "c":[],
    "d":["e", "g"],
    "e":["c"],
    "f":[],
    "g":["f"]
}

def dfs(graph, source_node):
    stack = []

    stack.append(source_node)
    while stack:
        node = stack.pop(-1)
        print(node)

        for n in graph[node]:
            stack.append(n)

dfs(graph, "a")