import sympy
import random
from time import perf_counter_ns


def keyMaking(m, prevM):
    p = sympy.randprime(prevM,m)
    g = sympy.randprime(int(p//2), p)
    k_pr = random.randint(int(p//2),p)
    i = random.randint(int(p//2),p)
    
    k_E = pow(g,i,p)
    
    shared_key = pow(k_E,k_pr,p)
    
    return shared_key, p


if __name__ == "__main__":
    for n in range(1024):
        
            m = int(pow(2, n))
            
            if n >= 3:
                
                start = perf_counter_ns()
                
                share_key, prime = keyMaking(m, prevM)
                
                end = perf_counter_ns()
                
                file1 = open("time.txt","a")
                file1.write(format(end-start) + "\n")
                print(end - start)
                file1.close()
                
                file2 = open("primes.txt", "a")
                file2.write(format(prime) + "\n")
                print()
                file2.close()
                
            if n >= 1:
                prevM = int(m)
