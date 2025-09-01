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
    
    