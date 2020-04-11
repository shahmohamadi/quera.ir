inp = input()
# print(list(input()))
length = len(inp)
for i in range(0, length):
    # print(inp)
    inp = list(inp)
    # print(inp[i])
    # print(inp[:length - i])
    out1 = []
    repeat = inp[i]
    for j in range(0, i):
        out1 += list(repeat)
    out = out1 + inp[i:]
    # print(inp[i:])
    print("".join([str(elm) for elm in out]))
