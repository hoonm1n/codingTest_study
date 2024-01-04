n = int(input())

time = [0,0,0]
result = 0

while True:
    if "3" in str(time[0]) + str(time[1]) + str(time[2]):
        result += 1
    if time[2] < 59:
        time[2]+=1
    else:
        time[2] = 0
        if time[1] < 59:
            time[1] += 1
        else:
            time[1] = 0
            if time[0] < 5:
                time[0] += 1
            else:
                break
               
print(result)
