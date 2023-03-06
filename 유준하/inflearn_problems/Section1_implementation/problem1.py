# K번째 약수
# 입력 : 첫쨰 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1이상 10,000 이하이다. K는 1 이상 N 이하 
# 출력 : 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.

N, K = map(int, input().split())  #입력 받기
result = []   #약수 결과를 받아올 리스트 생성
for i in range(1, N+1):
    if N % i == 0:  # 1부터 N까지 나머지 값이 0일 될 경우 result 리스트에 추가
        result.append(i)
if not result:
    print(-1)
else:
    print(result[K-1]) # 어짜피 순서대로 값이 들어가기 때문에 K번째 작은 값은 result 리스트의 K-1번째 값이 결과