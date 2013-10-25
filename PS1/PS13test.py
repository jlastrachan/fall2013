import sys
import random
import numpy as np
import PS1bin
import PS13mycode

if __name__ == "__main__":
    for maxInput, tableSize in [(2,5), (3,10)]:
        print '\n\ntesting with maxInput=%d, tableSize=%d'%(maxInput,tableSize)
        iA = range(maxInput)
        cA = range(tableSize)
        for i in xrange(10):
            print '..'
            msg = [random.choice(iA) for j in xrange(20)]
            cmsg = PS13mycode.compress(msg,maxInput,tableSize)
            assert type(cmsg)==type([]), "encoded message not a list"
            for x in cmsg:
                assert x in cA, "coded message out of range"
            dmsg = PS13mycode.uncompress(cmsg,maxInput,tableSize)
            assert type(dmsg)==type([]), "decoded message not a list"
            for x in dmsg:
                assert x in iA, "decoded message out of range"
            print msg, '->', cmsg
            assert PS1bin.chk3(msg,cmsg,maxInput,tableSize), "incorrect encoding"
            print dmsg
            assert len(msg)==len(dmsg), "incorrect length after decoding"
            for i in xrange(len(msg)):
                assert msg[i]==dmsg[i], "incorrect decoding"
                
    print '\n\nGREAT! NO ERRORS FOUND'  
