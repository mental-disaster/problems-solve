from itertools import count

def solution(w, b):
    for i in count():
        if max(w) >= (m := max(b)) and min(w) >= min(b):
            return i
        b[b.index(m)] = m//2