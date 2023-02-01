for a in range (0, 2):
    for b in range(0, 2):
        for c in range (0, 2):
            for d in range (0, 2):
                if (a <= b) and (not (b == c)) and (d <= a):
                    print (a,  b,  c,  d)
