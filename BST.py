#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"


class Node:
    def __init__(self, _value):
        self.left_child = None
        self.right_child = None
        self.value = _value

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

    # in-order
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

    #TODO: return Node where value occurs
    def search(self, k):
        if k == self.value:
            return hex(id(self))
        elif k < self.value:
            self.left_child.search(k)
        else:

            self.right_child.search(k)


# Pre-order or deep-first-search
def print_dfs(node):
    if node is not None:
        print node.value,
        print_dfs(node.left_child)
        print_dfs(node.right_child)


# in-order of the elements in the b-tree
def in_order_tree_walk(node):
    if node.left_child is not None:
        in_order_tree_walk(node.left_child)
    print node.value,
    if node.right_child is not None:
        in_order_tree_walk(node.right_child)


# Post-order
def post_order(node):
    if node is not None:
        post_order(node.left_child)
        post_order(node.right_child)
        print node.value,


# https://www.cs.bu.edu/teaching/c/tree/breadth-first/
#TODO: print a newline at each level
def print_bfs(node):
    l = [node]
    while len(l) > 0:
        v = l.pop()
        print v.value,
        if v.left_child is not None:
            l.insert(0, v.left_child)
        if v.right_child is not None:
            l.insert(0, v.right_child)


def main():
    arr = [3, 1, 6, 4, 7, 10, 14, 13]
    root = Node(8)
    for i in arr:
        root.insert(i)

    #print root.is_valid_bst(sys.maxint, -sys.maxint - 1)
    """
    print "ordered elements: "
    print "\n"
    x = 13
    node = root.search(x)
    print node
    print "max:", root.max(root)
    print "min:", root.min(root)
    """
    """
    preorder: visit each node before its children.
    postorder: visit each node after its children.
    inorder (for binary trees only): visit left subtree, node, right subtree.
    """

    print "in order:"
    in_order_tree_walk(root)
    print "\n\ndepth-first (pre-order):"
    print_dfs(root)
    print "\n\npost-order:"
    post_order(root)
    print '\n\nBreadth-First Traversal'
    print_bfs(root)

    """
    print 'Breadth-First Traversal'
    tree.bft()
    print 'Inorder Traversal'
    tree.inorder(tree.root)
    print 'Preorder Traversal'
    tree.preorder(tree.root)
    print 'Postorder Traversal'
    tree.postorder(tree.root)

    """


if __name__ == "__main__":
    main()