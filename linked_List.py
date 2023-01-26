class Node:
    '''
    This is node class that contains the class constructor for the the data in the node object
    '''
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return "{} {}".format(self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print (self):
        if self.head is None:
            print ('The linked list is empty...')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print (llstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    def insert_values (self, datalist):
        for data in datalist:
            self.insert_at_end (data)

    def get_length (self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter
    def remove_at (self, index):
        self.index = index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
        



if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_begining (4)
    ll.insert_at_end(99)
    ll.print()
    print ('The length of the linkedlist is {}'.format(ll.get_length()))

    llstrings = LinkedList()
    llstrings.insert_values (["James", "John", "Bakari"])
    llstrings.print()
    print ("The length of the linkedlist is ", llstrings.get_length())



