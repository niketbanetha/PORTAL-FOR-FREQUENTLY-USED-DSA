
import streamlit as st

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1


@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class BST():
    def __init__(self):
        self.root=None


@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class BSTFunction():
    def __init__(self):
        self.output=[]

    def insertBST(self,root,data):
        self.output.append("Checking  node is empty or not")
        if root is None:
            self.output.append("Node is empty, Inserting data into node")
            return Node(data)
        else:
            self.output.append("Checking data {} is greater than node data {}".format(data,root.data))
            if data>root.data:
                self.output.append("Moving to right side of tree")
                root.right = self.insertBST(root.right,data)
            else:
                self.output.append("Moving to left side of tree")
                root.left = self.insertBST(root.left,data)
            return root
    

    def searchBST(self,root,data):
        if root:
            self.output.append("Comapring search data and node data -> [{} == {} => {}]".format(data,root.data,data==root.data))
            if data==root.data:
                self.output.append("Data is present in tree")
                return True
            self.output.append("Checking search data {} is greater than node data {}".format(data,root.data))
            if data > root.data:
                self.output.append("Moving to right side of tree")
                return self.searchBST(root.right,data)
            else:
                self.output.append("Moving to left side of tree")
                return self.searchBST(root.left,data)
        self.output.append("Data not present in Tree")
        return False

    def minValueNode(self,root):
        temp = root
        while(temp.left is not None):
            temp = temp.left
        return temp

    def deleteBST(self,root,data):
        self.output.append("Checking whether node is empty or not")
        if root is None:
            self.output.append("Node is empty")
            return root
        self.output.append("Checking data {} is greater than node data {}".format(data,root.data))
        if data < root.data:
            self.output.append("Moving to left part of tree")
            root.left = self.deleteBST(root.left, data)

        elif(data > root.data):
            self.output.append("Moving to right part of tree")
            root.right = self.deleteBST(root.right, data)

        else:
            self.output.append("Delete data is found")
            self.output.append("Checking wether root left or right node is empty or not")
            if root.left is None:
                self.output.append("Left Node is empty, So replacing current node with right node")
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                self.output.append("Right Node is empty, So replacing current node with left node")
                temp = root.left
                root = None
                return temp

            self.output.append("Both left and right node is not empty, so looking for inorder successor of node")
            temp = self.minValueNode(root.right)
            self.output.append("Copying content of inorder successor to current node")
            root.data = temp.data
            self.output.append("deleting inorder successor")
            root.right = self.deleteBST(root.right, temp.data)
        return root

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class AVL():
    def __init__(self):
        self.root=None

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class AVLFunction():
    def __init__(self):
        self.output=[]
    
    def insertAVL(self, root, data):

        self.output.append("Checking wether node is empty or not")
        if not root:
            self.output.append("Node is empty, Inserting data  into Node")
            return Node(data)
        elif data < root.data:
            self.output.append("Data {} is less than node data {}".format(data,root.data))
            self.output.append("Moving to left part of data")
            root.left = self.insertAVL(root.left, data)
        else:
            self.output.append("Data {} is greater than node data {}".format(data,root.data))
            self.output.append("Moving to right part of data")
            root.right = self.insertAVL(root.right, data)

        self.output.append("Updating the height of the ancestor node")
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))

        self.output.append("Getting balance factor of node")
        balance = self.getBalance(root)

        if balance > 1 and data < root.left.data:
            self.output.append("Performing Left Left rotation")
            return self.rightRotate(root)

        if balance < -1 and data > root.right.data:
            self.output.append("Performing Right Right rotation")
            return self.leftRotate(root)

        if balance > 1 and data > root.left.data:
            self.output.append("Performing Left Right rotation")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and data < root.right.data:
            self.output.append("Performing Right Left rotation")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):

        y = z.right
        T2 = y.left
 
        self.output.append("Performing rotation")
        y.left = z
        z.right = T2

        self.output.append("Updating the height")
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))

        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right

        self.output.append("Performing rotation")
        y.right = z
        z.left = T3

        self.output.append("Updating the height")
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y
 
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        self.output.append("Balance of node is [height of left tree - height of right tree]-> {} - {}".format(self.getHeight(root.left),self.getHeight(root.right)))
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
  
        return self.getMinValueNode(root.left)

    def searchAVL(self,root,data):
        if root:
            self.output.append("Comapring search data and node data -> [{} == {} => {}]".format(data,root.data,data==root.data))
            if data==root.data:
                self.output.append("Data is present in tree")
                return True
            self.output.append("Checking search data {} is greater than node data {}".format(data,root.data))
            if data > root.data:
                self.output.append("Moving to right side of tree")
                return self.searchAVL(root.right,data)
            else:
                self.output.append("Moving to left side of tree")
                return self.searchAVL(root.left,data)
        self.output.append("Data not present in Tree")
        return False
    
    def deleteAVL(self, root, data):
  
        self.output.append("Checking whether node is empty or not")
        if not root:
            self.output.append("Node is empty")
            return root

        elif data < root.data:
            self.output.append("Data {} is less than node data {}".format(data,root.data))
            self.output.append("Moving to left part of data")
            root.left = self.deleteAVL(root.left, data)
  
        elif data > root.data:
            self.output.append("Data {} is greater than node data {}".format(data,root.data))
            self.output.append("Moving to right part of data")
            root.right = self.deleteAVL(root.right, data)
  
        else:
            if root.left is None:
                self.output.append("Node which is to be deleted has left node empty, Swapping current node with right node")
                temp = root.right
                root = None
                return temp
  
            elif root.right is None:
                self.output.append("Node which is to be deleted has right node empty, Swapping current node with left node")
                temp = root.left
                root = None
                return temp

            self.output.append("Both left and right node is not empty, so looking for inorder successor of node")
            temp = self.getMinValueNode(root.right)
            self.output.append("Copying content of inorder successor to current node")
            root.data = temp.data
            self.output.append("Deleting inorder successor")
            root.right = self.deleteAVL(root.right,
                                      temp.data)

        if root is None:
            return root

        self.output.append("Updating the height of the ancestor node")
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))

        self.output.append("Getting balance factor of node")
        balance = self.getBalance(root)

        
        if balance > 1 and self.getBalance(root.left) >= 0:
            self.output.append("Performing Left Left rotation")
            return self.rightRotate(root)

        
        if balance < -1 and self.getBalance(root.right) <= 0:
            self.output.append("Performing Right Right rotation")
            return self.leftRotate(root)

        
        if balance > 1 and self.getBalance(root.left) < 0:
            self.output.append("Performing Left Right rotation")
            
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        
        if balance < -1 and self.getBalance(root.right) > 0:
            self.output.append("Performing Right Left rotation")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

