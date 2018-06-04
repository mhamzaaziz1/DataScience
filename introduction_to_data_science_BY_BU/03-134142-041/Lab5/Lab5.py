import numpy as np
#_______________________________________________________________________________
#Create a random vector of size 10 and sort it
x = np.random.random(10)        #getting random vector
print("Original array:")
print(x)
x.sort()                        #sorting random vector
print("Sorted array:")
print(x)
#_______________________________________________________________________________
#Check two random arrays are equal or not
x = np.random.randint(0,2,6)        # random array
print("First array:")
print(x)
y = np.random.randint(0,2,6)        # random array
print("Second array:")
print(y)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(x, y)     #Checking two random arrays
print(array_equal)
#_______________________________________________________________________________
#Create a null vector of size 10 and update sixth value to 11
x = np.zeros(10)                #NULL Vector 
print(x)
print("Update sixth value to 13")
x[4] = 13                   #updating value
print(x)
#_______________________________________________________________________________
#Create a 3x3 matrix with values ranging from 2 to 10
x =  np.arange(2, 11).reshape(3,3)     #Create a 3x3 matrix
print(x)
#_______________________________________________________________________________
# Add, subtract, multiply, divide arguments element-wise
print("Add:")
print(np.add(1.0, 4.0))         # Adding element-wise
print("Subtract:")
print(np.subtract(1.0, 4.0))        #subtract element-wise
print("Multiply:")
print(np.multiply(1.0, 4.0))        #multiply element-wise
print("Divide:")
print(np.divide(1.0, 4.0))      #dividing element-wise

#_______________________________________________________________________________
#Get true division of the element-wise array inputs
x = np.arange(10)           #array inputs upto 10
print("Original array:")
print(x)
print("Division of the array inputs, element-wise:")
print(np.true_divide(x, 4))     #Division of the array inputs, element-wise:
#______________________________________________________________________________
#PythonNumPy: Generate inner, outer, and cross products of matrices and vectors
x = np.array([1, 4, 0], float)   #declaring vectors
y = np.array([2, 2, 1], float)
print("Matrices and vectors.")
print("x:")
print(x)
print("y:")
print(y)
print("Inner product of x and y:")
print(np.inner(x, y))               #inner product
print("Outer product of x and y:")
print(np.outer(x, y))               #outer product
print("Cross product of x and y:")
print(np.cross(x, y))               #Cross product
print("Dot product of x and y:")
print(np.dot(x, y))                 #Dot Product
#_______________________________________________________________________________
#Find the roots of the given polynomials
print("Roots of the first polynomial:")
print(np.roots([1, 1.5, 2]))        #getting roots of polynomial
print("Roots of the second polynomial:")
print(np.roots([1, -5.09]))         #getting roots of polynomial
#_______________________________________________________________________________
# Add, subtract, multiply and divide polynomials
from numpy.polynomial import polynomial as P
x = (10,20,30)              #declaring polynomials
y = (30,40,50)
print("Add one polynomial to another:")
print(P.polyadd(x,y))           #Adding polynomial
print("Subtract one polynomial from another:")
print(P.polysub(x,y))           #Subtracting polynomial
print("Multiply one polynomial by another:")
print(P.polymul(x,y))           #Multiplying polynomial
print("Divide one polynomial by another:")
print(P.polydiv(x,y))           #Dividing polynomial
#_______________________________________________________________________________
#Compute sine, cosine and tangent array of angles given in degrees
print("sine: array of angles given in degrees")
print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.)) #Computing sin of angles
print("cosine: array of angles given in degrees")
print(np.cos(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.)) #Computing cos of angles
print("tangent: array of angles given in degrees")
print(np.tan(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.)) #Computing tan of angles
#_______________________________________________________________________________
