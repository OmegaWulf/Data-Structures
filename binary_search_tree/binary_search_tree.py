class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        newNode = BinarySearchTree(value)

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
        while self.right is not None:
            

    def for_each(self, cb):
        pass