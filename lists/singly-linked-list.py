class Node:

    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node

    def insert(self, element):
        if self.next_node is None:
            n = Node(element)
            self.next_node = n
        else:
            self.next_node.insert(element)


def reverse(node):

    previous = None

    while node.next_node:
        tmp = node.next_node
        node.next_node = previous
        previous = node
        node = node.next_node

    return node


def print_list(first):
    if first:
        print first.element,
        print_list(first.next_node)


def main():

    arr = [5, 7, 9]
    head = Node(3)
    for i in arr:
        head.insert(i)

    print_list(head)

    reversed_list = reverse(head)

    print_list(reversed_list)

if __name__ == '__main__':
    main()


"""
class Node:
    def __init__(element, next_node=None):
        self.element = element
        self.next_node = next_node


# 3, 5, 7, 9

def reverse(node):
    previous = None

    while node.next_node != None:
        tmp = node.next_node
        node.next_node = previous
        previous = node
        node = node.next_node

    return node
"""