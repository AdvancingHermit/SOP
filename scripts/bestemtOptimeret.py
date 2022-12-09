import sympy
import random
from time import perf_counter_ns


def keyMaking(p, k_pr, g, div):

    i = random.randint(div,p)
    
    k_E = pow(g,i,p)
    
    shared_key = pow(k_E,k_pr,p)
    
    return shared_key


if __name__ == "__main__":
        for x in range(3):
    
            n = 15360
            m = int(pow(2, n))
            prevM = int(pow(2,n-1))
            
            
            if n >= 3:
                p = sympy.randprime(prevM,m)
                div = int(p//2)
                g = sympy.randprime(div, p)
                k_pr = random.randint(div,p)
                
                start = perf_counter_ns()
                
                share_key = keyMaking(p, k_pr, g, div)
                
                end = perf_counter_ns()
                
                file1 = open("certainTime.txt","a")
                file1.write(format(end-start) + "\n")
                print(end - start)
                file1.close()


                
            
                S