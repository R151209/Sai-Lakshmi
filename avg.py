import matplotlib.pyplot as plt
import numpy as np
f1=input("enter f1 value:")
f2=input("enter f2 value:")
n=input("enter no.of samples:")
t=np.arange(n)
x1=np.sin(2*np.pi*f1*t)
plt.subplot(3,1,1)
plt.plot(t,x1)
plt.title('sin_low frequency')
x2=np.sin(2*np.pi*f2*t)
plt.subplot(3,1,2)
plt.plot(t,x2)
plt.title('sin_high frequency')
x=x1+x2
plt.subplot(3,1,3)
plt.plot(t,x)
plt.title('sum of two waves')
plt.show( )
