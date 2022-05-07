class Address:
    def __init__(self,adr,inter=None):
        self.adr=adr
        self.inter=inter

    def toBinary(self):
        array=self.adr.split('.')
        binary=''
        for i in range(4):
            holder = str(bin(int(array[i])))[2:]
            binary += '0'*(8-len(holder))+holder
        return binary


class Node:
    def __init__(self,right=None,left=None,pre=None,inter=None):
        self.right=right
        self.left=left
        self.prefix=pre
        self.inter=inter


class Tree:
    def __init__(self,default):
        self.root=Node()
        self.default=default

    def constructTree(self,adr):
        node=self.root
        pref=''
        for i in adr.toBinary():
            if  i == '1' :
                pref += '1'
                if node.right is None:
                    node.right = Node(pre=pref)
                node=node.right
            else :
                pref += '0'
                if node.left is None:
                    node.left = Node(pre=pref)
                node = node.left
        node.inter=adr.inter

    def contructionBinaryTrie(self,linesFromFile):
        for line in linesFromFile:
            array=line.split(' ')
            adr=Address(array[0], array[1])
            self.constructTree(adr)

    def searchBinaryTrie(self,entry):
        node=self.root
        for i in entry:
            if node is None:
                return self.default + "(default)"
            elif  i == '1' :
                node=node.right
            else :
                node = node.left
        if node.inter is not None:
            return node.inter

    def showResult(self,Entries):
        for i in Entries:
            adr=Address(i)
            print("forwading " +i+ " => "+ self.searchBinaryTrie(adr.toBinary()))



if __name__ == "__main__" :
    print("*******starting*******")
    file1 = open("FIB.txt", "r")
    file2 = open("entry.txt", "r")
    fib=file1.readlines()
    entries=file2.readlines()
    tree=Tree(fib[-1][-1])
    print(fib)
    print(entries)
    print(fib[-1][-1])
    tree.contructionBinaryTrie(fib[:-1])
    tree.showResult(entries)

            