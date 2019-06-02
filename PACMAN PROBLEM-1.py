import copy
import math

IS = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,1,0,2,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,3,1,1,1,1,1,0,0,0,0,0,0,0,0,0]


stack = []
TT = []
visited = []
empty =[]


def bfs(T,s):
    global count,IS

    goal = 0
    visited.append(IS)
    stack.append(IS)
    TS = IS[:]
    '''for i in T[s]:
        TEMPSS = TS[:]
        print('TEMPSS1',TEMPSS)
        TEMPSS[0]=TEMPSS[i]
        TEMPSS[i] = 0
        stack.append(TEMPSS)
        print('TEMPSS2',TEMPSS)
    print('stack',stack)
    prevx=0'''
        
        
    x = TS.index(3)
    print(x)
    r = math.floor(x/8)+1
    print(r)
    c = (x%8)+1
    print(c)
    print('started at (',str(r),' ',str(c),')')
        
    while len(stack)!=0:
        
        count = count +1
        #print('iteration',count)
        TEMPS = stack[len(stack)-1]
        TMP = TEMPS[:]              #-----------------------------------------
        visited.append(TMP)
        #print('visited 1',visited)
        del(stack[len(stack)-1])
        
        #print('curret state',TMP)
        

        x = TMP.index(3)
        print(x)
        '''R0 = INDEX[x+1][0]
        C0 = INDEX[x+1][1]'''
        ind = 0
    
        #print('initial TEMPS',TMP)

        
                  
        PM = probablemoves(x)
        print(PM)
        for j in PM:

            #print(str(count),' ',str(ind))
            r = math.floor(j/8)+1
            c = (j%8)+1
            print('moved to (',str(r),' ',str(c),')')
            ind = int(ind)+1
            TEMP = TMP[:]       #-------------------------------
            #print('TEMP:  ',TEMP)
            
                    
            if(TEMP[j]==2):
                print('goal state reached')
                goal =1
                break
                
            elif(TEMP[j] == 1):
                TEMP[x] = TEMP[j];
                TEMP[j] = 3;
                
            #print('temp',TEMP)
            #print('temps',TMP)
            #print('arr', arr)
            #print('visited 2',visited)
            
                
            if(TEMP not in visited):
                #print('not in visited')
                stack.append(TEMP)

        if(goal==1):
            break
        
                
         


def probablemoves(indx):
    pms = []
    
    if(indx<8):
        pms = [indx+1,indx+8]
    elif(indx>=56):
        pms = [indx-8,indx+1]
    elif(indx%8 == 0):
        pms = [indx-8,indx+1,indx+8]
    elif((indx+1)%8 == 0):
        pms = [indx-8,indx-1,indx+8]
    else:
        pms = [indx-8,indx-1,indx+1,indx+8]

    return pms
    
        


count =0
bfs(IS,0)
print('visited 2',visited)
print(count)
            
