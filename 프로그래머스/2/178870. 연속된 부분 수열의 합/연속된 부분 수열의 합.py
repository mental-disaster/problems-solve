def solution(sequence, k):
    answer = [0, len(sequence)-1]
    s, e, total = 0, 0, sequence[0]
    
    while s < len(sequence):
        if total == k and answer[1]-answer[0] > e-s:
            answer = [s,e]
            
        if total > k:
                total -= sequence[s]
                s += 1
        else: 
            if e < len(sequence)-1:
                e += 1
                total += sequence[e]
            else:
                break
    
    return answer