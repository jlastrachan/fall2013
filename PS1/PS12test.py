import sys
import random
import numpy as np
import PS1bin
import PS12mycode

alp = 'ABCDEFGH'

if __name__ == "__main__":
    for n in [4, 5, 8]:
        cb = PS1bin.get_cb(n)
        ppl = len(cb)
        alph = range(ppl)
        print '\n\nchecking with code book'
        for word in cb:
            print word
        for i in xrange(5):
            print '..'
            msg = [random.choice(alph) for j in xrange(10)]
            cmsg = PS12mycode.encode(cb,msg)
            assert type(cmsg)==type(''), "encoded message not a string"
            dmsg = PS12mycode.decode(cb,cmsg)
            assert type(dmsg)==type([]), "decoded message not a list"
            for word in dmsg:
                assert type(word)==type(0), "decoded message not a lst of integers"
            print msg, '  ->  ', cmsg
            assert PS1bin.chk2(msg,cmsg,cb), "incorrect encoding"
            print dmsg
            assert len(dmsg)==len(msg), "incorrect length after decoding"
            for i in xrange(len(msg)):
                assert msg[i]==dmsg[i], "incorrect decoding"
                
    print '\n\nGREAT! NO ERRORS FOUND'  
