class  Node:
    def __init__(self):
        self.symbol=None
        self.left=None
        self.right=None
    
    def leftNode(self):
        return self.left

    def rightNode(self):
        return  self.right

    def addRightNode(self):
        if self.right==None:
            self.right=Node()

    def addLeftNode(self):
        if self.left==None:
            self.left=Node()
  

class PrefixCodeTree:
    def __init__(self):
        self.root=Node()
    def insert(self,codeword,symbol):
        node=self.root
        for bit in codeword:
            if bit==0:
                node.addLeftNode()
                node=node.left
            else:
                node.addRightNode()
                node=node.right
        node.symbol=symbol
    
    def decode(self,encodedData,datalen):
        node=self.root
        arr=[]
        ans=" "

        for i in encodedData:
            arr+= bin(i)[2:].zfill(8)
        arr=arr[:datalen]

        print(arr)
        count=0
        for bit in arr:
            count+=1
            if bit =='0':
                node=node.left
            elif bit == '1':
                node=node.right
            if node.symbol!=None:
                ans +=node.symbol+" "*count
                node=self.root
                count=0
        return ans

if __name__=="__main__":
    codebook={
        'x1': [0],
        'x2': [1,0,0],
        'x3': [1,0,1],
        'x4': [1,1], 
    }
    tree=PrefixCodeTree()
    for symbol in codebook:
        tree.insert(codebook[symbol],symbol)
    
    mess=tree.decode(b'\xd2\x9f\x20', 21)
    print(mess)





    
