def solution(k, tangerine):
    group = dict()
    for t in tangerine:
        group[t] = group.get(t, 0) + 1
    list_group = sorted(group.values(), reverse=True)
    
    summation = 0
    for i in range(len(list_group)):
        summation += list_group[i]
        if k <= summation:
            return i+1
        
    return -1