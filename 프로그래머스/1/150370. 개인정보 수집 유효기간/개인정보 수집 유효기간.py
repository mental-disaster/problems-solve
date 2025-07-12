def solution(today, terms, privacies):
    d = { k: int(v)*28 for k, v in map(str.split, terms)}
    f = lambda t: sum(map(lambda x,y: int(x)*y, t.split('.'), (336, 28, 1)))
    n = f(today)
    return [i for i,(p,t) in enumerate(map(str.split, privacies), 1) if n - f(p) >= d[t]]