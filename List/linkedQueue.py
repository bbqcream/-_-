class Node : 
    def __init__(self, elem, link = None):
        self.data = elem # 노드의 데이터
        self.link = link # 다음 노드를 가리키는 링크

class LinkedQueue: # 원형 연결 리스트
    def __init__(self): # 생성자
        self.tail = None # tail 없는 걸 기본
    
    def isEmpty(self): # 비었는지
        return self.tail == None # tail이 없으면 True 반환
    def isFull(self): # 다 찼는지
        return False # 끝이 없음
    
    def enqueue (self, item) : # 아이템 삽입
        node = Node(item, None) # node객체 생성
        if self.isEmpty() : # 비었으면
            self.tail = node # tail을 자신과 연결
            node.link = node # node의 link를 자기 자신과 연결

    def dequeue (self) : # 마지막 값 삭제
        if not self.isEmpty(): # 안비었으면
            data = self.tail.link.data # data에 tail의 link의 data를 삽입
            if self.tail.link == self.tail : # 근데 링크가 자기 자신이라면
                self.tail = None # None으로 하기
            else: # 아니라면 
                self.tail.link = self.tail.link.link # link의 link값으로 tail의 링크를 이동
            return data # data return
        
    # def dequeue(self):  # 요소 삭제
    #     if self.isEmpty():  # 비었으면 None 반환
    #         return None
    #     front = self.tail.link  # 첫 번째 노드
    #     data = front.data  # 첫 번째 노드의 데이터 저장
    #     if self.tail == front:  # 노드가 하나만 있을 경우
    #         self.tail = None  # 큐를 비움
    #     else:
    #         self.tail.link = front.link  # 첫 번째 노드를 제거하고 다음 노드를 가리키게 함
        
    #     return data  # 제거된 데이터 반환