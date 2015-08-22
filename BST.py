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

    #TODO: delete

    #TODO: return Node where value occurs
    def search(self, k):
        if k == self.value:
            return hex(id(self))
        elif k < self.value:
            self.left_child.search(k)
        else:

            self.right_child.search(k)


def max_node(node):
    while node.right_child is not None:
        node = node.right_child
    return node.value


def min_node(node):
    while node.left_child is not None:
        node = node.left_child
    return node.value


# Pre-order or deep-first-search
def print_dfs(node):
    if node is not None:
        print node.value,
        print_dfs(node.left_child)
        print_dfs(node.right_child)


# in-order
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
# using a queue (FIFO)
def print_bfs(node):
    l = [node]
    while len(l) > 0:
        v = l.pop()
        print v.value,
        if v.left_child is not None:
            l.insert(0, v.left_child)
        if v.right_child is not None:
            l.insert(0, v.right_child)


#TODO: print a newline at each level
def print_bfs_level(node):
    l = [node]
    while len(l) > 0:
        v = l.pop()
        print v.value,
        if v.left_child is not None:
            l.insert(0, v.left_child)
        if v.right_child is not None:
            l.insert(0, v.right_child)


def is_valid_bst(node, stack):
    """
    The left subtree of a node contains only nodes with keys less than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    Both the left and right subtrees must also be binary search trees.

    Method 1:
        - in-order transversal and check in-line if array is sorted
    """
    if node.left_child is not None:
        is_valid_bst(node.left_child, stack)
    stack.append(node.value)
    if node.right_child is not None:
        is_valid_bst(node.right_child, stack)
    return stack


def is_valid_bst2(node, previous):
    #TODO:
    """
    While doing In-Order traversal, we can keep track of previously visited node.
    If the value of the currently visited node is less than the previous value,
    then tree is not BST.
    """
    pass


def find_path(node, k, path):
    if k == node.value:
        return path
    elif k < node.value:
        path.append(node.value)
        find_path(node.left_child, k, path)
    else:
        path.append(node.value)
        find_path(node.right_child, k, path)


def lowest_common_ancestor(root, n1, n2):
    """
    Method 1 (By Storing root to n1 and root to n2 paths):
    Following is simple O(n) algorithm to find LCA of n1 and n2.
    1) Find path from root to n1 and store it in a vector or array.
    2) Find path from root to n2 and store it in another vector or array.
    3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.
    """
    p1 = []
    p2 = []
    find_path(root, n1, p1)
    find_path(root, n2, p2)
    print n1, p1
    print n2, p2
    x = -1
    y = -1
    #TODO: check if n1 in p2 or if n2 in p1
    while x == y and len(p1) > 0 and len(p2) > 0:
        x = p1.pop(0)
        y = p2.pop(0)
        lca = x
    print lca


def main():
    arr = [3, 1, 6, 4, 7, 10, 14, 13]
    root = Node(8)
    for i in arr:
        root.insert(i)

    lowest_common_ancestor(root, 4, 3)

    """
    print "\nmin:", min_node(root)
    print "\nmax:", max_node(root)

    stack = is_valid_bst(root, [])
    for x in range(1, len(stack)):
        if stack[x-1] > stack[x]:
            print False
            break
    print "\nis valid BST:", stack
    """

    #is_valid_bst2(root, -1)

    """
    # inorder (for binary trees only): visit left subtree, node, right subtree.
    print "\nInorder Traversal:"
    in_order_tree_walk(root)

    #preorder: visit each node before its children.
    print "\n\nPreorder Traversal (Depth-first):"
    print_dfs(root)

    #postorder: visit each node after its children.
    print "\n\nPostorder Traversal:"
    post_order(root)

    print '\n\nBreadth-First Traversal'
    print_bfs(root)

    #node = root.search(x)
    """

if __name__ == "__main__":
    main()