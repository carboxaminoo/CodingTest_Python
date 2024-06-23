def solution(arr):
    answer = []
    answer.append(arr[0])
    i = 1
    while i < len(arr):
        if answer[-1] == arr[i]:
            i = i + 1
        else: 
            answer.append(arr[i])
            i = i + 1
    return answer