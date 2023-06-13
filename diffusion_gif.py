import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from matplotlib.animation import PillowWriter

def calc_eular_explicit(delta_f, f, delta_x, delta_t, gamma, c_offset):
  nmax = len(f)
  a = delta_t * gamma / (delta_x) ** 2 #1.5210000000000001
  b = c_offset * delta_t #0.004
  
  for n in range(1, nmax - 1):
    delta_f[n] = a * (f[n + 1] - 2.0 * f[n] + f[n - 1]) + b
  #print(delta_f)
    
if __name__ == '__main__':
  image = []
  nmax = int(input("Nの値："))
  delta_x = 1.0 / (nmax - 1)
  x = np.zeros(nmax)
  for n in range(nmax):
    x[n] = n * delta_x
  f = np.zeros(nmax)
  delta_f = np.zeros(nmax)
  
  fig,ax = plt.subplots()
  for steps in range(1000):
    calc_eular_explicit(delta_f, f, delta_x, 1.0e-3, 1.0, 4.0)
    f += delta_f
    ax.set_xlim(0,1) 
    ax.set_ylim(0,0.6) 
    graph = ax.plot(x,f,color='C0')
    image.append(graph)
  
  ani = ArtistAnimation(fig, image, interval=100, blit=True, repeat_delay=1000)
  ani.save("diffusion.gif", writer='pillow')  
  
  #print("x  f")
  for n, fu_n in enumerate(f):
    x = n * delta_x
    theory = 2 * x * (1 - x) #理論解 f(x)=2x(1-x)
    print("%e %e %e" % (x, fu_n, theory))