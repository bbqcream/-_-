# 여기서부턴 난이도 확 올라가니 주의

class Node: # Node정의
    def __init__(self, elem, link = None): # 생성자
        self.data = elem # 노드의 데이터
        self.link = link # 다음 노드를 가리키는 링크

class LinkedList: # LinkedList 정의
    def __init__ (self): # 생성자
        self.head = None # 헤드 포인터 없는 게 기본

    def isEmpty(self) : # 비었니
        return self.head==None # head 없으면 빈 거임
    
    def isFull(self): # 이거는 쓰잘때기 없음
        return False # 얘는 최대 없음
    
    def getNode(self, pos) : # 특정 위치의 노드 반환 pos는 position의 줄임말, 위치를 뜻함함함하ㅏㅈ아ㅏ하핳
        if pos < 0: # 위치가 0보다 작으면 잘못된 요청임
            return None # 그래서 None 반환
        node = self.head  # head부터 시작
        while pos > 0 and node != None: # head가 아니고 값이 들어있으면
            node = node.link # 다음 노드로 이동
            pos -= 1 # 위치 값 감소
        return node # 탐색한 노드의 값 반환
    
    def getEntry(self, pos) : # 노드 염탐
        node = self.getNode(pos) # 해당 노드 값 들고오기
        if node == None : # 업성요 값이 없어요
            print("값 없어요 아니 있었는데 아닝 없어여ㅛ 걍 없엉해ㅓㅁ네라")
            return
        else:
            return node.data # 염탐한 노드의 data 반환
        
    def insert(self, pos, elem): # 값 삽입
        before = self.getNode(pos-1) # 삽입 위치 직전 노드 가져오기
        if before == None: # 만약 앞이 없으면
            if self.head is not None: # head가 안비었으면
                self.head = self.head.link # head랑 새 노드(얘)랑 연결 (얘가 1빠 자리)
        else: # 앞에 값이 있으면
            node = Node(elem, self.head) # 얘를 앞 노드의 다음 노드로 설정하기
            before.link = node # 앞쪽 값의 링크를 자기로 하기
        
    def delete(self,pos): # 값 삭제
        before = self.getNode(pos-1) # 삭제 위치의 이전 노드 가져오기
        if before == None : # 앞의 값이 없으면
            if self.head is not None : # 근데 head가 있으면
                self.head = self.head.link # head를 다음 노드로 변경
        elif before.link != None : # 맨 앞의 값이 있음 다음 값고 있음
            before.link = before.link.link # 이전 노드를 다음 노드와 연결
