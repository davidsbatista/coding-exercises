"""
Given a tree string expression in balanced parenthesis format:

(A(B(C)(D))(E)(F))

               A
             / | \
            B  E  F
           / \
          C   D
          
The function is to return the root of the tree you build, and if you can please print the tree with indentations like above.

http://stackoverflow.com/questions/2241513/java-printing-a-binary-tree-using-level-order-in-a-specific-format

You can print in the simplified format.
        A
    B   E  F
   C  D
"""


class Node:

    def __init__(self, element_):
        self.child = []
        self.parent = None
        self.element = element_


def parse_tree(tree):
    #TODO: check if tree string is valid
    root = Node(tree[1])
    stack = [root]
    opened = 1

    for w in range(2, len(tree)):
        #print "w:", tree[w]
        if tree[w] == '(':
            """
            print "entrei 1"
            print "opened", opened
            print stack
            """
            opened += 1

        elif opened > 1 and tree[w] == ')':
            """
            print "entrei 2"
            print stack
            print "opened", opened
            """
            child = stack.pop()
            parent = stack.pop()
            parent.child.append(child)
            stack.append(parent)
            opened -= 1
            #print "opened", opened

        else:
            """
            print "entrei 3"
            print "opened", opened
            """
            stack.append(Node(tree[w]))

    return root


def print_tree(node):
    if node.child is None:
        print node.element
        print "\n"
    else:
        for n in node.child:
            print n.element
            print_tree(node.child)


def main():
    #tree = "(A(B(C)(D))(E)(F))"
    tree = "(A(B(C))"
    root = parse_tree(tree)

    #print_tree(root)
    print root.element
    print len(root.child)
    for e in root.child:
        print e.element
        print len(e.child)



if __name__ == "__main__":
    main()