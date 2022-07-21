class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head == None:
            print("Double Linked List is empty")
        else:
            itr= self.head
            while True:
                print(itr.prev,itr,itr.next,itr.data)
                itr = itr.next
                if itr == self.head:
                    break
    
    def push(self,node_obj):
            self.head = node_obj
            self.head.prev = None
            self.head.next = self.head

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.push(new_node)
        else:
            itr = self.head
            while True:
                if itr.next == self.head:
                    itr.next = new_node
                    new_node.next = self.head
                    new_node.prev = itr
                    break
                itr = itr.next

    def insert_after(self,data,after_data):
        new_node = Node(data)
        itr = self.head
        if False:#itr.data == after_data:
            self.head = itr.next
            self.head.prev = None
            return
        else:
            while itr.data != after_data:
                itr = itr.next
            # prev_node.next = itr.next
            # itr.next.prev = itr.prev
            new_node.next = itr.next
            itr.next = new_node
            new_node.prev = itr
            
    def remove(self,remove_data):
        itr = self.head
        if itr.data == after_data:
            self.head = itr.next
            self.head.

    

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
    # n3.next = dl.head

    dl.append(11)
    dl.append(12)
    dl.append(15)
    print("\nData before insertion")
    dl.traverse()
    dl.insert_after(14,11)
    print("\ndata after insertion")
    dl.traverse()
    # print("\nremove 14 from DLL")
    # dl.remove(14)
    # print("\ndata after removal")
    # dl.traverse()
    