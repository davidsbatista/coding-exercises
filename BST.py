#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"


class Node:
    def __init__(self, _value):
        self.left_child = None
        self.right_child = None
        self.value = _value

    def __str__(self):
        return self.value

    def insert(self, value):
        if self.value is not None:
            if value > self.value:
                if self.right_child is None:
                    self.right_child = Node(value)
                else:
                    self.right_child.insert(value)
            elif value < self.value:
                if self.left_child is None:
                    self.left_child = Node(value)
                else:
                    self.left_child.insert(value)
        else:
            self.value = value

    def in_order_tree_walk(self):
        if self.left_child is not None:
            self.left_child.in_order_tree_walk()
        print self.value
        if self.right_child is not None:
            self.right_child.in_order_tree_walk()

    @staticmethod
    def max(node):
        while node.right_child is not None:
            node = node.right_child
        return node.value

    @staticmethod
    def min(node):
        while node.left_child is not None:
            node = node.left_child
        return node.value

    #TODO: bugged
    def is_valid_bst(self, min, max):
        if (min < self.value < max and
            self.is_valid_bst(self.left_child, min, self.value) and
            self.is_valid_bst(self.right_child, max, self.value)):
            return True
        else:
            return False

    #TODO: delete

    def search(self, k):
        print self.value, k
        if k == self.value:
            print "entrei"
            return self
        elif k < self.value:
            print "less", self.value
            self.left_child.search(k)
        else:
            print "bigger", self.value
            self.right_child.search(k)


def main():
    arr = [3, 1, 6, 4, 7, 10, 14, 13]
    root = Node(8)
    for i in arr:
        root.insert(i)

    #print root.is_valid_bst(sys.maxint, -sys.maxint - 1)
    print "ordered elements: "
    root.in_order_tree_walk()
    print "\n"
    x = 13
    print "is", x, "present: ", root.search(x)
    print "max:", root.max(root)
    print "min:", root.min(root)
    """
    print 'Breadth-First Traversal'
    tree.bft()
    print 'Inorder Traversal'
    tree.inorder(tree.root)
    print 'Preorder Traversal'
    tree.preorder(tree.root)
    print 'Postorder Traversal'
    tree.postorder(tree.root)

    - Binary search
    """


if __name__ == "__main__":
    main()