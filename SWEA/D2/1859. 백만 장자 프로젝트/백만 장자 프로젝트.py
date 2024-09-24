T = int(input())
for test_case in range(1, T + 1):
    day = int(input())
    day_list = [int(i) for i in input().split()]
    money = 0
    price = 0
    for i in reversed(day_list):
        if i > price:
            price =i 
        money +=price - i
    print('#%d %d'%(test_case,money))

