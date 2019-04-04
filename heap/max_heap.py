class Node:
    def __init__(self, value):
        self.value = value



class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        newNode = Node(value)
        if len(self.storage) == 0:
            self.storage[0] = newNode
        else:
            self.storage.append(newNode)
            self._bubble_up(len(self.storage)-1)


    def delete(self):
        if len(self.storage) == 1:
            return self.storage.pop()
        else:
            firstNode = self.storage.pop(0)
            lastNode = self.storage.pop(len(self.storage)-1)
            self.storage[0] = lastNode
            self._sift_down(0)
            return firstNode

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        

    def _sift_down(self, index):
        pass
