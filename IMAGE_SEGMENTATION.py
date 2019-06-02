import cv2
import numpy as np


img = cv2.imread('img.png')

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, fimg = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

r = len(fimg)
c = len(img[0])
print(r,c)
count=0
w = list()
label = list()

def bfs(R,C):
    global count,label
    if(label[R][C]==1):
        return
    elif(fimg[R][C]==0):
        return
    else:
        N = func(R,C)
        label[R][C] = 1
        for i in range(0,len(N)):
            bfs(N[i][0],N[i][1])

def func2(R,C):
    queue = list()
    N = func(R,C)
    label[R][C] = 1
    for i in range(0,len(N)):
        v = [N[i][0],N[i][1]]
        queue.append(v)
    return queue

def bfs2(Qq):

    #print('called',Qq)
    while len(Qq)!=0:
        x = Qq[0]
        del Qq[0]
        R = x[0]
        C = x[1]
        #print('rc',R,C)
        if(label[R][C]==0):
            N = func(R,C)
            #print('N',N)
            label[R][C] = 1
            for i in range(0,len(N)):
                v = [N[i][0],N[i][1]]
                #print('v',v)
                Qq.append(v)
    
        
def func(row,col):
    ans = list()
    if(fimg[row-1][col-1] == 255 and label[row-1][col-1] == 0):
        ans.append([row-1,col-1])
    if(fimg[row-1][col] == 255 and label[row-1][col] == 0):
        ans.append([row-1,col])
    if(fimg[row-1][col+1] == 255 and label[row-1][col+1] == 0):
        ans.append([row-1,col+1])
    if(fimg[row][col+1] == 255 and label[row][col+1] == 0):
        ans.append([row,col+1])
    if(fimg[row+1][col+1] == 255 and label[row+1][col+1] == 0):
        ans.append([row+1,col+1])
    if(fimg[row+1][col] == 255 and label[row+1][col] == 0):
        ans.append([row+1,col])
    if(fimg[row+1][col-1] == 255 and label[row+1][col-1] == 0):
        ans.append([row+1,col-1])
    if(fimg[row][col-1] == 255 and label[row][col-1] == 0):
        ans.append([row,col-1])
    return ans

        
for i in range(0,r+1):
	for j in range(0,c+1):
		w.append(0)
	label.append(w)
	w=list()


#print(label[2])
for i in range(2,r-2):
    for j in range(2,c-2):
        if(fimg[i][j]==255 and label[i][j]==0):
            #print('called')
            count=count+1
            Q = func2(i,j)
            bfs2(Q)
            #bfs(i,j)
            #print(Q)
            
            '''for i in range (0,r):
                print(label[i])'''


print('Total number of regions',count)
#print(fimg[0])
#for i in range (0,r):
#   print(label[i])
#print(label)

'''n = np.asarray(img)
n[n>150]=255
n[n<150]=0
img = n.tolist()
print(img)'''

