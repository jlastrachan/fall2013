class Node(object):
    def __init__(self, index, prob):
        self.index = index
        self.prob = prob
        self.code = ""
        self.left = None
        self.right = None

    def add_code(self, code_letter):
        self.code += code_letter
        if self.left is not None:
            self.left.add_code(code_letter)
        if self.right is not None:
            self.right.add_code(code_letter)

    def get_code_if_leaf(self):
        if self.left is None and self.right is None:
            return self.code
        return None

    def get_all_codes(self):
        # Returns dict containing {index: code}
        code_dict = {}
        self.add_code_to_dict(code_dict)
        return code_dict

    def add_code_to_dict(self, code_dict):
        code = self.get_code_if_leaf()
        if code is not None:
            code_dict[self.index] = code
        else:
            self.left.add_code_to_dict(code_dict)
            self.right.add_code_to_dict(code_dict)

    def __str__(self):
        return "("+str(self.index)+","+str(self.left)+","+str(self.right)+")"



def huffman(pList):
    """
    argument: pList -- numpy.array of probabilities
    return: (codeBook, codeLength)
       codeBook   -- a Huffman code: codeBook[k] encodes the symbol
                     with probability pList[k]
    codeLength -- code length for the codeBook
    """
    node_list = list()
    for i in range(0, len(pList)):
        node_list.append(Node(i, pList[i]))
    if len(pList) > 2:
        # We have at least two elements
        min_elt1 = pList.argmin()
        prob1 = pList[min_elt1]
        pList[min_elt1] = 2
        min_elt2 = pList.argmin()
        pList[min_elt2] = prob1 + pList[min_elt2]
        while pList[min_elt1] < 2 or pList[min_elt2] < 2:
            node1 = node_list[min_elt1]
            node2 = node_list[min_elt2]

            parent_node = Node(-1, pList[min_elt2])
            parent_node.left = node1
            parent_node.right = node2
            node_list[min_elt2] = parent_node
            node_list[min_elt1] = None
            if round(pList[min_elt2]*100)/100.0 >= 1:
                break
            min_elt1 = pList.argmin()
            prob1 = pList[min_elt1]
            pList[min_elt1] = 2
            min_elt2 = pList.argmin()
            pList[min_elt2] = prob1 + pList[min_elt2]

        nodes_to_code = [(node_list[min_elt2].left, '0'), (node_list[min_elt2].right, '1')]


        codeLength = 0
        # add all codes
        while len(nodes_to_code) > 0:
            (node, code) = nodes_to_code.pop()
            node.add_code(code)
            codeLength += node.prob
            if node.left is not None:
                nodes_to_code.append((node.left, '0'))
            if node.right is not None:
                nodes_to_code.append((node.right, '1'))



        codeDict = node_list[min_elt2].get_all_codes()

        codeBook = [0]*len(pList)
        for x in codeDict:
            codeBook[x] = codeDict[x]
        return (codeBook, codeLength)


    elif len(pList) == 1:
        raise NotImplementedError
    else:
        return None


        
        
    
    
    
if __name__ == "__main__":
    import sys
    import numpy
    import PS1bin
    if len(sys.argv)>1:
        pList = numpy.array(eval(sys.argv[1]))
    else:
        pList = PS1bin.get_dist(5)
    print 'pList = ', pList
    (codeBook, codeLength) = huffman(pList)
    print 'codeLength = ', codeLength
    print 'codeBook:'
    for x in codeBook:
        print x
