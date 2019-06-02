def dfs(graph,start,goal,path=[]):
    q=[start]
    while(q):
        v = q.pop(0)
        if v not in path:
            path = path+[v]

            if v==goal:
                return path
            q=q+graph[v]

    return path



def bfs(graph, start, goal,path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      if v==goal:
          return path
      q=q+graph[v]
  return path


graph={'A':['B','C','D'],'B':['E','F'],'C':['G','H'],'D':['I','J'],'E':['K','L'],'F':['M'],'G':['N'],'H':['O'],'I':['P','Q'],'J':['R'],'K':['S'],'L':['T'],'M':[],'N':[],'O':[],'P':['U'],'Q':[],'R':[],'S':[],'T':[]}
print("BFS traversal from start state A to goal state H")
bfspath=bfs(graph, 'A','M');
print(bfspath)
print("No of nodes traversed")
print(len(bfspath))

print("DFS traversal from start state A to goal state H")
dfspath=dfs(graph, 'A','M');
print(dfspath)
print("No of nodes traversed")
print(len(dfspath))