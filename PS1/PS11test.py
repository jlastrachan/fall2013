import sys
import numpy as np
import PS1bin
import PS11mycode


if __name__ == "__main__":
    for n in [4, 5, 8, 10, 20]:
        pp = PS1bin.get_dist(n)
        ppl = len(pp)
        print '\n\nchecking with pList = ', pp
        print '...'
        (codeBook, codeLength) = PS11mycode.huffman(pp.copy())
        print 'your codeBook ( codeLength = ', codeLength, ' ):'
        print codeBook
        assert type(codeBook)==type([]), "code book is not a list"
        assert ppl==len(codeBook), "wrong code book length"
        for word in codeBook:
            assert type(word)==type(''), "code word not a string"
            for x in word:
                assert x in ['0','1'], "code word has symbols other than 1 or 0"
        for i in xrange(ppl):
            for j in xrange(ppl):
                if i != j:
                    assert not codeBook[i].startswith(codeBook[j]),\
                           "code book is not prefix-free"
        s = 0.0
        for i in xrange(ppl):
            s += pp[i]*len(codeBook[i])
        assert abs(s-codeLength)<1e-6, "computed and actual code length do not match"
        assert PS1bin.chk1(pp,codeLength), "code book is far from optimal"    
    print '\n\nGREAT! NO ERRORS FOUND'            
        
