"""
Queue:

A queue is a linear data structure, a sequential collection. The entities in the collection
are kept in order and the principal operations on the collections are
:the addition of entities to the rear terminal position, known as enqueue;
:removal of entities from the front terminal position, known as dequeue.
This makes the queue a First-in-First-out (FIFO) data structure. In FIFO data structure,
the first element added to the queue will be the first one to be removed.
"""

from collections import deque

class Queue:

    def __init__(self):
        self._queue = deque([])

    def add(self, value):
        """
        Add element as the last element in the Queue.
        Worst Case Complexity:  O(1)
        :param value: the item to be added in the queue
        """

        self._queue.append(value)
    
    def remove(self):
        """
        Remove element from the front of the Queue and return its value
        Worst Case Complexity: O(1)
        """
        return self._queue.popleft()

    def is_empty(self):
        """
        Returns a boolean indicating if the Queue is empty.
        Worst Case Complexity: O(1)
        """
        return not len(self._queue)

    def size(self):
        """
        Returns size of the Queue
        Worst Case Complexity: O(1)
        """
        return len(self._queue)

