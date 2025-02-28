def solution(n):
    # return int(bin(0b1 << (list(reversed(bin(n))).index('1') if(int(list(reversed(bin(n))).index('1'))) else 1)) + bin(n >> list(reversed(bin(n))).index('1')+1)[2:], 2)
    return n + 1 + ((n & ((1 << n.bit_length()) - 1)) >> 1) if n & 1 else 0