def solution(s):
    num = len(s)//2
    return s[num] if len(s) %2 ==1 else s[num-1:num+1]