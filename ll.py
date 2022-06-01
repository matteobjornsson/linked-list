class Node:
    def __init__(self, data, successor):
        self.data = data
        self.succ = successor

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.string = "None"

    def add(self, data):
        self.head = Node(data, self.head)

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += str(current.data) + " -> "
            current = current.succ
        string += "None"
        return string


def reverse_linked_list(lst: LinkedList) -> LinkedList:
    reversed_list = LinkedList()
    if lst.head is None:
        # handle empty list case
        return reversed_list
    current = lst.head
    while current is not None:
        reversed_list.add(current.data)
        current = current.succ
    return reversed_list
