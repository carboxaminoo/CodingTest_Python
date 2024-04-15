def solution(quiz):
    answer = []
    a=[]
    for i in quiz:
        a = i.split()
        if a[1]== '+':
            if int(a[0])+ int(a[2]) ==int(a[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(a[0]) - int(a[2]) == int(a[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer