import sympy
import random
from time import perf_counter_ns


def keyMaking(p, k_pr, g, div):

    i = random.randint(div,p)
    
    k_E = pow(g,i,p)
    
    shared_key = pow(k_E,k_pr,p)
    
    return shared_key


if __name__ == "__main__":
    for n in range(2049):
        
            m = int(pow(2, n))
            
            if n >= 3:
                p = sympy.randprime(prevM,m)
                div = int(p//2)
                g = sympy.randprime(div, p)
                k_pr = random.randint(div,p)
                
                start = perf_counter_ns()
                
                share_key = keyMaking(p, k_pr, g, div)
                
                end = perf_counter_ns()
                
                file1 = open("optimeretTime.txt","a")
                file1.write(format(end-start) + "\n")
                print(end - start)
                file1.close()
                
                file2 = open("optimeretPrimes.txt", "a")
                file2.write(format(p) + "\n")
                print()
                file2.close()
                
            if n >= 1:
                prevM = int(m)
