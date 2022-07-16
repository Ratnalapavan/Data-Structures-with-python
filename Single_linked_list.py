import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SLlist:
    def __init__(self):
        self.head = None

    def add_at_end(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = new_node

    def add_at_begining(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def add_after(self,data,after_data):
        if self.head == None:
            self.head = Node(data)
        elif after_data == None:
            print("Please provide data after which insertion should happen")
        else:
            new_node = Node(data)
            itr = self.head
            while itr.data != after_data:
                itr = itr.next
                if itr == None:
                    print("Please enter the right value in the list to insert after it")
                    return
            new_node.next = itr.next
            itr.next = new_node

    def remove_node(self,data):
        if self.head == None:
            print("Linked list is empty")
        else:
            itr = self.head
            if itr.data == data:
                self.head = itr.next
                return
            while itr.data != data:
                prev_node = itr
                itr = itr.next
                if itr == None:
                    print("Please enter the value which is present in the Linked list remove")
                    return
            prev_node.next = itr.next
            
    def traverse(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            itr = self.head
            while itr != None:
                print(itr.data,end=" -> ")
                itr = itr.next

if __name__ == "__main__":
    ll = SLlist()
    # ll.head = Node("101")
    # n2 = Node("102")
    # n3 = Node("103")

    # ll.head.next = n2
    # n2.next = n3
    ll.add_at_end(100)
    ll.add_at_end(200)
    ll.add_at_end(300)
    ll.add_at_begining(10)
    ll.add_after(111,100)
    ll.remove_node(200)
    ll.traverse()