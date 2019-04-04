import math

class Node:
    def __init__(self, value):
        self.value = value


class Heap:
    def __init__(self):
        self.storage = []

    def print(self):
        for x in range(len(self.storage)):
            print(self.storage[x].value)


    def insert(self, value):
        newNode = Node(value)
        if len(self.storage) == 0:
            self.storage.append(newNode)
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
        node = self.storage[index]

        nodeIndex = self.storage.index(node)

        while self.storage[int((nodeIndex-1)/2)].value < node.value:
            # parent value is less than our node value
            #swap nodeIndex and nodeIndex parent
            self.storage[nodeIndex], self.storage[int((nodeIndex-1)/2)] = self.storage[int((nodeIndex-1)/2)], self.storage[nodeIndex]
            nodeIndex = self.storage.index(node)



    def _sift_down(self, index):
        pass


heap = Heap()
heap.insert(10)
heap.insert(3)
heap.insert(5)
heap.insert(7)
heap.insert(122)


heap.print()