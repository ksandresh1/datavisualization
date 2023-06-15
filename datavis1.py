# this is how we use to plot the data in python's matplotlib
import matplotlib.pyplot as plt
a = [-4,-3,-2,-1,0,1,2,3,4]
b = [16,9,4,1,0,1,4,9,16]
# plt.plot(a,b)
plt.scatter(a,b)
plt.xlabel("Value of A")
plt.ylabel("Value of B")
plt.title("Line plot")
plt.show()