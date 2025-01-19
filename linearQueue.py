MAX = 8 # 큐 크기
array = [None]*MAX # 모든 요소를 None으로 초기화
rear = -1 # 맨 마지막 원소
front = -1 # 맨 첫 번째 원소의 앞

def isEmpty(): # 비었을 때
    return front == rear # 맨 첫 번째 원소의 앞이 맨 마지막 원소의 위치와 같으면 반환

def isFull(): # 큐가 가득 찼을 때
    return rear == MAX - 1 # rear가 더 이상 집어넣을 공간이 없을 때

def enqueue(e): # 삽입
    global rear # 전역변수 rear 사용
    if not isFull(): # 큐의 남은 공간이 있을 때
        rear += 1 # rear를 옮겨주고
        array[rear] = e # 옮겨준 위치에 e를 대입
    else:
        print("공간 없다 돌아가라")
        exit()

def dequeue() : # 삭제 (맨 뒤의 값)
    global front # 전역변수 front 사용
    if not isEmpty(): # 만약 큐에 값이 있다면
        front+=1 # front 앞으로 옮기고 
        return array[front] # 맨 앞의 값 반환
    else:
        print("큐 값 없음")
        exit()

def peek(): # 앞의 값 반환
    if not isEmpty(): # 안 비었으면
        return array[front+1] # 맨 앞의 값 반환
    else:
        pass # 값 없으면 넘어가기