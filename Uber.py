def uberProblem(string, target):
    res = []
    recursion(string, [], res, target)
    return res

def recursion(string, path, res, target):
    if sum(path) == target and not string:
        t = ""
        for i, v in enumerate(path):
            if v > 0:
                if i == 0:
                    t += str(v)
                else:
                    t += '+' + str(v)
            else:
                t += str(v)
        res.append(t)

    for i in range(len(string)):
        num = int(string[:i+1])
        recursion(string[i+1:], path+[num], res, target)
        recursion(string[i+1:], path+[-num], res, target)



print(uberProblem('123456789', 1))
