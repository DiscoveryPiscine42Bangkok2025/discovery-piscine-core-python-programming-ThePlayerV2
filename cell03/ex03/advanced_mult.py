n = int(input())

i = 0

while i <= n:
    ans = []

    ans.append("Table de %d:" % i)
    j = 0
    while j <= n:
        mult = j * i
        ans.append(str(mult))

        j += 1

    res = " ".join(ans)

    print(res)

    i += 1