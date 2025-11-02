import sys

n = int(sys.stdin.readline().strip())

if n <= 10:
    print(n)
    sys.exit(0)

decreasing_numbers = []

# 길이가 1 ~ 10인 감소하는 수 구하기
for length in range(1, 11):
    def backtrack(current, start):
        if len(current) == length:
            # 증가하는 수를 뒤집어서 감소하는 수로 저장
            decreasing_numbers.append(int(''.join(current[::-1])))
            return
        for i in range(start, 10):
            current.append(str(i))
            backtrack(current, i + 1)
            current.pop()
    backtrack([], 0)

decreasing_numbers.sort()

if n >= len(decreasing_numbers):
    print(-1)
else:
    print(decreasing_numbers[n])
