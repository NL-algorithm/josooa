#N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.
#
#입력
#첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.
#
#출력
#첫째 줄에 정답 정사각형의 크기를 출력한다.

import sys
#직사각형 사이즈 n*m 
n, m = list(map(int, sys.stdin.readline().split()))
#배열 입력
arr = []
for _ in range(n):
    arr.append(list(map(int , list(sys.stdin.readline().rstrip()))))
#최대 정사각형 변 초기화
max_dist  = 1

#max_dist update



#최대변**2
print(max_dist**2)