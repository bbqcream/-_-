MAX = 8 # 큐의 크기
array = [None]*MAX # 모든 요소를 None으로 초기화
rear = 0 # 맨 마지막 원소
front = 0 # 맨 처음 원소의 앞

# 원형 큐는 rear의 값이 MAX를 넘어가도 9, 10... 이렇게 수가 계속 늘어나기에
# % MAX를 해서 원형 큐의 정확한 인덱스에 값을 집어넣을 수 있게해 준다.

def isEmpty(): # 비었는지
    return front == rear # 처음 원소의 위치와 마지막 원소의 위치가 같음

def isFull(): # 가득 찬지
    return front == (rear+1) % MAX # 마지막 원소의 값이 큐의 최대값의 -1이면 return
    # (rear + 1) % MAX를 하는 이유 : 큐는 기본적으로 최대 MAX-1의 값을 넣을 수 있음.
    # 그래서 +1을해 주고 거기에 큐의 크기를 나눠줌. 
    # 만약 가득 찼다면 front와 rear가 겹치니까 충돌이 발생하겠죠

def enqueue(item) : # 삽입하기 (맨 뒤에 삽입함)
    global rear
    if not isFull(): # 방이 꽉 안찼으면
        rear = (rear+1) % MAX # rear를 한 칸 옮겨주고
        array[rear] = item # 옮겨준 방에 item을 넣어주기
    else: # 방이 꽉 찼으면
        print("우리집 터지기 직전")

def dequeue() : # 삭제하기 (맨 앞의 값 삭제)
    global front
    if not isEmpty(): # 안비었으면
        front = (front+1) % MAX # front 한 칸 옮기고 (front는 항상 맨 처음 원소의 앞에 있음)
        return array[front] # 해당 방에 있는 값을 반환
    else: # 비었으면
        print("우리집빔")

def peek() : # 앞의 값 출력
    if not isEmpty():
        return array[(front+1) % MAX] # 가장 앞에 있는 방에 침입하고 리턴
    else:
        print("우리집빔")