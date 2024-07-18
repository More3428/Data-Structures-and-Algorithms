

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    ## Code Explanation ##

# The method swaps the values of the first and last nodes of a linked list.
# The first if statement checks if the linked list is empty or has only one node. 
# If either of these conditions is true, then the method returns without doing anything.
# If the linked list has at least two nodes, then the method swaps the values of the first and last nodes using a tuple assignment. 
# The tuple (self.tail.value, self.head.value) represents the values of the last and first nodes, respectively. 
# The values are swapped by setting the tuple to (self.head.value, self.tail.value).
# After the values are swapped, the method exits. 
# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

## Code Explanation ## 

    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value
            
    
    
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""