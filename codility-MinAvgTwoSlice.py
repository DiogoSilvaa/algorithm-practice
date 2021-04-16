A = [4,2,2,5,1,5,8]

def solution(A):
    n = len(A)
    mi = 0
    cm = max(A)
 
    for idx in range(0, n-1):
        p = (A[idx] + A[idx+1])/2.0
        if p < cm:
            mi = idx
            cm = p
        if idx < n-2:
            t = (A[idx] + A[idx+1] + A[idx+2])/3.0
            if t < cm:
                mi = idx
                cm = t
 
    return mi 
