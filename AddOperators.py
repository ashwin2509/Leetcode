def addOperators(num, target):
    res = []
    dfs(num, 0, 0, "", None, res, target)
    return res


def dfs(num, ind, value, expr, last, res, target):
    if ind == len(num):
        if value == target:
            res.append(expr)
        return

    for i in range(ind+1, len(num)+1):  #why is it ind+1
        if i == ind+1 or (i > ind and num[ind]!='0'):  #why is the first condition there
            s, x = num[ind:i], int(num[ind:i])
            if last == None:
                dfs(num, i, x, s, x, res, target) #why are we passing i
            else:
                dfs(num, i, value+x, expr+'+'+s, x, res, target)   #what is last exactly, is it the last value or the last number
                dfs(num, i, value-x, expr+'-'+s, -x, res, target)
                dfs(num, i, value-last+last*x, expr+'*'+s, last*x, res, target)

print(addOperators('105', 5))
