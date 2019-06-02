import copy
m=[['#','#','#','#','#','#','#','#'],['#','-','-','-','-','-','-','#'],['#','-','#','#','#','-','-','#'],['#','-','#','*','#','-','-','#'],['#','-','-','-','#','-','-','#'],['#','-','#','#','#','-','-','#'],['#','P','-','-','-','-','-','#'],['#','#','#','#','#','#','#','#']]

def retindx(l,s):
    for m in range(len(l)):
        for n in range(len(l[m])):
            if l[m][n]==s:
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

def show(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end='')
        print('')
    print('\n\n -------------- \n\n')

def bfs(st):
    q=[]
    i=0
    q.append(st)
    [a,b]=retindx(q[0],'*')
    while(True):
        show(q[i])
        [j,k]=retindx(q[i],'P')
        if([a,b]==[j,k]):
            print('Food Found')
            break
        if(q[i][j-1][k]!='#'):
            if((q[i][j-1][k]=='-')):
                temp=up(q[i],j,k)
                if temp not in q:
                    q.append(temp)
            else :
                temp=up(q[i],j,k)
                temp[j][k]='-'
                if temp not in q:
                    q.append(temp)

        if(q[i][j+1][k]!='#'):
            if((q[i][j+1][k]=='-')):
                temp=down(q[i],j,k)
                if temp not in q:
                    q.append(temp)
            else :
                temp=down(q[i],j,k)
                temp[j][k]='-'
                if temp not in q:
                    q.append(temp)

        if(q[i][j][k-1]!='#'):
            if((q[i][j][k-1]=='-')):
                temp=left(q[i],j,k)
                if temp not in q:
                    q.append(temp)
            else :
                temp=left(q[i],j,k)
                temp[j][k]='-'
                if temp not in q:
                    q.append(temp)

        if(q[i][j][k+1]!='#'):
            if((q[i][j][k+1]=='-')):
                temp=right(q[i],j,k)
                if temp not in q:
                    q.append(temp)
            else :
                temp=right(q[i],j,k)
                temp[j][k]='-'
                if temp not in q:
                    q.append(temp)
        if(i<=len(q)):
            i=i+1
        else:
            break

bfs(m)
