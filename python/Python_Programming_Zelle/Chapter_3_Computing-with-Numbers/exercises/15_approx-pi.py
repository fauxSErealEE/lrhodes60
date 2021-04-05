#approx-pi.py

import math as math
import timeit as timeit
import time as time

NANO_TO_SEC_CONV = 1000000000

def main():
    loop = True
    while (loop == True):
        n = eval(input("Enter depth to approx pi: "))
        if (n < 0):
            print("Entered negative number, used absolute value")
            n = n * (-1)

        pi_approx = 0
        #tic = timeit.timeit()
        tic = time.perf_counter_ns()
        for i in range(1,n + 1,1):
            if ( (i % 2) == 0):
                #even number index
                next_term = float((-4) / (2*i - 1))
            else:
                #odd number index
                next_term = float(4 / (2*i - 1))
            pi_approx = float(pi_approx + next_term)
        
        #toc = timeit.timeit()
        toc = time.perf_counter_ns()
        print("toc:",toc)
        print("tic:",tic)
        print("The loop took",(toc-tic)/NANO_TO_SEC_CONV,"seconds to complete")

        print("The approximation of pi is",pi_approx)

        err = math.pi - pi_approx
        print("The error is",err)

        loop_inp = input("Keep looping (Y/N)? ")
        if(loop_inp == 'y') | (loop_inp == 'Y'):
            loop = True
        else:
            loop = False
main()