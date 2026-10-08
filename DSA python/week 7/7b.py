class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def create_tree(self):
        self.root=Node('A')
        self.root.left=Node('B')
        self.root.right=Node('C')
        self.root.left.left=Node('D')
        self.root.left.right=Node('E')
        self.root.right.right=Node('F')

    def preorder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")

    def level_order(self):
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            node=queue.pop(0)
            print(node.data,end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

tree=BinaryTree()
tree.create_tree()

print("Preorder: ",end="")
tree.preorder(tree.root)

print("\nInorder: ",end="")
tree.inorder(tree.root)

print("\nPostorder: ",end="")
tree.postorder(tree.root)

print("\nLevel-order: ",end="")
tree.level_order()
