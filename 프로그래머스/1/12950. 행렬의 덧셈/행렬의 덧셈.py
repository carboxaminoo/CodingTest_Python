def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        adding = []
        for j in range(len(arr1[i])):
            adding.append(arr1[i][j] + arr2[i][j])
        
        answer.append(adding)
        del adding
            
    return answer