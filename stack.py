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
    
## 괄호 검사 문제 ##

# 조건1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함. ex) '([{}] 안됨'
# 조건2 : 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 함 ex) '][ 안됨'
# 조건3 : 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안됨 ex) ' [ }, {) 안됨'

def checkBrackets(statement):
    stack = ArrayStack(100) # 용량이 100인 스택 객체 생성
    openParentheses = ["{", '[', '(']
    closeParentheses= ['}', ']', ')']
    
    for ch in statement : # 입력 값을 하나씩 검사
        if ch in openParentheses: # 여는 괄호 중 하나가 같다면
            stack.push(ch) # 스택에 삽입
            
        elif ch in closeParentheses: # 닫는 괄호 중 하나가 같다면
            if stack.isEmpty(): # 비었으면
                return False # 조건 2 위반 (비었는데 닫는 괄호가 나왔다는 거는 오른쪽 괄호가 왼쪽 괄호보다 먼저 나왔잖아)
            else:
                left = stack.pop()
                if (ch == openParentheses[0] and left !=closeParentheses[0]) or (ch == openParentheses[1] and left!=closeParentheses[1]) or (ch==openParentheses[2] and left !=closeParentheses[2]):
                    return False # 조건 3 위반
                
    return stack.isEmpty() # False 반환되면 조건 1 위반 (뭐 하나는 여는 괄호만 들어갔다는 얘기)