def lastIndex(list,N,l):
    index=-1
    for i in range(N-1,-1,-1):
        if(list[i]==l):
            index=i
            break
    return index

N=int(input())
list = [int(i) for i in input().split()]   
location=int(input())                      
print(lastIndex(list, N, location)) 
