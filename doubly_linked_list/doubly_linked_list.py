"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode


    def remove_from_head(self):
        self.head = self.head.next


    def add_to_tail(self, value):
        newNode = ListNode(value)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def remove_from_tail(self):
        self.tail = self.tail.prev

    def move_to_front(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head
        node.prev = None
        self.head = node


    def move_to_end(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = self.tail
        self.tail = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get_max(self):
        if self.head is None:
            return 0
        count = 1
        currentNode = self.head

        while currentNode.next is not None:
            count += 1
            currentNode = currentNode.next

        return count