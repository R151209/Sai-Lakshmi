import matplotlib.pyplot as plt
n=input("Enter the number of samples:")
x=[]
for i in range(0,n):
	a=input("Enter the values:")
	x.append(a)
print(x)
r=[]
for j in range(n-1,0,-1):	
	r.append(x[j])
r.append(x[0])
print(r)
plt.stem(r)
plt.show()
