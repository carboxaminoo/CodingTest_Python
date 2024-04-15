def solution(bridge_length, weight, truck_weights):
    count = 0
    moving = []
    summ = 0
    stop = truck_weights.copy()
    
    while len(stop) !=0:
        if len(moving)<= bridge_length and summ + stop[0] <= weight:
            moving.append(stop[0])
            summ+= stop[0]
            del stop[0]
        else:
            moving.append(0)
            
        if len(moving)>=bridge_length: 
            summ-=moving[0]
            del moving[0]
            
        
        count +=1
            
    if len(stop)==0 and len(moving)!= 0:
        count+= bridge_length
        
    
    return count