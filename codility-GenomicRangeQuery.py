def solution(S,P,Q):
    arr = []
    for x in range (0, len(P)):
        if 'A' in S[P[x]:Q[x]+1]:                               
            arr.append(1)
        elif 'C' in S[P[x]:Q[x]+1]:
            arr.append(2)
        elif 'G' in S[P[x]:Q[x]+1]:
            arr.append(3)
        else:
            arr.append(4)
    return arr