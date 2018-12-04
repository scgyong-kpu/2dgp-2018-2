t = 1
for y in range(500, 400, -22):
    for x in range(47, 560, 44):
        print('  {"x":%4d, "y":%4d, "t":%2d},' % (x, y, t))
        t += 1
        if t > 10: t = 1