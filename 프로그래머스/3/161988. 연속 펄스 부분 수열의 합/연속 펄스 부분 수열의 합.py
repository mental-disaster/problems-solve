def solution(sequence):
    plus = sequence[0]
    minus = -sequence[0]
    answer = max(plus, minus)
    
    for s in sequence[1:]:
        plus, minus = max(s, minus+s), max(-s, plus-s)
        answer = max(answer, plus, minus)
    
    return answer