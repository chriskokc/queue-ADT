# queue ADT
# Fixed array implementation
# struct queue{
#    int arr[];
#    int front;
#    int back;
#    int maxsize;
# }

class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.arr = [None for i in range(maxsize)]
        self.front = -1
        self.back = -1

    def enqueue(self, x):
        # if the queue is full
        # e.g maxsize = 10, front = 0, back = 9
        if (self.back + 1) % self.maxsize == self.front:
            print("The queue is full")
        # if the queue is not full
        # if the queue is empty, i.e front = -1, back = -1
        elif self.front == -1:
            # set both front and back index to 0
            self.front = 0
            self.back = 0
            self.arr[self.back] = x
        else:
            # e.g back = 9, maxsize = 10
            self.back = (self.back + 1) % self.maxsize
            self.arr[self.back] = x

    def dequeue(self):
        # if the queue is empty
        # e.g front = -1
        if self.front == -1:
            print("The queue is empty")
        # when there is only one element left in the queue
        # e.g front = 2, back = 2
        elif self.front == self.back:
            # reset both the front and back index
            # First In First Out
            x = self.arr[self.front]
            self.front = -1
            self.back = -1
            return x
        # if the queue is not empty
        else:
            # First In First Out
            x = self.arr[self.front]
            # e.g front = 9, maxsize = 10
            self.front = (self.front + 1) % self.maxsize
            return x

    def display(self):
        if self.front == -1:
            print("The queue is empty")
        elif self.back < self.front:
            print("The elements in the queue are: ", end=" ")
            for i in range(self.front, self.maxsize):
                print(self.arr[i], end=" ")
            for i in range(0, self.back + 1):
                print(self.arr[i], end=" ")
            print()
        else:
            # if back index is greater than front index
            print("The elements in the queue are: ", end=" ")
            for i in range(self.front, self.back + 1):
                print(self.arr[i], end=" ")
            print()

