# struct Node{
#   int value;
#   node* next;
# }
#


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

