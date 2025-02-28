def solution(n):
    return n + (1 << (len(bin(n)) - bin(n).rfind('1') - 1)) + int('0b0' + bin(n)[bin(n).replace('b', '').rfind('01') + 3:].replace('0', ''), 2)