import numpy as np
a= np.array([1,2,3])
b= np.array([4,5,6])
print(a)
print
print(b) 
print(b.ndim)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(x)
print(x.ndim)
print(y)
print(y.ndim)


arg3= np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arg3)
print(arg3.ndim)


# numpy create array specify data type
ar_zero= np.zeros(5)
print(ar_zero)

rm_zero= np.zeros(19)
print(rm_zero)

sr_zero= np.zeros((3, 4))
print(sr_zero)

er_zero= np.zeros((3, 4, 5))
print(er_zero)

et_one= np.ones(5)
print(et_one)

qw_one = np.ones(4)
print(qw_one)


# ranmdom number ranges 

var= np.random.rand(5)
print(var)
# [0.43879525 0.34325879 0.39532866 0.28885364 0.64352538]

# [0.87351097 0.10029616 0.00173895 0.71644151 0.01646489]

var1= np.random.rand(2,5)
print(var1)
var2= np.random.rand(3,4)
print(var2)
