# 두 개의 정 N면체와 정 M면체의 두개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

N, M = map(int, input().split())  # N, M 면채의 수를 입력 받는다
result = {}   # N주사위와 M주사위 값을 더했을때의 결과를 저장할 리스트
mostlist = []  # 최빈값을 저장할 리스트
for i in range(1, N+M+1):  # N과 M의 합의 최대값만큼 키 벨류 초기화
    result[i] = 0
for n in range(1, N+1):
    for m in range(1, M+1):
        result[n+m] += 1   # N 주사위와 M 주사위의 합에 해당하는 key의 value 값을 증가 시킨다
most = max(result.values())  # 제일 큰 value 값을 찾아서 most에 저장
for key, value in result.items():
    if value == most:  # most값과 동일한 value의 key 값을 mostlist 리스트에 저장
        mostlist.append(key)

print(sorted(mostlist))  # 오름 차순 정렬

