import numpy

def linear(A,msg):
    """
    encode 1/0 string of length kN into 1/0 string of length nN
    using linear block (n,k,d) code described by its k-by-m matrix A
    """
    output = ""
    while len(msg) > 0:
    	output+=get_code(A, msg[0:len(A)])
    	msg = msg[len(A):]

    return output

def get_code(A, msg):
	"""
	takes in msg of length k and returns a encoded message of length n.
	"""
	# implement matrix multiplication
	for j in range(0,len(A[0])):
		sum = 0
		for i in range(0,len(A)):
			sum += A[i][j]*int(msg[i])
		sum %= 2
		msg += str(sum)
	return msg

if __name__ == "__main__":
    import sys
    assert len(sys.argv)>2, '%d arguments supplied, 2 needed' %(len(sys.argv)-1)
    A = numpy.array(eval(sys.argv[1]))
    msg = sys.argv[2]
    print linear(A,msg)
