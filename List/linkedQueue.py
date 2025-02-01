class LinkedQueue: # 원형 연결 리스트
    def __init__(self): # 생성자
        self.tail = None # tail 없는 걸 기본
    
    def isEmpty(self)