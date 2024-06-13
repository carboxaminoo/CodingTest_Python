def solution(s):

    a = list(map(int,s.split()))
    min = a[0]
    max = a[0]
    for i in a[1:]:
        if min > i:
            min = i
        if max < i :
            max = i
    return f"{str(min)} {str(max)}"