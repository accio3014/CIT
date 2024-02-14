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
    
    def __str__(self) :         # __str__ 특수 메서드는 object를 print()했을 경우 실행 됨
        if(self.head is None) :
            return "Linked list is empty!"
        res = "Head"
        node = self.head

        while(node is not None) :
            res += " → " + str(node.data)
            node = node.next
        return res
    
    def __contains__(self, target) :
        if(self.head is None) :
            return False
        
        node = self.head
        while(node is not None) :
            if(node.data == target) :
                return True
            node = node.next

        return False
    
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


    def popleft(self) :
        if(self.head is None) :
            return None
        node = self.head                        # 임시 노드 생성 후, head를 저장
        self.head = self.head.next              # 현재 head를 다음 노드의 헤드로 이동
        self.length -= 1
        return node.data


    def pop(self) :
        if(self.head is None) :
            return None
        node = self.head                        # 임시 노드 생성 후, head를 저장
        while(node.next is not None) :
            prev = node
            node = node.next
            
        if(node == self.head) :                 # Linked list가 비었을 경우(노드가 없을 때)
            self.head = None
        else :
            prev.next = None
        self.length -= 1
        return node.data



if __name__ == "__main__" :             # 프로그램을 직접 실행 했을 경우 여기 부터 실행
    import random

    data = list(range(15, 20))
    random.shuffle(data)

    my_list = LinkedList()
    for i in data :
        my_list.append(i)
    print(my_list)
    print()

    for _ in range(4) :
        i = random.randint(5, 25)
        if(i in my_list) :
            print("%d는(은) 연결 리스트에 있습니다." % i)
        else :
            print("%d는(은) 연결 리스트에 없습니다." % i)
    print()

    for _ in range(len(my_list)) :
        print("%s를(을) 꺼낸 후: 길이 = %s, %s" % (my_list.pop(), len(my_list), my_list))
    print("연결 리스트가 비었을 때 꺼낸 값은 %s" % my_list.pop())