N = int(input())
score = list(map(int, input().split()))
avg = (sum(score) / N) + 0.5
min = 100
for idx, x in enumerate(score):
    tmp = abs(x - avg)  # 거리 값
    if tmp < min:
        min = tmp
        chkscore = x
        result = idx + 1
    elif tmp == min:
        if x > chkscore:
            chkscore = x
            result = idx + 1
print(int(avg), result)
