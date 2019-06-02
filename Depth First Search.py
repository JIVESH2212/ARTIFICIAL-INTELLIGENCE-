graph1 = {
    'A' : ['B','C','D'],
    'B' : ['A','E','F'],
    'C' : ['A','G','H'],
    'D' : ['A','I','J'],
    'E' : ['B','K','L'],
    'F' : ['B','M'],
    'G' : ['N','C'],
    'H' : ['C','O'],
    'I' : ['D','P','Q'],
    'J' : ['D','R'],
    'K' : ['E','S'],
    'L' : ['E','T'],
    'M' : ['F'],
    'N' : ['G'],
    'O' : ['H'],
    'P' : ['I','U'],
    'Q' : ['I'],
    'R' : ['J'],
    'S' : ['K'],
    'T' : ['L'],
    'U' : ['P'],
}

def dfs(graph, node,goal, visited):
    if goal in visited:
        return visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
                dfs(graph,n,goal,visited)
    
    return visited

visited = dfs(graph1,'A','N', [])
print(visited)
