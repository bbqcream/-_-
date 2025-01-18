MAX = 5 # 스택의 크기
array = [None] * MAX # 모든 요소를 None으로 초기화
top = -1 # 맨 마지막 원소의 위치

def isEmpty(): # 스택이 비었을 때
    if top == -1: # 공백상태라면
        return True
    else:
        return False
    
def isFull(): # 스택이 가득 찼을 때
    return top == MAX - 1 # 최댓값의 하나 뺀 값

def push(e): # 요소 집어넣기
    global top # 전역변수 top 사용 빨주노초 암어 레전드 때ㅑ노스
    if not isFull(): # 가득 차지 않았다면
        top += 1 # 스택에 하나를 채워주고
        array[top] = e # 요소를 집어넣기
    else:
        print("스택 가득 참 너 돌아가.")
        exit()
        
def pop(): # 마지막 요소 제거하기
    global top # 전역변수 top 사용
    if not isEmpty() : # 내 머리처럼 비지 않았다면
        top -= 1 # 스택 크기 줄여주고
        return array[top+1] # 반환하기 (근데 왜 top을 먼저 줄이는지는 의문)
    else:
        print("스택 빔짐빔우리집빔")
        exit()
        
def peek(): # 최댓값 찾기
    if not isEmpty(): # 안 비었으면
        return array[top] # 젤 위에꺼 반환
    else:
        pass