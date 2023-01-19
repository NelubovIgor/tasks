# переменные для теста:
n, m = 5, 4

def made_block(n, m, num):
    block = []
    while len(block) <= m - 1:
        block.append(n)
        n += 1
        if n > num:
            n = 1
    return block, block[-1]

def cyrcle_mas(n, m):
    num = n
    path = [made_block(n + 1 - n, m, num)[0]]
    n = path[0][-1]
    while True:
        block, n = made_block(n, m, num)
        path.append(block)
        if n == 1:
            break
    return path

result = cyrcle_mas(n, m)

for x in result:
    print(x[0], end='')
