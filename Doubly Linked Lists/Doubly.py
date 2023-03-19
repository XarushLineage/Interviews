class Node:
    """
    A node in the doubly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

"""
The DoublyLinkedList class is the implementation of the doubly linked list and has an empty head and tail when initialized. The is_empty() function returns True if the doubly linked list is empty, False otherwise. The insert_at_head(data) function inserts a new node with data at the head of the doubly linked list. The insert_at_tail(data) function inserts a new node with data at the tail of the doubly linked list.

The delete_at_head() function removes the node at the head of the doubly linked list and returns its data. If the list is empty, it raises an exception. The delete_at_tail() function removes the node at the tail of the doubly linked list and returns its data. If the list is empty, it raises an exception

All of these functions operate on the doubly linked list by manipulating the prev and next pointers of the nodes, updating the head and tail pointers when necessary, and returning the data contained in the removed nodes.
"""
        
class DoublyLinkedList:
    """
    A doubly linked list implementation.
    """
    def __init__(self):
        """
        Initializes the doubly linked list with an empty head and tail.
        """
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Returns True if the doubly linked list is empty, False otherwise.
        """
        return self.head is None

    def insert_at_head(self, data):
        """
        Inserts a node at the head of the doubly linked list.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        """
        Inserts a node at the tail of the doubly linked list.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_head(self):
        """
        Removes the node at the head of the doubly linked list.
        """
        if self.is_empty():
            raise Exception('List is empty')

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return data

    def delete_at_tail(self):
        """
        Removes the node at the tail of the doubly linked list.
        """
        if self.is_empty():
            raise Exception('List is empty')

        data = self.tail.data
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return data
