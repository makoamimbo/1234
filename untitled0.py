# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IblKH8fS3VGgEKyPi8HhvG2F-GG6xT3i
"""

import numpy as np
import matplotlib.pyplot as plt

import sympy

from sympy import*

p = -1
A = np.array([[-5,1]])
B = np.array([[1,p]])
C = np.array([[4,-2]])

M=print(np.concatenate((B-A,C-A)).T)

# import sympy
import sympy
  
# find the reduced row echelon form
sympy.Matrix([[6,-2],[9,-3]]).rref()
  
# find the rank of matrix
print("Rank of matrix :",sympy.Matrix([[6,-2],[9,-3]]).rank())


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
  
#Defining the points
A = np.array([-5,1])
B = np.array([1,-1])
C = np.array([4,-2])

#Generating lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1 + 0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor