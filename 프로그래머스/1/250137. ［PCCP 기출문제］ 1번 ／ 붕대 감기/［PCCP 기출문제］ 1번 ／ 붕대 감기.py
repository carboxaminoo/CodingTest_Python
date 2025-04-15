def solution(bandage, health, attacks):
    now_health = health
    now_time = 0
    print(now_health)
    
    for i in attacks:
        time = i[0]-1-now_time
        now_health = min(now_health + bandage[1]*time + time//bandage[0]*bandage[2], health)
        
        now_health -= i[1]
        print(now_health)
        now_time = i[0]
        
        if now_health <1 :
            return -1
        
    return now_health