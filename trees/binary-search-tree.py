#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

# TODO: delete


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


# In-Order Tree Walk
def in_order_tree_walk(node):
    if node.left_child:
        in_order_tree_walk(node.left_child)
    print node.value,
    if node.right_child:
        in_order_tree_walk(node.right_child)


# Pre-Order Tree Walk (i.e., Deep-first Search - DFS)
def pre_order_tree_walk(node):
    print node.value,
    if node.left_child:
        in_order_tree_walk(node.left_child)
    if node.right_child:
        in_order_tree_walk(node.right_child)


# Post-Order Tree Walk
def post_order_tree_walk(node):
    if node:
        post_order_tree_walk(node.left_child)
        post_order_tree_walk(node.right_child)
        print node.value,


# Maximum element in the Tree
def max_node(node):
    while node.right_child:
        node = node.right_child
    return node.value


# Minimum element in the Tree
def min_node(node):
    while node.left_child:
        node = node.left_child
    return node.value


# Tree-Search
def search(node, k):
    if k == node.value:
        return node
    elif k < node.value:
        if node.left_child:
            return search(node.left_child, k)
    else:
        if node.right_child:
            return search(node.right_child, k)


# Breadth-first Search - BFS
def print_bfs(root):
    this_level = [root]
    while this_level:
        next_level = list()
        for n in this_level:
            print n.value,
            if n.left_child:
                next_level.append(n.left_child)
            if n.right_child:
                next_level.append(n.right_child)
        this_level = next_level
        print


# Validate BST
def in_order_traversal_validation(node, previous):
    """
    While doing In-Order traversal, we can keep track of previously
    visited node. If the value of the currently visited node is less than
    the previous value, then tree is not BST.
    """

    if node.left_child:
        in_order_traversal_validation(node.left_child, node)

    if previous:
        print node.value, previous.value
        if node.value < previous.value:
            return False
        else:
            return True

    if node.right_child:
        in_order_traversal_validation(node, node.right_child)


# Lowest Common Ancestor
def lowest_common_ancestor(root, n1, n2):
    """
    Method 1 (By Storing root to n1 and root to n2 paths):
    Following is simple O(n) algorithm to find LCA of n1 and n2.
    1) Find path from root to n1 and store it in a vector or array.
    2) Find path from root to n2 and store it in another vector or array.
    3) Traverse both paths till the values in arrays are same.
    Return the common element just before the mismatch.
    """
    p1 = []
    p2 = []
    find_path(root, n1, p1)
    find_path(root, n2, p2)
    print p1
    print p2
    if n1 in p2:
        return n1
    if n2 in p1:
        return n2
    x = -1
    y = -1
    last_equal = -1
    while x == y:
        if len(p1) == 1:
            return p1[0]
        elif len(p2) == 1:
            return p2[0]
        else:
            last_equal = x
            x = p1.pop(0)
            y = p2.pop(0)
    return last_equal


# Find path between a node value
def find_path(node, k, path):
    if k == node.value:
        return path
    elif k < node.value:
        path.append(node.value)
        find_path(node.left_child, k, path)
    else:
        path.append(node.value)
        find_path(node.right_child, k, path)


# Lowest Common Ancestor: simpler and recursive version
def lca(root, n1, n2):
    """
    We can solve this problem using BST properties. We can recursively
    traverse the BST from root. The main idea of the solution is,
    while traversing from top to bottom, the first node n we encounter with
    value between n1 and n2, i.e., n1 < n < n2 or same as one of the n1 or n2,
    is LCA of n1 and n2 (assuming that n1 < n2).

    So just recursively traverse the BST in, if node’s value is greater
    than both n1 and n2 then our LCA lies in left side of the node,
    if it’s is smaller than both n1 and n2, then LCA lies on right side.
    Otherwise root is LCA (assuming that both n1 and n2 are present in BST)
    """
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA lies on the left
    if root.value > n1 and root.value > n2:
        return lca(root.left_child, n1, n2)

    # If both n1 and n2 are greater than root, then LCA on the right
    if root.value < n1 and root.value < n2:
        return lca(root.right_child, n1, n2)

    return root


def main():
    arr = [3, 1, 6, 4, 7, 10, 14, 13]
    root = Node(8)
    for i in arr:
        root.insert(i)

    print "lca(6,3):", lca(root, 6, 3)
    print "lca(6,14):", lca(6, 14)

    x = lowest_common_ancestor(root, 4, 13)
    print "lca(4,13):", x

    print lca(root, 10, 8).value
    x = lowest_common_ancestor(root, 4, 1)
    print "lca(4,1):", x
    print lca(root, 4, 1).value

    x = lowest_common_ancestor(root, 4, 3)
    print "lca(4,3):", x
    print lca(root, 4, 3).value

if __name__ == "__main__":
    main()
