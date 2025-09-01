#문제
#선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

#함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

#함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

#배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

#각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

#다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

#다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)

#전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.




from collections import deque
t = int(input())
for i in range(t):
    order = input()
    #revers가 연속으로 나올시 str은 그대로임
    order = order.replace("RR", "")
    #배열에 들어있는 수 n
    n= int(input())
    #배열
    x=input()
    #대괄호 삭제
    x = x[1:-1]
    #string list -> int list
    if x == "":
        intx = deque()
    else:
        intx = deque(map(int, x.split(',')))
    #error flag
    error = False
    #reverse flag
    re = False

    for i in order:
        #마지막에 뒤집을지 안 뒤집을지 결정
        if(i=='R'):
            re = not re
        elif(i=='D'):
            #error 컨
            if(len(intx)==0):
                error=True
                print("error")
                break
            #뒤집혀 있다면 뒤에서 pop
            elif(re):
                intx.pop()
            #안 뒤집혀있다면 앞에서 pop
            else:
                intx.popleft()
    if(not error):
        #마지막 reverse 처리
        if(re):
            intx = reversed(intx)
        print("["+",".join(map(str, intx))+"]")
    
    