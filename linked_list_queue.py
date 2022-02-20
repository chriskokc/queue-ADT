# queue ADT
# Linked list implementation
# struct queue{
#     node* front;
#     node* back;
# }

from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def peek(self):
        return self.front.value

    def is_empty(self):
        return self.front is None

    def enqueue(self, x):
        # create a new node
        new_node = Node(value=x)
        # if the queue is empty
        if self.is_empty():
            self.front = new_node
        else:
            # if the queue is not empty
            # connect the node to the queue
            self.back.next = new_node
        # make the new node as the back
        self.back = new_node

    def dequeue(self):
        # if the queue is empty
        # handle the underflow error
        if self.is_empty():
            print("The queue is empty")
        # if the queue is not empty
        else:
            # First In First Out
            # return the dequeued value
            x = self.front.value
            # make the second node as the new head
            self.front = self.front.next
            # return the value
            return x


