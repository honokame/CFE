import numpy as np
import pandas as pd

def calc_eular_explicit(delta_f, f, delta_x, delta_t, gamma, c_offset):
  nmax = len(f)
  a = delta_t * gamma / (delta_x) ** 2 #1.5210000000000001
  b = c_offset * delta_t #0.004
  
  for n in range(1, nmax - 1):
    delta_f[n] = a * (f[n + 1] - 2.0 * f[n] + f[n - 1]) + b
  print(delta_f)
    
if __name__ == '__main__':
  nmax = int(input("Nの値："))
  delta_x = 1.0 / (nmax - 1)
  
  f = np.zeros(nmax)
  delta_f = np.zeros(nmax)
  
  for steps in range(1000):
    calc_eular_explicit(delta_f, f, delta_x, 1.0e-3, 1.0, 4.0)
    f += delta_f
    print(f)
  
  #print("x  f")
  for n, fu_n in enumerate(f):
    x = n * delta_x
    theory = 2 * x * (1 - x) #理論解 f(x)=2x(1-x)
    print("%e %e %e" % (x, fu_n, theory))