singers = ["阿凱", "小琪", "大雄", "美美", "志明"]
scores = [
    [8, 9, 7, 10, 9],
    [9, 9, 9, 9, 9],
    [10, 6, 8, 10, 8],
    [7, 8, 8, 9, 6],
    [10, 10, 10, 3, 4],
]
finals = []
for s in scores:
    hi = 0
    lo = 0
    for i in range(5):
        if s[i] > s[hi]:
            hi = i
        if s[i] < s[lo]:
            lo = i
    if hi == lo:
        lo = (hi + 1) % 5
    total = 0
    for i in range(5):
        if i != hi and i != lo:
            total = total + s[i]
    finals.append(round(total / 3, 2))

ranks = []
for i in range(5):
    higher = 0
    for j in range(5):
        if finals[j] > finals[i]:
            higher = higher + 1
    ranks.append(higher + 1)

order = []
for i in range(5):
    order.append(i)
for i in range(5):
    for j in range(i + 1, 5):
        a = order[i]
        b = order[j]
        if ranks[b] < ranks[a]:
            order[i] = b
            order[j] = a

for i in order:
    print(ranks[i], singers[i], finals[i])