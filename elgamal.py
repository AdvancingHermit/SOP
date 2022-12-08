import sympy
import random
from time import perf_counter_ns

def shared_secret(g,x,p):
  # Shared Secret (h)
  h = pow(g,x,p)
  return h

def keyMaking(p):
    g = sympy.randprime(int(p/2), p)
    x = random.randint(int(p/2),p)
    r = random.randint(int(p/2),p)
    h = pow(g,x,p)
    return h

def numberGen(n):
    return end - start


if __name__ == "__main__":
    for n in range(1024):
            m = int(pow(2, n))
            if n >= 3:
                start = perf_counter_ns()
                p = sympy.randprime(prevM,m)
                share_key = keyMaking(p)
                end = perf_counter_ns()
                file1 = open("time.txt","a")
                file1.write(format(end-start) + "\n")
                print(end - start)
                file1.close()
                file2 = open("primes.txt", "a")
                file2.write(format(p) + "\n")
                print()
                file2.close()
                
            if n >= 1:
                prevM = int(m)
                
                
                
                