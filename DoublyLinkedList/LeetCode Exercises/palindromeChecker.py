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
#     If the length of the list is less than or equal to 1, 
#     then the list is a palindrome by definition, so the method returns True.
#     The method initializes two pointers, forward_node and backward_node, 
#     that point to the head and tail of the list, respectively. 
#     The method then iterates over half of the list,
#     comparing the values of the nodes at each end of the list to see if they are the same.
#     If the values of the nodes do not match, 
#     the method returns False, indicating that the list is not a palindrome. 
#     If all of the values match, the method returns True, indicating that the list is a palindrome.

    def is_palindrome(self):
        
        
        if self.length <= 1:
            return True
            
        temp = self.head
        temp2 = self.tail
        for i in range(self.length//2):
            if temp.value != temp2.value:
                return False
            temp = temp.next
            temp2 = temp2.prev
        return True
            
                    
                    
        




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""