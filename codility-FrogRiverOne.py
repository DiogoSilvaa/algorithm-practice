def solution(X, A):
    path = set()
    
    for second, leaf in enumerate(A):
        if leaf <= X:
            path.add(leaf)
            if len(path) == X:
                return second
    
    return -1
                
            