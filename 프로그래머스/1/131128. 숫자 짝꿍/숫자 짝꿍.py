def solution(X, Y):
    diff = [0] * 10
    dup = [0] * 10
    
    for i in X:
        diff[int(i)] += 1
    
    for i in Y:
        idx = int(i)
        if diff[idx] > 0:
            diff[idx] -= 1
            dup[idx] += 1
            
    ans = []
    if sum(dup[1:]):
        for i in range(9, -1, -1):
            ans.append(str(i) * dup[i])
        return ''.join(ans)
    
    if dup[0]:
        return '0'
        
    return "-1"