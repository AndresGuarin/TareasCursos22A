import numpy as np

# Physical parameters
a=1
b=1
L=10
c=1

# Code parameters
N = 100
Nx = 100
Nt = 200

# Functions
def A_n(n):
    return 2*a/b * L/(n*np.pi)**2 * ( -np.sin(n*np.pi*2*b/L) + 2*np.sin(n*np.pi*b/L) )

A=[A_n(n) for n in range(1,N)]

def u_n(n,x,t):
    return A[n-1] * np.cos(c*n*np.pi*t/L)*np.sin(n*np.pi*x/L)

# Find solution
x = np.linspace(0,L,Nx)
t = np.linspace(0,20,Nt)
u = np.zeros((Nx,Nt))

for i in range(Nt):
    for j in range(Nx):
        for n in range(1,N):
            u[j,i] += u_n(n,x[j],t[i])
