class BinaryTreeArray:
    def __init__(self,size):
        self.tree=[None]*size
        self.size=size

    def set_root(self,data):
        self.tree[0]=data

    def set_left(self,parent_index,data):
        child_index=2*parent_index+1
        if child_index<self.size:
            self.tree[child_index]=data
        else:
            print("Index out of range!")

    def set_right(self,parent_index,data):
        child_index=2*parent_index+2
        if child_index<self.size:
            self.tree[child_index]=data
        else:
            print("Index out of range!")

    def preorder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        print(self.tree[index],end=" ")
        self.preorder(2*index+1)
        self.preorder(2*index+2)

    def inorder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        self.inorder(2*index+1)
        print(self.tree[index],end=" ")
        self.inorder(2*index+2)

    def postorder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        self.postorder(2*index+1)
        self.postorder(2*index+2)
        print(self.tree[index],end=" ")

    def level_order(self):
        for value in self.tree:
            if value is not None:
                print(value,end=" ")

    def display(self):
        print("\nArray Representation:")
        for i in range(self.size):
            print(f"Index {i}: {self.tree[i]}")

tree=BinaryTreeArray(7)
tree.set_root('A')
tree.set_left(0,'B')
tree.set_right(0,'C')
tree.set_left(1,'D')
tree.set_right(1,'E')
tree.set_right(2,'F')
tree.display()
print("\nPreorder: ",end="")
tree.preorder()
print("\nInorder: ",end="")
tree.inorder()
print("\nPostorder: ",end="")
tree.postorder()
print("\nLevel-order: ",end="")
tree.level_order()
