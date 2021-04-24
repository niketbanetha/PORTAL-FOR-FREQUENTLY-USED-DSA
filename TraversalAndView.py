from collections import defaultdict
class TraversalAndView():
    def __init__(self):
        self.output=[]

    def inOrderTraversal(self,root):
        if root:
            self.output.append("Traversing to left node of root")
            self.inOrderTraversal(root.left)
            self.output.append("Data is {}".format(root.data))
            self.output.append("Traversing to right node of root")
            self.inOrderTraversal(root.right)

    def preOrderTraversal(self,root):
        if root:
            self.output.append("Data is {}".format(root.data))
            self.output.append("Traversing to left node of root")
            self.preOrderTraversal(root.left)
            self.output.append("Traversing to right node of root")
            self.preOrderTraversal(root.right)

    def postOrderTraversal(self,root):
        if root:
            self.output.append("Traversing to left node of root")
            self.postOrderTraversal(root.left)
            self.output.append("Traversing to right node of root")
            self.postOrderTraversal(root.right)
            self.output.append("Data is {}".format(root.data))

    def _levelOrderTraversal(self,root,resultDict,level):
        if root:
            self.output.append("Insert into dictionary, key would be level {} and value would be node data {}".format(level,root.data))
            resultDict[level].append(root.data)
            self.output.append("Traversing to left node of root")
            self._levelOrderTraversal(root.left,resultDict,level+1)
            self.output.append("Traversing to right node of root")
            self._levelOrderTraversal(root.right,resultDict,level+1)

    def levelOrderTraversal(self,root):
        self.output.append("Creating Dictionary that store all data of particular level")
        resultDict=defaultdict(list)
        self._levelOrderTraversal(root,resultDict,0)
        print(resultDict)

    def rightView(self,root):
        resultDict=defaultdict(list)
        self.output.append("Performing Level Order Traversal")
        self._levelOrderTraversal(root,resultDict,0)
        self.output.append("After level order traversal, all element present at rightmost side of each level will be visible in right view")
        print(resultDict)
        for i in resultDict:
            self.output.append("Rightmost data present at level {} is {}".format(i,resultDict[i][-1]))
    
    def leftView(self,root):
        resultDict=defaultdict(list)
        self.output.append("Performing Level Order Traversal")
        self._levelOrderTraversal(root,resultDict,0)
        self.output.append("After level order traversal, all element present at leftmost side of each level will be visible in left view")
        print(resultDict)
        for i in resultDict:
            self.output.append("Leftmost data present at level {} is {}".format(i,resultDict[i][0]))

    def _topBottomView(self,root,hd,resultDict):
        if root:
            self.output.append("Inserting into Dictionary, key would horizontal distance of that node {} and value be node data {}".format(hd,root.data))
            resultDict[hd].append(root.data)
            self.output.append("Traversing to left node of root")
            self._topBottomView(root.left,hd-1,resultDict)
            self.output.append("Traversing to right node of root")
            self._topBottomView(root.right,hd+1,resultDict)
            
    def topView(self,root):
        self.output.append("Creating Dictionary that store all data of particular horizontal distance")
        resultDict=defaultdict(list)
        self._topBottomView(root,0,resultDict)
        print(resultDict)
        for i in resultDict:
            self.output.append("Data present at top of each horizontal distance will be visible in top view, So for horizontal distance {} value -> {} would be visible".format(i,resultDict[i][0]))
    
    def bottomView(self,root):
        resultDict=defaultdict(list)
        self._topBottomView(root,0,resultDict)
        print(resultDict)
        for i in resultDict:
            self.output.append("Data present at last of each horizontal distance will be visible in bottom view, So for horizontal distance {} value -> {} would be visible".format(i,resultDict[i][-1]))



