class Node():

    def __init__(self, name):

        self.leftChild = None
        self.rightChild = None
        self.name = name

    def setLeftChild(self, node):
        self.leftChild = node

    def setRightChild(self, node):
        self.rightChild = node


    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild


class Tree():

    def __init__(self):

        self.root = None
        self.nodeList = []
        self.preorderList = []
        self.inorderList = []
        self.postorderList = []

    def setRoot(self, node):

        self.root = node

    def getRoot(self):

        return self.root

    def getNodeByName(self, name):

        for nodes in self.nodeList:
            if nodes.name == name:
                return nodes

        return None

    # return True if there is no same name
    def nodeNameCheck(self, name):

        for nodes in self.nodeList:

            if nodes.name == name:
                return False

        return True
    def insertNode(self,nodeInfo):
        for ind in range(3):

            if ind == 0:
                if self.nodeNameCheck(nodeInfo[ind]):

                    newNode = Node(nodeInfo[ind])

                    if len(self.nodeList) == 0:
                        self.setRoot(newNode)
                        self.nodeList.append(newNode)
                else:
                    pass

            elif ind == 1:
                if nodeInfo[ind] == '.':
                    pass
                else:
                    parentNode = self.getNodeByName(nodeInfo[0])
                    if self.nodeNameCheck(nodeInfo[ind]):
                        newNode = Node(nodeInfo[ind])
                        self.nodeList.append(newNode)
                        parentNode.setLeftChild(newNode)
                    else:
                        childNode = self.getNodeByName(nodeInfo[ind])
                        paretNode.setLeftChild(childNode)



            else: #ind == 2:
                if nodeInfo[ind] == '.':
                    pass
                else:
                    parentNode = self.getNodeByName(nodeInfo[0])
                    if self.nodeNameCheck(nodeInfo[ind]):
                        newNode = Node(nodeInfo[ind])
                        self.nodeList.append(newNode)
                        parentNode.setRightChild(newNode)
                    else:
                        childNode = self.getNodeByName(nodeInfo[ind])
                        parentNode.setRightChild(childNode)

    def preorder(self, node):

        self.preorderList.append(node.name)
        if node.leftChild != None:
            self.preorder(node.leftChild)
        if node.rightChild != None:
            self.preorder(node.rightChild)

    def inorder(self, node):
        if node.leftChild != None:
            self.inorder(node.leftChild)
        self.inorderList.append(node.name)
        if node.rightChild != None:
            self.inorder(node.rightChild)

    def postorder(self, node):
        if node.leftChild != None:
            self.postorder(node.leftChild)
        if node.rightChild != None:
            self.postorder(node.rightChild)
        self.postorderList.append(node.name)


tree = Tree()

for x in range(input("")):
    nodeInfo = raw_input("").split(" ")
    tree.insertNode(nodeInfo)

tree.preorder(tree.getRoot())
tree.inorder(tree.getRoot())
tree.postorder(tree.getRoot())

print "".join(tree.preorderList)
print "".join(tree.inorderList)
print "".join(tree.postorderList)
