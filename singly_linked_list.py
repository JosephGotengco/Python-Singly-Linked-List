class Node:
    """
    class implementation for a singly linked list node

    Args:
        data: node data
        nextNode: the next node
    """

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, nextNode):
        self.nextNode = nextNode

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    """
    class implementation for a singly linked list node

    Args:
        data: node data
        nextNode: the next node
    """

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.nextNode
        return '[' + ','.join(nodes) + ']'

    def getSize(self):
        return self.size

    def prepend(self, data):
        self.head = Node(data, self.head)

    def append(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def remove(self, key):
        curr = self.head
        prev = None
        if curr:
            while curr and curr.data != key:
                prev = curr
                curr = curr.nextNode
            if prev is None:
                self.head = curr.nextNode
            elif curr:
                prev.nextNode = curr.nextNode
                curr.nextNode = None
