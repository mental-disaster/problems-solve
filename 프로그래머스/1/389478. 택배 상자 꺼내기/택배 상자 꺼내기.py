def solution(n, w, num):
    answer = 0
    
    top_q, top_r = divmod(n-1, w)
    target_q, target_r = divmod(num-1, w)
    
    answer += top_q - target_q
    top_r += 1
    target_r += 1
    
    if (top_q % 2 == target_q % 2):
        if (top_r >= target_r):
            answer += 1
    else:
        if (top_r + target_r > w):
            answer += 1
    
    return answer