def recursion_rpn(rpn):
    global pos, ans
    singn = rpn[pos]
    pos += 1
    cnt = 1
    component = [''] * 2
    while cnt > -1:
        if rpn[pos] in ['-', '+', '*', '/']:
            a = recursion_rpn(rpn)
            component[cnt] = a
            cnt -= 1
        else:
            print(string[rpn])
            component[cnt] = int(rpn[pos])
            cnt -= 1
            pos += 1
    exec("global ans\nans = component[0]" + singn + "component[1]")
    return int(ans)


pos, ans = 0, 0
string = input("write RPN: ")
print(recursion_rpn(string[::-1]))
