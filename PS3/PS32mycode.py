import sys
import numpy

class Viterbi():
    """
    decoder = Viterbi(W)
    u = decoder.decode(y)
    """
    def __init__(self,W):
        self.W = W
        self.r = len(self.W)
        self.K = len(self.W[0])

    def back(self,x):
        """
        (x0,x1)=decoder.back(x) returns two possible previous states
        """
        x0 = 2*x % 2**(self.K-1)
        x1 = (2*x + 1) % 2**(self.K-1)
        return (x0, x1)
    
    def out(self,x):
        """
        (y0,y1)=decoder.out(x) returns two possible output sequences
        """
        y0 = [sum(numpy.convolve(self.W[i], self.reverse(self.get_binary_of_num(x, self.K-1)) + (0,), 'valid')) for i in range(len(self.W))]
        y1 = [sum(numpy.convolve(self.W[i], self.reverse(self.get_binary_of_num(x, self.K-1)) + (1,), 'valid')) for i in range(len(self.W))]

        for i in range(len(y0)):
            y0[i] %= 2
            y1[i] %= 2
        return (y0,y1)

    def reverse(self, x):
        """Reverse the array, used in convolution"""
        return tuple([x[len(x)-i-1] for i in range(len(x))])
    
    def cost(self, bits, values):
        return sum([abs(bits[i] - values[i])**2 for i in range(len(bits))])

    def decode_k_is_1(self,y):
        """Decode if k = 1, algorithm differs in that you work forward. Not less efficient because only
        one state, so we are enumerating through exactly how many we have to."""

        final_time = len(y)/self.r
        self.path_metrics = [0]*(final_time+1)
        result_code = []
        unique = True
        y0,y1 = self.out(0)
        for time in range(final_time):
            # Step through each time step and compute next time step's path metric
            bits = y[self.r*(time):self.r*(time+1)]
            cost0 = self.cost(y0, bits)
            cost1 = self.cost(y1, bits)

            if cost0 <= cost1:
                result_code.append(0)
                self.path_metrics[time+1] = cost0 + self.path_metrics[time]
                if cost0 == cost1:
                    # Either option is just as good, so code isn't unique
                    unique = False
            else:
                result_code.append(1)
                self.path_metrics[time+1] = cost1 + self.path_metrics[time]
        return (numpy.array(result_code), self.path_metrics[final_time], unique)


    
    def decode(self,y):
        if self.K == 1:
            return self.decode_k_is_1(y)

        unique = True
        final_time = len(y)/self.r

        # Set up the trellis (num states x time steps 2d array). Init all vals to +inf except at time 0 and state 0
        self.trellis = [[0] + [float("inf")]*(final_time)]
        for time_step in range(1, 2**(self.K-1)):
            self.trellis.append([float("inf")]*(final_time+1))

        self.previous_state = [[0]*(final_time+1) for _ in range(2**(self.K-1))]

        # Compute path metrics at every time step
        for time_step in range(1,final_time+1):
            unique = (self.set_path_metrics(time_step, y[self.r*(time_step-1):self.r*time_step]) and unique)
        
        # Get the final index of the min path metric
        min_path_metric = 0
        for i in range(1,2**(self.K-1)):
            if self.trellis[i][final_time] < self.trellis[min_path_metric][final_time]:
                min_path_metric = i

        # Do backtrack to get actual code sequence
        time = final_time
        state = min_path_metric
        result_code = []
        while time > 0:
            if state >= 2**(self.K-2):
                result_code.insert(0,1)
            else:
                result_code.insert(0,0)
            
            state = self.previous_state[state][time]
            time -= 1
        for t in range(final_time+1):
            print_array = []
            for state in range(2**(self.K-1)):
                print_array.append(self.trellis[state][t])

        vals = [self.trellis[i][final_time] for i in range(2**(self.K-1))]
        min_val = min(vals)

        # Code is not unique if at any point the code came together (unique val returned by path 
        # metric calculation at every time step) or if there are two min values at the end (the 
        # length of the set of path metrics non-infinite at final_time is not equal to the length
        # of the list of these values)
        unique = unique and vals.count(min_val) == 1
        return (numpy.array(result_code), self.trellis[min_path_metric][final_time], unique)


    def set_path_metrics(self, time, par_bits):
        non_unique = []
        for state in range(2**(self.K-1)):
            x0, x1 = self.back(state)

            cost0 = self.cost(par_bits, self.out(x0)[int(state >= 2**(self.K-2))])
            cost1 = self.cost(par_bits, self.out(x1)[int(state >= 2**(self.K-2))])

            cost0 += self.trellis[x0][time-1]
            cost1 += self.trellis[x1][time-1]
            if cost0 <= cost1:
                self.trellis[state][time] = cost0
                self.previous_state[state][time] = x0
                if cost0 == cost1 and cost0 != float('inf'):
                    non_unique.append(state)
            else:
                self.trellis[state][time] = cost1
                self.previous_state[state][time] = x1

        min_index = 0
        min_elt = self.trellis[0][time]
        for i in range(1, 2**(self.K-1)):
            if self.trellis[i][time] < min_elt:
                min_elt = self.trellis[i][time]
                min_index = i
        # Only care for uniqueness if the costs that converged were to the min element
        return (not(min_index in non_unique))

    def get_binary_of_num(self, i, n):
        bin_str = "{0:b}".format(i)
        if len(bin_str) != n:
            for i in range(n-len(bin_str)):
                bin_str = "0"+bin_str
        return tuple([int(i) for i in bin_str])


if __name__ == "__main__":
    if len(sys.argv)==3:
        decoder = Viterbi(numpy.array(eval(sys.argv[1])))
        (u, Pmin, unique) = decoder.decode(numpy.array(eval(sys.argv[2])))
        print ''.join([str(x) for x in u]), \
        '   ( Pmin =',Pmin,', unique =',unique,')'

