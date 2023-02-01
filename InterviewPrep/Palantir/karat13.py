"""
给 list of [name, time], time is string format: '1300' //下午一点
return: list of names and the times where their swipe badges within one hour. if there are multiple intervals that satisfy the condition, return any one of them.
name1: time1, time2, time3...
name2: time1, time2, time3, time4, time5...
example:
input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
output: {
'Martha': ['1600', '1620', '1530']
}
"""

def timeDiff (start, end):
    startH = start[:2]
    startM = start[2:]
    
    endH = end[:2]
    endM = end[2:]
    
    if startH == endH:
        return int(endM) - int(startM)
    else:
        return (60-int(startM)) + int(endM)

def freqAccess(records):
    office = dict()
    
    for name, time in records:
        if name not in office:
            office[name] = [time]
        else:
            office[name].append(time)
    
    answer = dict()
    
    for key, value in office.items():
        value.sort()
        if len(value) <= 1:
            continue
        for idx in range(len(value)-1):
            if timeDiff((value[idx]),(value[idx+1])) <= 60:
                if key not in answer:
                    answer[key] = [value[idx], value[idx+1]]
                else:
                    if value[idx] not in answer[key]:
                        answer[key].append(value[idx])
                    if value[idx+1] not in answer[key]:
                        answer[key].append(value[idx+1])
            
    print(answer)                

records = [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]

freqAccess(records)