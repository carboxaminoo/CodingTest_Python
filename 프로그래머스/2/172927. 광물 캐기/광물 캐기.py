def solution(picks, minerals):
    answer = 0
    mine_name = {0:[1,1,1], 1:[5,1,1], 2:[25,5,1]}
    mine = {'diamond': 100,'iron': 10,'stone': 1}
    a = []
    adding = 0
    
    # 5개를 단위로 다이아몬드는 100, 철은 10, 돌은 1으로 계산하여 우선순위 파악
    for i in range(len(minerals)):
        
        adding += mine[minerals[i]]
        
        # 만약 곡괭이보다 더 많은 양이 저장된다면 끝내기
        if len(a) >= sum(picks): 
            break

        if i  %5 == 4 or i ==len(minerals)-1:
            a.append(adding)
            adding = 0
        
    for j in range(3):
        # 곡괭이가 없다면 다음으로 넘어가기
        if picks[j] == 0:
            continue

        for k in range(picks[j]):
            # 곡괭이는 남았는데 광물이 없다면 return
            if a == []:
                return answer
            print(max(a), a)
            diamond,iron,stone = fun1(max(a))
            d,i,s = mine_name[j]
            answer += d*diamond + i*iron + s*stone
            print(answer)

            del a[a.index(max(a))]
        
    return answer

# 각 광물 별 갯수를 파악
def fun1(result):
    diamond = result//100
    iron = result%100//10
    stone = result%10
    return diamond, iron, stone

''' 
1. 캘 수 있는 광물의 개수보다 곡괭이의 개수가 적을 때 

2. 다이아 곡괭이로 최대한 이득을 낼 때

'''