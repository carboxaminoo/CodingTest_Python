def solution(array):
    adding = [0]*(max(array)+1)

    for i in array:
        adding[i]+= 1
        
    top = 0    
    answer = 0
    for j in adding:
        if j == max(adding):
            top += 1
    if top >1:
        return -1
    else:
        return adding.index(max(adding))
    