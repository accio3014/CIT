class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class LinkedList :
    def __init__(self) :
        self.head = None
        self.length = 0

    def __len__(self) :         # 특수 메서드
        return self.length
    
    def appendleft(self, data) :
        if(self.head is None) :         # Linked list에 데이터가 없는 경우
            self.head = Node(data)
        else :                          # Linked list에 데이터가 있는 경우
            node = Node(data)           # 새로운 노드 생성
            node.next = self.head       # 새로 추가된 노드의 next가 head를 가르킴
            self.head = node            # head를 이동
        
        self.length += 1                # 길이 증가

    def append(self, data) :
        if(self.head is None) :
            self.head = Node(data)
        else :
            node = self.head                    # Linked list의 head를 가지고 옴
            while(node.next is not None) :      # append()는 제일 뒤에 추가하는 것이기 떄문에 node.nex가 None이 될때 까지 반복, node가 Linked list의 제일 뒤 값으로 이동
                node = node.next
            node.next = Node(data)              # 새로운 노드 추가

        self.length += 1

if __name__ == "__main__" :             # 프로그램을 직접 실행 했을 경우 여기 부터 실행
    my_list = LinkedList()
    print("연결 리스트 생성.  연결 리스트의 길이 = %s" % len(my_list))
    print()

    for i in range(4) :
        my_list.appendleft(i)
        my_list.append(i)
        print("%d을(를) 추가.  연결 리스트의 길이 = %s" % (i, len(my_list)))