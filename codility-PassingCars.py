def solution(A):
    carF = 0
    carS = 0

    for car in A:
        if car == 0:
            carF += 1
        else:
           carS += carF

    if carS > 1000000000:
        return -1
    else:            
        return carS