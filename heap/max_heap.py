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
            self.storage.insert(0, lastNode)
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
        node = self.storage[index]
        nodeIndex = self.storage.index(node)

        left = (nodeIndex * 2) + 1
        right = (nodeIndex * 2) + 2
        childMax = max(self.storage[left].value, self.storage[right].value)
        greaterChild = self.findGreaterChild(left, right)


        while node.value < childMax:
            # node is less than one of it's children, swap
            self.storage[nodeIndex], self.storage[greaterChild] = self.storage[greaterChild], self.storage[nodeIndex]
            node = self.storage[greaterChild]
            nodeIndex = greaterChild
            left = greaterChild * 2 + 1
            right = greaterChild * 2 + 2

            childMax = max(self.storage[left].value, self.storage[right].value)
            greaterChild = self.findGreaterChild(left, right)

    def findGreaterChild(self, left, right):
        greater = right
        if self.storage[left].value > self.storage[right].value:
            greater = left
        return greater


heap = Heap()
heap.insert(10)
heap.insert(3)
heap.insert(5)
heap.insert(7)
heap.insert(12)
heap.insert(155)
heap.insert(2)
heap.insert(19)

heap.print()
print(f'New\n')

heap.delete()
heap.print()
