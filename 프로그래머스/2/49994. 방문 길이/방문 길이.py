def solution(dirs):
    current = [0,0]
    trail = set()
    commands = {
        'U': lambda l: [l[0], min(5, l[1]+1)],
        'D': lambda l: [l[0], max(-5, l[1]-1)],
        'R': lambda l: [min(5, l[0]+1), l[1]],
        'L': lambda l: [max(-5, l[0]-1), l[1]],
    }
    
    for d in dirs:
        moved = commands[d](current)
        if(moved != current):
            trail.add(frozenset([tuple(moved), tuple(current)]))
            current = moved
    
    return len(trail)