from collections import OrderedDict

nl = {}
for n in range(1, 1025):
    b = n
    a = 0
    while n != 1:
        a += 1
        if n % 2 == 1:
            n = (n * 3 + 1) / 2
        else:
            n = n / 2
    if a in nl:
        nl.get(a).append(b)
    else:
        nl[a] = [b]
nl = OrderedDict(sorted(nl.items()))
for i in nl:
    print(i, nl[i])
