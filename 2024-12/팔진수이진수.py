import sys

input = sys.stdin.readline

number8 = int(input())

share = number8
answer = []

if number8 < 0:
    print("양수를 입력하세요")
    sys.exit()

while number8 > 0:
    remain = share % 2
    answer.append(str(remain))
    share = share // 2

print("".join(answer))