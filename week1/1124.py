#문제
#자연수 X를 소인수분해하면, 곱해서 X가 되는 소수의 목록을 얻을 수 있다. 예를 들어, 12 = 2 × 2 × 3이다. 1은 소수가 아니다.
#
#어떤 수 X를 소인수분해 해서 구한 소수의 목록의 길이가 소수이면, 그 수를 언더프라임 이라고 한다. 12는 목록에 포함된 소수의 개수가 3개이고, 3은 소수이니 12는 언더프라임이다.
#
#두 정수 A와 B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 정수 중에서 언더프라임인 것의 개수를 구해보자.
#
#입력
#첫째 줄에 두 정수 A와 B가 주어진다.
#
#출력
#첫째 줄에 A보다 크거나 같고, B보다 작거나 같은 언더프라임 개수를 출력한다.
import sys
import math
a, b = map(int, sys.stdin.readline().split())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_count(n):
    count = 0
    temp = n
    
    # 2부터 √n까지 확인
    for i in range(2, int(math.isqrt(n)) + 1):
        while temp % i == 0:
            count += 1
            temp //= i
        if temp == 1:
            break
    
    # 남은 값이 1보다 크면 소수
    if temp > 1:
        count += 1
    
    return count

def is_under(n):
    
    prime_count = prime_count(n)

    if is_prime(prime_count):
        return True
    return False

count = 0
for i in range(a, b+1):
    if is_under(i):
        count +=1

print(count)