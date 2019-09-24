#https://leetcode.com/problems/same-tree/
'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Inorder:
    def __init__(self,TreeNode):
        self.stack = []
    def inorder(self,TreeNode):
        root = TreeNode
        if root == None:
            return self.stack
        else:
            self.inorder(root.left)
            self.stack.append(root.data)
            self.inorder(root.right)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree1 = Inorder(p)
        tree2 = Inorder(q)
        if tree1 == tree2:
            return True
        else:
            return False


