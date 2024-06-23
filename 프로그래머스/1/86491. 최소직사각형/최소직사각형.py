def solution(sizes):
    answer = 0
    minimum = 0
    maximum = 0
    for i in sizes:
        if min(i) > minimum:
            minimum = min(i)
        if max(i) > maximum:
            maximum = max(i)
        
    return minimum * maximum