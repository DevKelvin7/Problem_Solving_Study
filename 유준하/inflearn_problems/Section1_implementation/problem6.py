# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

def digit_sum(x):
    digit_list = [int(a) for a in str(x)]
    sum_of_digit = sum(digit_list)
    return sum_of_digit

N = int(input())
numbers = list(map(str, input().split()))
result = []
for num in numbers:
    result.append(digit_sum(num))
print(max(result))