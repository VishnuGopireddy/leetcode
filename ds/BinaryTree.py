class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if self.root is None:
            self.root = Node(val)
        elif node.left is None:
            node.left = Node(val)
        elif node.right is None and node.left is not None:
            node.right = Node(val)
        elif node.left and node.right:
            self.insert(node.left, val)


    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node == None:
            return
        else:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

if __name__ == '__main__':
    btree = BinaryTree()
    elems = [1,2,3,4,5,6]
    for i in elems:
        btree.insert(btree.root,i)
    btree.inorder(btree.root)
    print('')
    btree.preorder(btree.root)