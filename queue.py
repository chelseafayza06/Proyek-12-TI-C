class QueueNode:

    def __init__(self, data):

        self.data = data
        self.next = None


class Queue:

    def __init__(self):

        self.front = None
        self.rear = None


    def enqueue(self, data):

        node_baru = QueueNode(data)

        if self.rear is None:

            self.front = node_baru
            self.rear = node_baru

        else:

            self.rear.next = node_baru
            self.rear = node_baru


    def dequeue(self):

        if self.front is None:

            return None

        data = self.front.data

        self.front = self.front.next

        if self.front is None:

            self.rear = None

        return data