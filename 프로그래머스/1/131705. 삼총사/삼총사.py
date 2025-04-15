def solution(number):
    answer = 0
    num_len = len(number)
    for i in range(num_len-2):
        for j in range(i+1,num_len-1):
            for k in range(j+1,num_len):
                if number[i] + number[j] + number[k] == 0 :
                    answer +=1 
        
    return answer