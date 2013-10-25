import numpy


def recover(A,msg):
    """
    takes k-by-m ndarray A describing an (n,k,d) linear code with d>2
    and 0/1 string msg of length nN,
    returns 0/1 string of length kN, recovering 1 possible single errors
    in every n-bit word
    """

    k = len(A) 
    m = len(A[0])
    n = m + k
    H = create_H_matrix(A, m)
    syndromes = get_syndromes(H, k)
    result = ""
    while len(msg) > 0:
    	n_msg = msg[0:n]
    	msg = msg[n:]

    	calculated_syndrome = get_syndrome(H, n_msg)
    	received_parity = n_msg[k:]
    	if calculated_syndrome in syndromes:
    		index_of_error = syndromes[calculated_syndrome]
    		corrected_msg = get_sum(n_msg, "0"*index_of_error + "1" + "0"*(n-index_of_error-1))
    		result += corrected_msg[:k]
    	else:
    		result += n_msg[:k]
    return result

def get_sum(code1, code2):
	if len(code1) != len(code2):
		raise Exception("codes not same size")
	result = ""
	for i in range(len(code1)):
		sum = int(code1[i]) + int(code2[i])
		sum %= 2
		result += str(sum)
	return result


def get_syndromes(H, k):
	syndrome_dict = {}
	for j in range(k):
		error_msg = "0"*j + "1" + "0"*(len(H[0])-j-1)
		syndrome = get_syndrome(H, error_msg)
		syndrome_dict[syndrome] = j
	return syndrome_dict

def create_H_matrix(A, m):

	# now add identity matrix
	for i in range(m):
		for j in range(i):
			H[i].append(0)
		H[i].append(1)
		for j in range(i+1, m):
			H[i].append(0)
	return H

def get_syndrome(H, msg):
	# implement matrix multiplication
	result = ""
	for i in range(0,len(H)):
		sum = 0
		for j in range(0,len(H[i])):
			sum += H[i][j]*int(msg[j])
		sum %= 2
		result += str(sum)
	return result

if __name__ == "__main__":
    import sys
    assert len(sys.argv)>2, '%d arguments supplied, 2 needed' %(len(sys.argv)-1)
    A = numpy.array(eval(sys.argv[1]))
    msg = sys.argv[2]
    print recover(A,msg)