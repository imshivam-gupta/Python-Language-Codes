def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

N=int(input())
list = [int(i) for i in input().split()]                      
reverseList(list, 0,N-1) 
print(*list,sep=' ')
