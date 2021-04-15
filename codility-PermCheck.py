A = [4,1,3,2]

def solution(A):

    A.sort()
    next = 1
    
    if A[0] != 1:
        return 0

    for item in A:
        if item == next:
            if next == len(A):
                return 1
            next +=1          
        else:
            return 0
    
    
print(solution(A))