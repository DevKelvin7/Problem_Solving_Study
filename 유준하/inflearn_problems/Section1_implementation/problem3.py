
from itertools import permutations

N, K = map(int, input().split())   # N, K 값 입력
numbers = list(map(int, input().split()))  # N개의 숫자 입력 받을 리스트
sumofnum = []  # 리스트 각 순열의 합을 저장할 리스트 생성
for i in permutations(numbers, K):  # 리스트 순열별 합을 구하기 위한 for 문
    sumofnum.append(sum(i))
sumofnum1 = set(sumofnum)  # 중복 제거를 위해 리스트 형태를 set으로 변환
sumofnum2 = sorted(sumofnum1, reverse = True)  # 오름 차순 정렬
print(sumofnum2[K-1])