def encode(codeBook, msg):
    """
    arguments:
    codeBook -- list of 0/1 strings (e.g. the output of PS11mycode.huffman)
    msg      -- list of integers between 0 and len(codeBook)
    
    returns: 0/1 string
    """
    result_code = ""
    for symbol in msg:
        result_code += codeBook[symbol]
    return result_code

def decode(codeBook, msg):
    """
    arguments:
    codeBook -- list of 0/1 strings, prefix-free (e.g. from PS11mycode.huffman)
    msg      -- encoded message (a 0/1 string)
    
    returns: list of integers between 0 and len(codeBook)
    """
    symbol_code = msg[0]
    symbols = []
    while len(msg) > 0:
        if symbol_code in codeBook:
            symbols.append(codeBook.index(symbol_code))
            msg = msg[len(symbol_code):]
            if len(msg) is 0:
                break
            symbol_code = msg[0]
        else:
            symbol_code += msg[len(symbol_code)]
    return symbols


    
if __name__ == "__main__":
    import sys
    import numpy
    import PS1bin

    if len(sys.argv)>2:
        codeBook = numpy.array(eval(sys.argv[1]))
        msg = numpy.array(eval(sys.argv[2]))
    else: 
        raise Exception("Need to have two args: codeBook array and msg array")
    print codeBook
    print "Encoded: ", encode(codeBook.tolist(), msg)
    print "Decoded: ", decode(codeBook.tolist(), encode(codeBook.tolist(), msg))
