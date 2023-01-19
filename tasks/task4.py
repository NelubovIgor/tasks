import math

# переменная для теста:
mas = [1, 10, 2, 9]

def massive(m):
    count = 0
    centr = sum(m) / len(m)
    if len(list(filter(lambda x: x > centr, m))) >= len(list(filter(lambda x: x < centr, m))):
        centr = math.ceil(centr)
    else:
        centr = math.floor(centr)
    ender = [centr for _ in range(len(m))]
    while m != ender:
        for i in range(len(m)):
            if m[i] < centr:
                m[i] += 1
                count += 1
            elif m[i] == centr:
                continue
            else:
                m[i] -= 1
                count += 1
    return count

print(massive(mas))
