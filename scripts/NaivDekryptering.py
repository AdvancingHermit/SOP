import sympy
import random
from time import perf_counter_ns
import math


def keyMaking(m, prevM):
    p = sympy.randprime(prevM,m)
    g = sympy.randprime(int(p/2), p)
    k_pr = random.randint(int(p/2),p)
    beta = pow(g, k_pr, p)
    
    return g, k_pr, beta, p

if __name__ == "__main__":
    for n in range(2, 124):
        
            m = int(pow(2, n))
            
            if n >= 3:
                
                
                generator, bob_private_key, bob_public_key, prime = keyMaking(m, prevM)
                maybe_share_key = 0
                
                start = perf_counter_ns()
                
                for x in range(2, prime):
                    k = pow(generator, x, prime)
                    if k == bob_public_key:
                        print("Did Work")
                        break
                
                end = perf_counter_ns()
                
                file1 = open("timeForDLP.txt","a")
                file1.write(format(end-start) + "\n")
                print(end - start)
                file1.close()
                
                file2 = open("primeForDLP.txt", "a")
                file2.write(format(prime) + "\n")
                print()
                file2.close()
                
            if n >= 1:
                prevM = int(m)