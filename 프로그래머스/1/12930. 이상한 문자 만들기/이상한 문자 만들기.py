def solution(s):
    adding = s.split(" ")
    answer = []
    
    for i in adding:
        setting = []
        for j in range(len(i)):
            if j %2 == 0:
                setting.append(i[j].upper())
            else:
                setting.append(i[j].lower())
                
        answer.append(''.join(setting))
    return ' '.join(answer)