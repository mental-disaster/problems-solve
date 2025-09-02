def solution(targets):
    answer = 1
    targets.sort(key=lambda t: t[0])
    min_y = targets[0][1]
    
    for i in range(len(targets) - 1):
        if min_y > targets[i][1]:
            min_y = targets[i][1]
        elif min_y <= targets[i][0]:
            answer += 1
            min_y = targets[i][1]
    if targets[-1][0] >= min_y:
        answer += 1
    
    return answer