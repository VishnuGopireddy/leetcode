# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Inorder:
    def __init__(self):
        self.stack = []

    def inorder(self, root):
        if root == None:
            return self.stack
        else:
            self.inorder(root.left)
            self.stack.append(root.val)
            print(root.val)
            self.inorder(root.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree1 = Inorder()
        tree2 = Inorder()
        tree1.inorder(p)
        tree2.inorder(q)

        #        print(tree1.stack)
        #        print(tree2.stack)
        if tree1 == tree2:
            return True
        else:
            return False

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            p = stringToTreeNode(line);
            line = next(lines)
            q = stringToTreeNode(line);

            ret = Solution().isSameTree(p, q)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()