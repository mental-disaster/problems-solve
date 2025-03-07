def solution(n):
    return n + 1 + ((n & ((1 << n.bit_length()) - 1)) >> 1) if n & 1 else 0
