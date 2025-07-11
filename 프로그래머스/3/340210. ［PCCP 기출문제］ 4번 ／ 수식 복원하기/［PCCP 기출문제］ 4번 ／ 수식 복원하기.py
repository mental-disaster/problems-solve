def solution(expressions):
    def conv_radix(n, r):
        res = []
        while n:
            n, rem = divmod(n, r)
            res.append(str(rem))
        if res:
            return ''.join(reversed(res))
        else:
            return '0'
    
    def calc_exp(num1, num2, op, r):
        if op == '+':
            return conv_radix(int(num1, r) + int(num2, r), r)
        else:
            return conv_radix(int(num1, r) - int(num2, r), r)
    
    converted_exps = []
    targets = []
    min_radix = 2
    
    for expression in expressions:
        for c in expression:
            if c.isdecimal() and min_radix < int(c) + 1:
                min_radix = int(c) + 1
                
        if 'X' in expression:
            targets.append(expression)
        else:
            converted_exps.append(expression)
            
    passible_radixes = [i for i in range(min_radix, 10)]
    
    for radix in range(min_radix, 10):
        for exp in converted_exps:
            num1, op, num2, _, res  = exp.split()
            
            if res != calc_exp(num1, num2, op, radix):
                passible_radixes.remove(radix)
                break
    
    for i in range(len(targets)):
        for radix in passible_radixes:
            num1, op, num2, _, res  = targets[i].split()
            
            if res == '?':
                continue

            if res == 'X':
                res = calc_exp(num1, num2, op, radix)
            elif res != calc_exp(num1, num2, op, radix):
                res = '?'
                
            targets[i] = ' '.join([num1, op, num2, "=", res])
    
    return targets