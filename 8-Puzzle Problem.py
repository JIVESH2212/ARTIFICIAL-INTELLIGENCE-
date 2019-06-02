import copy
init=[[' ','5','2'],['1','8','3'],['4','7','6']]
goal=[['1','2','3'],['4','5','6'],['7','8',' ']]

def retindx(l):
    for m in range(len(l)):
        for n in range(len(l[m])):
            if l[m][n]==' ':
                return [m,n]
            
def up(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i-1][j]
    temp[i][j]=t2
    temp[i-1][j]=t1
    return(temp)

def down(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i+1][j]
    temp[i][j]=t2
    temp[i+1][j]=t1
    return(temp)

def left(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i][j-1]
    temp[i][j]=t2
    temp[i][j-1]=t1
    return(temp)

def right(l,i,j):
    temp=copy.deepcopy(l)
    t1=l[i][j]
    t2=l[i][j+1]
    temp[i][j]=t2
    temp[i][j+1]=t1
    return(temp)

def bfs(st,gl):
    q=[]
    i=0
    q.append(st)
    while(True):
        [j,k]=retindx(q[i])
        if([j,k]==[0,0]):
            temp=right(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=down(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif([j,k]==[0,len(q[0])-1]):
            temp=left(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=down(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif([j,k]==[len(q[0])-1,0]):
            temp=right(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=up(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif([j,k]==[len(q[0])-1,len(q[0])-1]):
            temp=left(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=up(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif(j==0):
            temp=left(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=down(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=right(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif(k==0):
            temp=up(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=down(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=right(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif(j==len(q[0])-1):
            temp=left(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=up(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=right(q[i],j,k)
            if temp not in q:
                q.append(temp)

        elif(k==len(q[0])-1):
            temp=left(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=up(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=down(q[i],j,k)
            if temp not in q:
                q.append(temp)

        else:
            temp=left(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=up(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=down(q[i],j,k)
            if temp not in q:
                q.append(temp)
            temp=right(q[i],j,k)
            if temp not in q:
                q.append(temp)

        temp=q[i]
        print(temp)
        if temp == gl:
            break
        i=i+1

bfs(init,goal)            
            
                
