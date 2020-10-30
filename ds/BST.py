#BST
class Node:
    def __init__(self,ele):
        self.left = None
        self.data = ele
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, prev, curr, ele):
        if self.root == None:
            self.root = Node(ele)
            return
        else:
            if curr == None:
                if prev.data < ele:
                    prev.right = Node(ele)
                if prev.data >= ele:
                    prev.left = Node(ele)
                return
            if curr.data < ele:
                self.insert(curr, curr.right, ele)
            else:
                self.insert(curr, curr.left, ele)

    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def inorder_array(self, node, sol):
        if node == None:
            return
        else:
            self.inorder(node.left, sol)
            sol.append(node.data)
            self.inorder(node.right, sol)

    def preorder(self, node):
        if node == None:
            return
        else:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def levelorder(self,node):
        values = []
        if node is None:
            return
        else:
            return node.data

    def helper(self,node):
        sol = []
        sol.append(self.levelorder(node))
        return sol





if __name__ == '__main__':
    bst = BST()
    elements = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for i in elements:
        bst.insert(bst.root, bst.root, i)
    bst.preorder(bst.root)
    print('-----')
    bst.inorder(bst.root)
    print (bst.helper(bst.root))