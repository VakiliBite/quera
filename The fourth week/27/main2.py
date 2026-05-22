now_time = list(map(int,input().split(":")))
future_time = list(map(int,input().split(":")))

alarm = []
seconds = 0
minutes = 0
hours = 0

if now_time[0] != future_time[0] or now_time[1] != future_time[1] or now_time[2] != future_time[2]: 
    if future_time[2] < now_time[2] :
        seconds = 60 - now_time[2]
        seconds += future_time[2]
        now_time[1] = now_time[1] + 1
    else:
        seconds = future_time[2] - now_time[2]
    
    if future_time[1] < now_time[1] :
        minutes = 60 - now_time[1]
        minutes += future_time[1]
        now_time[0] = now_time[0] + 1
    else:
        minutes = future_time[1] - now_time[1]
        
    if future_time[0] < now_time[0]:
        hours = 24 - now_time[0]
        hours += future_time[0]
    else:
        hours = future_time[0] - now_time[0]
else:
    hours , minutes , seconds = 24 , 0 , 0
    

    
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    
        

    
    

