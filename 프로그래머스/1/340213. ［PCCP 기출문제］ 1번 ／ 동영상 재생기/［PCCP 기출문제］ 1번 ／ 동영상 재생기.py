def solution(video_len, pos, op_start, op_end, commands):
    
    a = [int(x) for x in pos.split(":")]
    now = a[0]*60 + a[1]
    b = [int(x) for x in op_start.split(":")]
    start = b[0]*60 + b[1]
    c = [int(x) for x in op_end.split(":")]
    end = c[0]*60 + c[1]
    d = [int(x) for x in video_len.split(":")]
    v_end = d[0]*60 + d[1]
    print(now)
    
    for i in commands:
        if now < end and now >= start: 
            print(i, now)
            now = end
        if i == 'next':
            now += 10
            if now > v_end:
                now = v_end
        elif i == 'prev':
            now -= 10
            if now < 0:
                now = 0
                
    if now < end and now >= start: 
            print(i, now)
            now = end
    return '{0:02d}:{1:02d}'.format(now//60, now%60)