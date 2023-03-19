class Queue:
    def __init__(self):
        """
        Initializes the queue with an empty list of items.
        """
        self.items = []

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the first item from the queue.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items.pop(0)

    def size(self):
        """
        Returns the number of items in the queue.
        """
        return len(self.items)
