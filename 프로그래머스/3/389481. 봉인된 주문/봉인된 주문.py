def solution(n, bans):
    def to_index(spell):
        index = 0
        spell = spell[::-1]
        for i in range(len(spell)):
            index += 26**i*(ord(spell[i])-96)
        return index
    
    def to_spell(index):
        spell = ''
        while index > 0:
            index -= 1
            spell = chr(ord('a') + index % 26) + spell
            index //= 26
        return spell
    
    bans.sort(key=lambda x: (len(x), x))
    
    for ban in bans:
        ban_idx = to_index(ban)
        if ban_idx <= n:
            n += 1
        else:
            break
    
    return to_spell(n)