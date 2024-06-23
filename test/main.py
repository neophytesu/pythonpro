nl = []
d = False
for n in range(1, 1025):
    b = n
    a = []
    for i in range(10):
        if n % 2 == 1:
            n = (n * 3 + 1) / 2
            a.append('a')
        else:
            n = n / 2
            a.append('b')
        if n == 1:
            d = True
    c = ''.join(a)
    c = c[:5] + '|' + c[5:]
    print(b, ':', c)
