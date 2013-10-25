import numpy
import math
def optimal(k):
    """
    output k-by-m ndarray
    representing the A matrix of a linear (n,k,3) code
    with minimal possible n
    """
    m = 1
    while k > 2**m - m - 1:
    	m+=1
    n = m + k

    A = []

    for parity_bit in range(m):
    	par_index = 2**parity_bit
    	row = []
    	for i in range(1,n+1):
    		bin_i = get_binary_of_num(i, n)
    		log_of_index = math.log(i,2)
    		diff = int(log_of_index*1000)/1000. - int(log_of_index)
    		if ((i > 2**(m-1)) or (diff > .001)):
    			g = bin_i[-parity_bit-1]
    			row.append(g)
    	A.append(row)
    A_str = str(transpose(A))
    return numpy.array(eval(A_str))

def transpose(A):
	H = []
	for j in range(len(A[0])):
		col_to_row = []
		for i in range(len(A)):
			col_to_row.append(A[i][j])
		H.append(col_to_row)
	return H

def binary_and(num1, num2, index):
	if num1[index] is 1 and num2[index] is 1:
		return 1
	return 0

def get_binary_of_num(i, n):
	bin_str = "{0:b}".format(i)
	if len(bin_str) != n:
		for i in range(n-len(bin_str)):
			bin_str = "0"+bin_str
	return [int(i) for i in bin_str]


if __name__ == "__main__":
    import sys
    assert len(sys.argv)>1, '%d arguments supplied, 1 needed' %(len(sys.argv)-1)
    k = int(sys.argv[1])
    print optimal(k)