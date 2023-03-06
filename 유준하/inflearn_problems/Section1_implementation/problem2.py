# K 번째의 수
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름차순 정렬했을 때 K번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요

testcase = int(input())

for tc in (0, testcase):
    numbers = []
    N, s, e, k = map(int, input().split())     # 각 입력값을 띄어쓰기로 구분하여 입력 받는다
    numbers = list(map(int, input().split()))  # N만큼의 수를 띄어쓰기로 구분하여 입력 받는다
    pnumber = numbers[s-1:e]   # 필요구간인 s~e까지 문자열 슬라이싱 진행 단 리스트가 0부터 시작하기때문에 s-1부터 e까지의 문자만 따로 저장한다.
    pnumber.sort()   # 따로 저장된 구간 값을 오름차순 정렬
    print(pnumber[k-1])  # 리스트가 0부터 시작이기때문에 k-1번째 값을 결과로 출력한다
