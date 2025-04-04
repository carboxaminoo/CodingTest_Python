def solution(numbers):
    adding = []
    for i in range(10):
        if i in numbers:
            pass
        else: 
            adding.append(i)
    return sum(adding)