class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def printlist(self):
        if self.head == None:
            print('List empty')
        else:
            curr = self.head
            while curr != None:
                print(curr.val,end=' ')
                curr = curr.next
            print()

if __name__ == '__main__':
    singly = LinkedList()
    ele = [1,2,3,4,5,6]
    for i in ele:
        singly.insert(i)
    singly.printlist()