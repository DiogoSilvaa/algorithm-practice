A = [3,4,4,6,1,4,4]

def solution(N, A):
    arr = [0]*N
    maxC = 0
    maxChanged = False
    
    for x in range (len(A)):
        if A[x]>N+1:
            pass
        if (0 <= A[x]-1 <= N-1):
            arr[A[x]-1] = arr[A[x]-1]+1
            if arr[A[x]-1] > maxC:
                maxC = arr[A[x]-1]
                maxChanged = True
        elif maxChanged:
            arr = [maxC]*N
            maxChanged = False
            
    return arr
            

print(solution(5,A))