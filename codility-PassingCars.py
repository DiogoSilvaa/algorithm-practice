def solution(A):
    # write your code in Python 3.6
    carF = 0
    carS = 0
    for car in A:
        if car == 0:
            carF += 1
        else:
           carS += carF             
    return carS