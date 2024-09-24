T = int(input())

for test_case in range(1, T + 1):
    day = int(input()) # 날짜 수
    day_list = [int(i) for i in input().split()] # 각 날짜의 물건가격 List
  
    money = 0 # 이득 비용
    price = 0 # 최대 물건가격

    # 해당 날짜보다 더 비싼 날이 있을 때 사고 파는 것이 이득이므로 
    # 역순으로 가격을 확인한다
    for i in reversed(day_list):
        if i > price:
            price =i 
        money +=price - i
    print('#%d %d'%(test_case,money))


