A = [0,1,0,1,1]

def solution(A):
    # write your code in Python 3.6
    pairs = 0
    for fst in range (0,len(A)):
        if A[fst] == 1:
            pass
        else:
           pairs += A[fst+1:len(A)+1].count(1)             
    return pairs