def solution(phone_number):
    answer = str(phone_number)
    c = len(answer)
    
    return '*'*(c-4)+answer[c-4:]