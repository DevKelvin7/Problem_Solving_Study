# 자연수 N이 입력 되면 1부터 N 까지의 소수의 개수를 출력하는 프로그램을 작성하세요
# 만약 20이 입력 되면 1부터 20까지의 소수는 2, 3, 5, 6, 11, 13, 17, 19로 총 8개 입니다.
# 에라토스테네스 체


N = int(input())
ch = [0 for _ in range(N+1)]
cnt = 0
for i in range(2, N+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            ch[j] = 1
print(cnt)