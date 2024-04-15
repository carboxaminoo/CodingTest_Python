
def solution(string, n):
    answer = []
    strings = sorted(string)
    str =''
    
    while strings:
        str =''
        for i in strings:
            if str =='' or str[n] > i[n]:
                str = i
        
        answer.append(str)
        del strings[strings.index(str)]
        
    
    return answer