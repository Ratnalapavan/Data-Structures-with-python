class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr
    
    def traverse(self):
        if self.head == None:
            print("Double Linked List is empty")
        else:
            itr= self.head
            while itr != None:
                print(itr.data,end=" -> ")
                itr = itr.next

    def insert(self,data,pre_val):
        if self.head == None:
            print("Double Linked List is empty")
            return
        if pre_val == None:
            print("Please provide a value after which insertion should happen")
            return
        new_node = Node(data)
        itr = self.head
        while itr.data != pre_val:
            itr = itr.next
        new_node.prev = itr
        new_node.next = itr.next
        itr.next = new_node

    def remove(self,del_data):
        if self.head == None:
            print("Double Linked List is empty")
            return
        itr = self.head
        if itr.data == del_data:
            self.head = itr.next
            return
        while itr.data != del_data:
            pre_node = itr
            itr = itr.next
        pre_node.next = itr.next
        if itr.next != None: # condition for last node 
            itr.next.prev = pre_node


if __name__ == "__main__":
    dl = DoubleLinkedList()
    # dl.head = Node(11)
    # n2 = Node(12)
    # n3 = Node(13)

    # dl.head.prev = None
    # dl.head.next = n2
    # n2.prev = dl.head
    # n2.next = n3
    # n3.prev = n2
    # n3.next = None

    dl.append(11)
    dl.append(12)
    dl.append(15)
    print("\nData before insertion")
    dl.traverse()
    dl.insert(14,12)
    print("\ndata after insertion")
    dl.traverse()
    print("\nremove 14 from DLL")
    dl.remove(14)
    print("\ndata after removal")
    dl.traverse()
    