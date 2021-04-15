def solution(A):

    A.sort()
    minPos = 1
    
    for item in A:
        if item == minPos:
            minPos += 1
            
    return minPos
