graph = {
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

def bfs(gr,st,gl):
    k=1
    q=[]
    visited=[False]*21
    q.append(st)
    visited[ord(st)-65]=True
    for i in range(0,21):
        z=q[i]
        print(q[i])
        if q[i]==gl:
            k=0
        for j in gr.get(z):
            if visited[ord(j)-65]==False:
                visited[ord(j)-65]=True
                q.append(j)
        if(k==0):
            break
        

s=input('Enter the start node')
e=input('Enter the ending node')
bfs(graph,s,e)
