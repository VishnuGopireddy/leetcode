from ds.BST import BST

bst1 = BST()
elems = [3,5,1,2]

for i in elems:
    bst1.insert(bst1.root, bst1.root, i)
bst1.preorder(bst1.root)

print('')
bst2 = BST()
elems = [3,4,1,2,7]

for i in elems:
    bst2.insert(bst2.root, bst2.root, i)
bst2.preorder(bst2.root)

def merge(bst1, bst2):
    bst3 = BST()
    node1 = bst1.node
    node2 = bst2.node
    while node1 or node2:
        if node1 and node2:
            bst3.insert(bst3.root, node1.data + node2.data)
        if node1:
            bst3.insert()