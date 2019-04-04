class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


    def contains(self, target):
        if target < self.value:
            if self.value.left is None:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if self.value.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):

        if self.right is None:
            return self.value

        rightNode = self.right
        while rightNode.right is not None:
            rightNode = rightNode.right
        return rightNode.value

    def for_each(self, cb):

        if self is not None:
            # perform cb
            if self.left is not None:
                self.for_each(self.left, cb)
            if self.right is not None:
                self.for_each(self.right, cb)




tree = BinarySearchTree(10)
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(12)

print(tree.get_max())