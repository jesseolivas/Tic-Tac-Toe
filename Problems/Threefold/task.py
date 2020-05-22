intlist = list(input())
avg = []
for x in intlist:
    y = (int(x) + int(x + 1) / 2)
    avg.append(int(y))
print(avg)