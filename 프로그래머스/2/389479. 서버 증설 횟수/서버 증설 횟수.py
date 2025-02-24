def solution(players, m, k):
    servers = [p//m for p in players]
    
    if k > 1:
        for i in range(1, len(servers)):
            w_size = min(k-1, i)
            windows = servers[i-w_size:i]
            servers[i] = max(0, servers[i]-sum(windows))
    
    return sum(servers)