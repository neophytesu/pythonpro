for m in range(1, 17):
    nl = {}
    for n in range(1, 2 ** m + 1):
        b = n
        a = 0
        c = ''
        for i in range(m):
            if n % 2 == 1:
                n = (n * 3 + 1) / 2
                c = c + '0'
            else:
                n = n / 2
                c = c + '1'
        nl[b] = int(c, 2)
    nl = dict(sorted(nl.items(), key=lambda x: x[1]))
    ml = []
    for i in nl:
        for t in range(m):
            if i % 2 == 1:
                i = (i * 3 + 1) / 2
            else:
                i = i / 2
        if i % 2 == 1:
            ml.append('0')
        else:
            ml.append('1')
    print(''.join(ml))
