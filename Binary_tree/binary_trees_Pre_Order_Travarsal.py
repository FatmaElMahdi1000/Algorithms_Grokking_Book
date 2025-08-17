class node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Binary_tree:
    def __init__(self, root):
        self.root = node(root)

    def pre_order(self, root, traversal): #traversing tree 
        if root is None:
            return traversal
        else:
            traversal = traversal + str(root.value) + "-"
            traversal = self.pre_order(root.left, traversal)
            traversal = self.pre_order(root.right, traversal)
            return traversal
            
tree = Binary_tree(3)
tree.root.left = node(5)
tree.root.right = node(7)
tree.root.right.right = node(18)
tree.root.right.left = node(2)
result = tree.pre_order(tree.root, "pre-order: ")
print(result[:-1])


""" if root is None:
    return traversal
we’re not saying "root is always None".
We’re just saying: when recursion reaches past a leaf node, root becomes None.

How it works step by step
Take this small tree:

markdown
Copy
Edit
    3
   / \
  5   7
Start at root (3):

root = Node(3), not None.

Add "3-" to traversal.

Recurse left.

Go left (5):

root = Node(5), not None.

Add "5-".

Recurse left again.

Left of 5:

root is None (because 5 has no left child).

Here the if root is None: return traversal line prevents a crash, and just gives back the traversal so far.

It then goes right of 5 (also None) → same thing happens.

Then recursion continues on the right child (7) … etc."""