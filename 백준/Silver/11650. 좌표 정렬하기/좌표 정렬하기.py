n = int(input())
l = []
for i in range(n):
    d = input().split()
    l.append((int(d[0]), int(d[1])))
l.sort(key=lambda x:x[1])
l.sort(key=lambda x:x[0])
for x, y in l:
    print(x, y)