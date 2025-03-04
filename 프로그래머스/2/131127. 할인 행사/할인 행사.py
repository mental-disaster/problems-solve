from collections import Counter

def solution(want, number, discount):
    return sum(all(Counter(discount[i:i+10])[goods] >= amount for goods, amount in zip(want, number)) for i in range(len(discount)-9))