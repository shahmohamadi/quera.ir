inp = list(input())
for i in range(len(inp)):
    out1 = []
    repeat = inp[i]
    for j in range(i):
        out1 += list(repeat)
    out = out1 + inp[i:]
    print("".join([str(elm) for elm in out]))
