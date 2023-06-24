# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#numpy in arrays

"""

import numpy as np
#0 dimentional array
x=np.array(2)
print(x)
#one dimentional
a=np.array([1,2,3])
print(a.ndim)
# 2 dimentional array
b=np.array([[1,2,3,4,5],[1,2,3,4,9]])
print(b)
# 3 dimentional array
c=np.array([[[1,2,3,4,5],[1,2,3,4,9],[4,3,8,9,4]]])
print(c.ndim)
# multi dimention array
d=np.array([1,2,3,4,5,6,3,6],ndmin=6)
print("higher dim:", d)

"""
#output
#2
#1
#[[1 2 3 4 5]
# [1 2 3 4 9]]
#3
#higher dim: [[[[[[1 2 3 4 5 6 3 6]]]]]]



#numpy in slicing


"""
import numpy as n
x=n.array(["hi",2,3,"sesan"])
print(x[0],x[3])

y=n.array([[[1,2,3],[9,8,7,],[3,2,8],[2,3,6]]])
print(y[0,0: ,1])
print(y[0,1,1])
print(y[0,-1])
print(y[0,-1,-1])
print(y[0,-1,-3])
print(y[0,-1: ])
"""

#output

#hi sesan
#[2 8 2 3]
#8
#[2 3 6]
#6
#2
#[[2 3 6]]




# NUMPY DATATYPES


#    i --> integer
#    b --> boolean
#    u --> unsigned integer
#    U --> unicode string
#    f --> float
#    c --> complex float
#    m --> timedelta
#    o --> object 
#    M --> datetime
#    S --> string
#    V --> void(Null)


#import numpy as np

"""
a=np.array([1,2,3,9,6])
print(a.dtype)

b=np.array(["hi","sesan","komal"])
print(b.dtype)
"""

# output

# int32
# <U5 -->unicode string

"""
c=np.array([1,2,3,9,6],dtype="S")
print(c.dtype)
"""

# output

# |S1 --->string( bytes)

"""
c=np.array([1,2,3,9,6],dtype="i4")
print(c.dtype)
d=np.array([1,2,3,9,6],dtype="i8")
print(d.dtype)
e=np.array([1,2,3,9,6],dtype="i")
print(e.dtype)
"""

# int32
# int64
# int32

# ********************************************************
# astype()


"""
d=np.array([1,2,3,9,6])
new_d= d.astype("S")
print(new_d.dtype)
"""

#output
#|s11
"""
d=np.array([1.1,2.3,3.6,9.0,6])
new_d= d.astype("i")
print(new_d.dtype)

"""
#output
#int32

"""
d=np.array([1,0,2])
new_d= d.astype("bool")
new_e=d.astype(int)
print(new_e)
print(new_d.dtype)
print(new_d)
"""

# output

# [1 0 2]
# bool
# [ True False  True]


#-----------------------------------------------------------------


# NUMPY COPY AND VIEW

# COPY

"""
import numpy as np
x= np.array([1,2,3,4,5,6])
y= x.copy()
x[3]=2002
print(x)
print(y)
"""

#output

# [   1    2    3 2002    5    6]
# [1 2 3 4 5 6]


# VIEW (compare password check)

"""
import numpy as np
x= np.array([1,2,3,4,5,6])
y= x.view()
x[3]=2002
print(x)
print(y)
"""

#output

# [   1    2    3 2002    5    6]
# [   1    2    3 2002    5    6]


#-----------------------------------------------------------------

# NUMPY ARRAY SHAPE AND RESHAPE


# SHAPE(structure)

"""
import numpy as np
x=np.array([[1,4,5,3,6],[3,6,9,4,2]])
print(x.shape)
"""

#output
# (2, 5)  --> 2- dimetion   5-elements

"""
x=np.array([1,4,5,3,6],ndmin=6)
print(x)
print(x.shape)
"""

# output
# [[[[[[1 4 5 3 6]]]]]]
# (1, 1, 1, 1, 1, 5)

# 1-[]  , 1-[] , 1-[]  , 1-[]  , 1-[]--elements   5-[1 4 5 3 6] elements





# RESHAPE

"""
import numpy as np
x=np.array([1,4,5,3,6,3,5,7,3,7,3,8,0,4,2,6,3,7])  #18 elements
y=x.reshape(3,6)
print(y)
"""

#output

# now it is a 2 dimentions

# [[1 4 5 3 6 3]
#  [5 7 3 7 3 8]
#  [0 4 2 6 3 7]]


"""
import numpy as np
x=np.array([1,4,5,3,6,3,5,7,3,7,3,8,0,4,2,6,3,7])  #18 elements
y=x.reshape(2,3,3)
print(y)
"""

#output
   
# 3 dimentional array

# [[[1 4 5]
#   [3 6 3]
#   [5 7 3]]

#  [[7 3 8]
#   [0 4 2]
#   [6 3 7]]]

# ------------------------------------------------------

# base

"""
import numpy as np
x=np.array([1,4,5,3,6,3,5,7,3,7,3,8,0,4,2,6,3,7])  #18 elements
y=x.reshape(2,3,3).base
print(y)
"""

#output
# [1 4 5 3 6 3 5 7 3 7 3 8 0 4 2 6 3 7]

# ---------------------------------------------------------------

# unknown dimension (-1)

#************ -1 is a automatic shaped array

"""
import numpy as np
x=np.array([1,4,5,3,6,3,5,7,3,7,3,8,0,4,2,6,3,7])  #18 elements
y=x.reshape(3,1,-1)
print(y)
"""

#output

# [[[1 4 5 3 6 3 5 7 3]]

 # [[7 3 8 0 4 2 6 3 7]]]
 
 
 
 
 # 3 dimention to 1 dimenstion


"""
import numpy as np
x=np.array([[[1,4,5],[3,6,3],[5,7,3],[7,3,8],[0,4,2],[6,3,7]]])  #18 elements
y=x.reshape(-1)
print(y)
"""

# output
# [1 4 5 3 6 3 5 7 3 7 3 8 0 4 2 6 3 7]



#------------------------------------------------------------------------

# ITERATING IN NUMPY  (return in function calling)

# 1 dimentional

"""
import numpy as np
x=np.array([1,2,3])  
for a in x:
    print(a)
"""
    
# output
# 1
# 2
# 3


# 2 dimentional

"""
import numpy as np
x=np.array([[1,2,3],[1,5,6]])
for a in x:
    print(a)
"""

# output
# [1 2 3]
# [1 5 6]


# 2 for loop using:(2 dim)

"""
import numpy as np
arr=np.array([[1,2,3],[1,5,6]])
for a in arr:
    for b in a:
        print(b)
"""

# output
# 1
# 2
# 3
# 1
# 5
# 6


# using 3 loops (3 dim)

"""
import numpy as np
arr=np.array([[[1,2,3],[1,5,6],[3,7,5]]])
for a in arr:
    for b in a:
        for c in b:
            print(c)
"""

# output
# 1
# 2
# 3
# 1
# 5
# 6
# 3
# 7
# 5


#*************************important******************************

# nditer()  --> function(keyword)

"""
import numpy as np
arr=np.array([[[1,2,3],[1,5,6],[3,7,5],[3,6,7]]])
for x in np.nditer(arr):
    print(x)
"""    
    
# output
# 1
# 2
# 3
# 1
# 5
# 6
# 3
# 7
# 5
# 3
# 6
# 7

# --------------------------------------------------------------------

# iterating a different datatyes

"""
import numpy as np
arr=np.array([1,2,3])    
for x in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):  # buffered--> to store a size datatypes(to store a certain a space)
    print(x)   # buffered --> garbage collectin (c,c++)   op_dtypes---> keyword
"""
    
# output
# b'1'
# b'2'
# b'3'


# 2 dimentional array

"""
import numpy as np
arr=np.array([[1,2,3],[1,5,6]])
for x in np.nditer(arr[:,: :2]):
    print(x)
"""

# output
# 1
# 3
# 1
# 6    

"""    
import numpy as np
arr=np.array([[1,2,3],[1,5,6],[5,7,2],[1,4,9]])
for x in np.nditer(arr[1:,0:2]):
    print(x)
"""

# output
# 1
# 5
# 5
# 7
# 1
# 4

#---------------------------------------------------------------------


# ENUMERATION ---> ndenumerate() -- function

"""
import numpy as np
arr=np.array([[1,2,3],[1,5,6],[5,7,2],[1,4,9]])
for x in np.ndenumerate(arr):
    print(x)
"""  
    
# output
# ((0, 0), 1)
# ((0, 1), 2)
# ((0, 2), 3)
# ((1, 0), 1)
# ((1, 1), 5)
# ((1, 2), 6)
# ((2, 0), 5)
# ((2, 1), 7)
# ((2, 2), 2)
# ((3, 0), 1)
# ((3, 1), 4)
# ((3, 2), 9)


# idx --> with out a bracket (print a id in x)
 
"""
import numpy as np
arr=np.array([[1,2,3],[1,5,6],[5,7,2],[1,4,9]])
for idx,x in np.ndenumerate(arr):
    print(x,idx)
"""  

# output
# 1 (0, 0)
# 2 (0, 1)
# 3 (0, 2)
# 1 (1, 0)
# 5 (1, 1)
# 6 (1, 2)
# 5 (2, 0)
# 7 (2, 1)
# 2 (2, 2)
# 1 (3, 0)
# 4 (3, 1)
# 9 (3, 2)


#-----------------------------------------------------


# ARRAY JOIN AND SPLIT


# ARRAY JOIN (concatenate())

# 1 dim

"""
import numpy as np
a=np.array([1,3,5,6])
b=np.array([4,3,6,2])
c=np.concatenate((a,b))
d=np.concatenate((b,a))
print(c)
print(d)
"""

# output
# [1 3 5 6 4 3 6 2]
# [4 3 6 2 1 3 5 6]


# 2 dim

"""
import numpy as np
a=np.array([[1,3],[5,6]])
b=np.array([[4,3],[6,2]])
c=np.concatenate((a,b),axis=1)
d=np.concatenate((b,a),axis=-1)
print(c)
print(d)
"""

# output
# [[1 3 4 3]
#  [5 6 6 2]]
# [[4 3 1 3]
#  [6 2 5 6]]


# STACK() --> function


"""
import numpy as np
a=np.array([[1,3],[5,6]])
b=np.array([[4,3],[6,2]])
c=np.stack((a,b),axis=1)
d=np.stack((b,a),axis=-1)
print(c)
print(d)
"""

# output
# [[[1 3]
#   [4 3]]

#  [[5 6]
#   [6 2]]]
# [[[4 1]
#   [3 3]]

#  [[6 5]
#   [2 6]]]


# hstack() --> print only rows(horizontal)

"""
import numpy as np
a=np.array([[1,3],[5,6]])
b=np.array([[4,3],[6,2]])
c=np.hstack((a,b))
d=np.hstack((b,a))
print(c)
print(d)
"""

# output
# [[1 3 4 3]
#  [5 6 6 2]]
# [[4 3 1 3]
#  [6 2 5 6]]


# vstack ---> print only columns(vertical)

"""
import numpy as np
a=np.array([[1,3],[5,6]])
b=np.array([[4,3],[6,2]])
c=np.vstack((a,b))
d=np.vstack((b,a))
print(c)
print(d)
"""

# output
# [[1 3]
#  [5 6]
#  [4 3]
#  [6 2]]
# [[4 3]
#  [6 2]
#  [1 3]
#  [5 6]]

# dstack() ----> print height (d-depth)

"""
import numpy as np
a=np.array([[1,3],[5,6]])
b=np.array([[4,3],[6,2]])
c=np.dstack((a,b))
d=np.dstack((b,a))
print(c)
print(d)
"""

# output
# [[[1 4]
#   [3 3]]

#  [[5 6]
#   [6 2]]]
# [[[4 1]
#   [3 3]]

#  [[6 5]
#   [2 6]]]

#-------------------------------

# SPLIT()

"""
import numpy as np
a=np.array([1,5,7,8,4,8,3,7,3,7,5,6,7])
b=np.array_split(a,5)
print(b)
"""

# output
# [array([1, 5, 7]), array([8, 4, 8]), array([3, 7, 3]),
#  array([7, 5]), array([6, 7])]


#split indexting

#1 dim

"""
import numpy as np
a=np.array([1,5,7,8,4,8,3,7,3,7,5,6,7])
b=np.array_split(a,5)
print(b[1])
c=np.array_split(a,3)
print(b[2])
"""

# output
# [8 4 8]
# [3 7 3]


#2 dim
"""
import numpy as np
a=np.array([[1,5,7],[8,4,8],[3,7,3],[7,5,6]])
b=np.array_split(a,5)
print(b[1])
c=np.array_split(a,3)
print(b[2])
"""

# output
# [[8 4 8]]
# [[3 7 3]]



#--------------------------------------------------------------


# NUMPY SEACHING ARRAY


# where()   ---> function

"""
import numpy as np
x=np.array([1,2,5,9,5,6,2,5,2])
y=np.where(x==2)
print(y)
"""

# output
# (array([1, 6, 8], dtype=int64),)

"""
import numpy as np
x=np.array([1,2,5,9,5,6,2,5,2])
z=int(input("hello -->"))
y=np.where(x==z)
print(y)
"""

# output
# hello -->2
# (array([1, 6, 8], dtype=int64),)


# print odd numbers position

"""
import numpy as np
x=np.array([1,2,5,9,5,6,2,5,2])
y=np.where(x%2==0)
print(y)
"""

# output
# (array([1, 5, 6, 8], dtype=int64),)


# print even numbers position 

"""
import numpy as np
x=np.array([1,2,5,9,5,6,2,5,2])
y=np.where(x%2==1)
print(y)
"""

# output
# (array([0, 2, 3, 4, 7], dtype=int64),)


# --------------------------------------------------


# searchsorted()   ---> method

"""
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
y=np.searchsorted(x,5)
print(y)
"""

# output
# 4



# which side searchsorted()

"""
import numpy as np
x=np.array([1,2,3,4,5,6,5,8,9])
y=np.searchsorted(x,5,side='right')
print(y)
"""

# output
# 7

# search multple values

"""
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
y=np.searchsorted(x,[2,5,8])
print(y)
"""

# output
# [1 4 7]


#----------------------------------------------------------------


 # SORTING ARRAY
 
 
# sorting numbers:
    
"""
import numpy as np
x=np.array([3,2,0,1,9,4])
print(np.sort(x))
"""

# output
# [0 1 2 3 4 9]



# sorting alphabets

"""
import numpy as np
x=np.array(['a','h','e','c','z','y','u','d'])
print(np.sort(x))
"""

# output
# ['a' 'c' 'd' 'e' 'h' 'u' 'y' 'z']


# sorting a boolean values

"""
import numpy as np
x=np.array([True,False,True,False,False])
print(np.sort(x))
"""

# output
# [False False False  True  True]



# 2 dim

"""
import numpy as np
x=np.array([[1,65,37,87,32],[3,5,33,8,90]])
print(np.sort(x))
"""

# output
# [[ 1 32 37 65 87]
#  [ 3  5  8 33 90]]

#----------------------------------------------------------------------

# FILTER()       (use amzon app filtering())
 
"""
import numpy as np
x=np.array([1,65,37,87,32])
y=[True,False,True,False,True]
new_x=x[y]
print(new_x)

"""

# output
# [ 1 37 32]


#******************important*****************************************


"""
import numpy as np
arr=np.array([1,65,37,87,32])
filter_arr=[]
for x in arr:
    if x>47:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
new_arr=arr[filter_arr]
print(filter_arr)
print(new_arr)
"""

# output
# [False, True, False, True, False]
# [65 87]

   # or

"""
import numpy as np
arr=np.array([1,65,37,87,32])
filter_arr=arr > 42
new_arr=arr[filter_arr]
print(new_arr)
print((filter_arr))
"""

# output
# [65 87]
# [False  True False  True False]



# conditons apply

# print odd numbers

"""
import numpy as np
arr=np.array([1,65,37,87,32,4,45,23])
filter_arr=arr%2==1
new_arr=arr[filter_arr]
print(new_arr)
print((filter_arr))
"""

# output
# [ 1 65 37 87 45 23]
# [ True  True  True  True False False  True  True]



# print even numbers

"""
import numpy as np
arr=np.array([1,65,37,87,32])
filter_arr=arr%2==0
new_arr=arr[filter_arr]
print(new_arr)
print((filter_arr))
"""

# output
# [32]
# [False False False False  True]



# ------------------------bacic array concepts finished-------------------



                # mathematic concepts in numpy


# RANDOM NUMBER IN NUMPY


# randint()  ---> integer values

"""
from numpy import random   #import random
x=random.randint(100)
print(x)
"""

#output
# 8
# 79
# 35


# rand  -----> floting values

"""
from numpy import random   #import random
x=random.rand()
print(x)
"""

# output
# 60
# 0.32311483027161225


# size=?   (online rummy games)

"""
from numpy import random   #import random
x=random.randint(100,size=5)
print(x)
"""

# output
# [94 65 90 56 75]



# 2-dim (ludo games)

"""
from numpy import random   #import random
x=random.randint(100,size=(3,6))
print(x)
"""

# output
# [[19 57  5 19 53 13]
#  [86 96 41 70 32 54]
#  [39  4 19 38 88 99]]


"""
from numpy import random   #import random
x=random.rand(4,5)
print(x)
"""

# output
# [[0.95522429 0.61405779 0.45165555 0.67927672 0.37684167]
#  [0.60411953 0.89825299 0.73428104 0.37444252 0.31315122]
#  [0.20774771 0.85570933 0.63214158 0.41426503 0.21956425]
#  [0.66448972 0.13263721 0.9612383  0.26409129 0.49918124]]



# choice()

"""
from numpy import random   #import random
x=random.choice([10,50,30,40,90,20,60])
print(x)
"""

# output
# 50
# 50
# 50
# 30
# 50


"""
from numpy import random   #import random
x=random.choice([10,50,30,40,90,20,60],size=(5,7))
print(x)
"""

# output

# [[90 90 40 20 90 30 50]
#  [30 90 20 10 40 20 10]
#  [60 60 10 40 20 90 60]
#  [90 30 90 40 40 90 90]
#  [10 40 20 30 20 20 90]]





#-------------------------------------------------------------------------

 # DATA DISTRIBUTION
 
 
# probability value is always 1.
#probability - p 
# p = 0 to 1  (can't here 1 or more value)

"""
from numpy import random
x=random.choice([3,2,6,5],p=[0.1,0.5,0.4,0.0],size=(80))
print(x)
"""

# 3--> 0.1
# 2--> 0.5
# 6--> 0.7
# 5--> 0.0
#     ------
#      1.0
#     ------


# output

# [2 2 2 6 2 6 6 6 2 2 6 6 2 6 6 6 6 2 3 2 6 2 6 6 2 6 2 2 2 2 6 2 2 2 3 6 6
#  6 6 2 2 6 6 6 6 6 2 2 6 3 2 2 2 2 3 6 2 2 6 2 2 3 2 2 2 3 6 2 2 6 6 2 6 2
#  2 6 3 6 2 6]


# probability more 1 (p>1) is a error

"""
from numpy import random
x=random.choice([3,2,6,5],p=[0.1,0.6,0.7,0.0],size=(80))
print(x)
"""

# output
#  error
#  because the prbability values is 0.1+0.6+0.7+0.0 = 1.4
#  p>1 is a error


"""
from numpy import random
x=random.choice([3,2],p=[0.1,0.6,0.7,0.0],size=(80))
print(x)
"""

#output 

# it is also an error ,because choice is only 2 elements but p is 4 values.


"""
from numpy import random
x=random.choice([3,2],p=[0.0,1.0],size=(80))
print(x)
"""

# output

# [2 6 6 6 6 2 2 6 2 2 2 6 2 2 6 2 6 2 6 2 2 6 6 3 6 3 2 6 2 2 2 2 2 6 6 6 6
#  6 6 3 6 2 6 6 6 3 2 2 2 6 6 2 6 6 2 6 6 2 2 2 2 3 6 6 2 6 2 2 6 6 2 2 2 2
#  2 6 2 3 2 6]
# [2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2]

"""
from numpy import random
x=random.choice([3,2,9,7],p=[0.3,0.3,0.3,0.1],size=(4,5))
print(x)
"""

# output


# [[2 3 3 9 9]
#  [3 3 2 3 9]
#  [3 2 9 9 3]
#  [2 9 9 7 7]]


#------------------------------------------------------------------------------



# NUMPY PERMUTATIONS:
    
# shuffle()

"""
from numpy import random
import numpy as np
x=np.array([1,2,3,4,5])
random.shuffle(x)       # shuffle --> function
print(x)
"""

# output
# [2 3 1 5 4]




# permutation()

"""
from numpy import random
import numpy as np
x=np.array([4,2,8,4,9,4,5])
random.permutation(x)
print(x)
"""

# output
# [4 2 8 4 9 4 5]   # here not shuffle



"""
from numpy import random
import numpy as np
x=np.array([4,2,8,4,9,4,5])
y=random.permutation(x)
print(y)
"""

# output
# [2 5 8 4 9 4 4]

"""
from numpy import random
import numpy as np
x=np.array([4,2,8,4,9,4,5])
y=random.permutation(x)
print(y)
print(x)
"""

# output
# [4 5 2 4 8 9 4]
# [4 2 8 4 9 4 5]


#------------------------------------------------------------------


#--------------------------------------------------------------------



#******************************SESABORN**************************

# it is a module
# it is depend on the module of matplot liabrary


#pyplot --> graphical represetation



"""
import seaborn as sb
import matplotlib.pyplot as plt

sb.distplot([0,1,2,3,4,5,6,7],hist=True)
plt.show()

""" 


#             Numpy mathematics


# normal distribution (gaussion distribution)
# (suit for probability)

# *********use for heart beat check,, IQ check***************


#       KEYWORDS

# loc --> mean  (1+2+3=6/3=>2)

# scale --> standard deviation( to find flat of plots)
# more details search this website ---> mathisfun.com

# size --> size of array


"""
from numpy import random
x=random.normal(loc=2,scale=3,size=(2,4))  # normal --> distribution
print(x)
"""

# output
# [[-1.24600756  4.23620474  3.08937355  2.34694159] 
#  [ 5.49987554  0.03933376  2.8440163   0.16256995]]

"""
import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random
sb.distplot(random.normal(loc=2,scale=3,size=(2,4)),hist=True)
plt.show()
"""

#--------------------------------------------------------------

# Binomial distribution (not a continous) , (head or tail) 

# keywords

# n --> number of trials
# p --> probability (chances)
# size --> size of array

"""
from numpy import random
x=random.binomial(n=10,p=0.7,size=(8))
print(x)
"""

#output
# [7 7 9 8 9 8 7 6]

"""
from numpy import random
x=random.binomial(n=1,p=0.7,size=(8))
print(x)
"""


# output
# [0 1 0 1 1 1 1 1]



"""
import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random

sb.distplot(random.binomial(n=1,p=0.6,size=20),hist=True)
plt.show()
"""


#-----------------------------------------------------------

# MULTINOMIAL distributions ( more than 2 possibilities)

# eg;  dice (6 sides)

# to find a ****** blood groups *******

# n - number of possible outcomes
# pvals - list probability values
# size - size of array

"""
from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6],size=1)
print(x)
"""

# output
# [[2 0 1 2 0 1]]

"""
from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)
"""

# output
# [1 0 2 1 1 1]

"""
from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6],size=10)
print(x)
"""

# output

#  [2 0 0 2 1 1]
#  [0 1 1 1 2 1]
#  [1 0 1 0 1 3]
#  [1 1 1 1 1 1]
#  [3 0 0 1 1 1]
#  [2 2 1 1 0 0]
#  [0 0 2 1 2 1]]

"""
from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6])
print(x)
"""

# output
# [1 1 4]   here n=6 so 1+1+4--> 6


"""
from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6])
print(x)
"""

# output
# [1 5]  # n=1+5-->6


"""
from numpy import random
x=random.multinomial(n=6,pvals=[1/6])
print(x)
"""

# output
# [6]     #n=6


# here n=6 , so >6 is a error



# **ludo gaming --> pvals--> machine learning


#------------------------------------------------------------------------------


# EXPONENTIAL DISTRIBUTION

#  use **share markets** 

# scale --> inverse rate ---> default valus is 1.0
# size --> size of array

"""
from numpy import random
x=random.exponential(scale=2,size=(3))
print(x)
"""

# output
# [0.17102283 0.40103994 1.07304743]  

"""
from numpy import random
x=random.exponential(scale=1,size=(6))
print(x)
"""

# output
# [1.06539746 2.06860866 0.95906927 0.58334545 0.36540519 1.7584306 ]

"""
from numpy import random
x=random.exponential(scale=3,size=(3,4))
print(x)
"""

# output

# [[0.53970168 0.42019691 2.62039074 1.92760811]
#  [0.179207   1.33562843 1.17813812 1.61533212]
#  [0.15612274 1.44360475 1.81902178 5.91936112]]

"""
import seaborn as sb
import matplotlib.pyplot as plot
from numpy import random
sb.distplot(random.exponential(scale=3,size=(3,4)),hist=True)
plot.show()
"""



#------------------------------------------------------------------------------------


# UNIFORM DISTRIBUTION ( uniform values (same))

# a- lower bound
# b- upper bound
# size - size of array

"""
from numpy import random
x=random.uniform(size=(3,4))
print(x)
"""

# output
# [[0.12695605 0.5436942  0.98769346 0.28167943]    =same values
#  [0.38194061 0.7911727  0.97121301 0.84258238]    =same values
#  [0.14403727 0.98930534 0.9586352  0.20360664]]   =same values


# here 3 set of values are same, so it is called uniform distribution

"""
from numpy import random
x=random.uniform(size=(3))
print(x)
"""

# output
# [0.58167992 0.02230162 0.14653693]

"""
import seaborn as sb
import matplotlib.pyplot as plot
from numpy import random
sb.distplot(random.uniform(size=(3,4)),hist=True)
plot.show()
"""



#-----------------------------------------------------------------------


# Logistic distribution (this is predict our datas)
# use of -- recursion , neural networks
# company funtd 40lakh ( logical thinking )

# loc - mean  (0.0)
# scale - standard deviation
# size - size of array

"""
from numpy import random
x=random.logistic(loc=2,scale=3,size=(2,4))
print(x)
"""

# output

# [[-2.79943083  0.48847099  2.78309164 -3.15573062]
#  [ 3.89299309 -1.21081671 -0.79016821 -3.1353253 ]]


"""
import seaborn as sb
import matplotlib.pyplot as plot
from numpy import random
sb.distplot(random.logistic(loc=2,scale=3,size=(2,4)),hist=True)
plot.show()

"""



#--------------------------------------------------------------------------------------


# POISSON DISTRIBUTION

# use of -- datas of daily activites


# lam - rate of occurance
# size - size of array


# eg; eating 3 times a day. so lam=3, chances = 10
"""
from numpy import random
x=random.poisson(lam=3,size=(10))
print(x)
"""

# output
# [4 2 1 1 4 4 2 5 5 2]


"""
import seaborn as sb
import matplotlib.pyplot as plot
from numpy import random
sb.distplot(random.poisson(lam=3,size=(10)),hist=True)
plot.show()
"""


#--------------------------------------------------------------------------------


#  UNIVERSAL FUNCTIONS IN NUMPY


# ufuns ---> run in ndarray

# important in machine learning

# vectorization --> process cpu faster (some kind of arithmetic operations)

# solve simple problems

# cpu normal work eg;
"""
x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=[]
for i,j in zip(x,y):  # zip --> when 2 values are used
    z.append(i+j)
print(z)
"""

# output
# [7, 9, 11, 13, 15]


# cpu faster using (numpy library)
# memory low space

"""
import numpy as np
x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=np.add(x,y)
print(z)
"""

# output
# [ 7  9 11 13 15]


#--------------------------------------------------------------------------


# creating a universal functions 


# using ---> frompyfunc

"""
import numpy as np
def myfunc(x,y):
    return x+y
myfunc=np.frompyfunc(myfunc,2,1)
# function --> myfunc , input --> 2 , output --> 1

print(myfunc([1,4,3,6,4],[3,6,4,8,6]))
"""

# output
# [4 10 7 14 10]    ----> 1 line output


"""
import numpy as np
def myfunc(x,y,z):
    return x+y-z
myfunc=np.frompyfunc(myfunc,3,1)
# function --> myfunc , input --> 3 , output --> 1

print(myfunc([1,4,3,6,4],[3,6,4,8,6],[1,6,9,4,6]))
"""

# output
# [3 4 -2 10 4]


"""
import numpy as np
def myfunc(x,y):
    return x+y
myfunc=np.frompyfunc(myfunc,2,1)
# function --> myfunc , input --> 2 , output --> 1

print(myfunc([1,4,3,6,4],[3,6,4,8,6]))
"""


# output
# [4 10 7 14 10]



#--------------------------------------------------------------------------



# arithmetic operations using universal functions

# Add()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
#z=x+y
z=np.add(x,y)
print(z)
"""

# output
# [ 7  9 11 13 15]



# subtract()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.subtract(x,y)
print(z)
"""

# output
# [-5 -5 -5 -5 -5]



# multiply()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.multiply(x,y)
print(z)
"""

# output
# [ 6 14 24 36 50]



# divide()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.divide(x,y)
print(z)
"""

# output
# [0.16666667 0.28571429 0.375      0.44444444 0.5]



# power()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.power(x,y)
print(z)
"""

# output
# [      1     128    6561  262144 9765625]


# remainder()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.remainder(x,y)
print(z)
"""

# output
#[1 2 3 4 5]


# or or or 

# mod()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.mod(x,y)
print(z)
"""

# output
#[1 2 3 4 5]


# print remainder and quotient values


# divmod()

"""
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.divmod(x,y)
print(z)
"""

# output
# (array([0, 0, 0, 0, 0]), array([1, 2, 3, 4, 5]))

 #   quotient             , remainder
 
 
 
 
 # absolute()

"""
import numpy as np
x=np.array([-1,2,-3,-4,5])
z=np.absolute(x)
print(z)
""" 
 
# output
# [1 2 3 4 5]
 
 
#-------------------------------------------------------------------------------------



# ufunctions using decimals (rounding)


# Truncation --> turnc()  and   fix()


# trunc() ---> to remove a decimal values:


"""
import numpy as np
x=np.trunc([-3.2334,6.3344])
print(x)
"""

# output
# [-3.  6.]


# fix()

"""
import numpy as np
x=np.fix([-3.2334,6.3344])
print(x)
"""

# output
# [-3.  6.]


#--------------------------------------------------------------------------


# rounding ---->  around()

# values <5 is a first values

# values >5 is a last values

"""
import numpy as np
x=np.around([3.99,6.33])
print(x)
"""

# output
# [4. 6.]


"""
import numpy as np
x=np.around([10.01,6.93])
print(x)
"""

# output
# [10.  7.]

# trunc() ---> its changes to integer values
# floor() ---> but floor can't change. it still floating values


#floor ---> floor()

"""

import numpy as np
x=np.floor([-1.800,5.545])
y=np.floor([9.345,7.545])
print(x)
print(y)

"""
# #output
# [-2.  5.]
# [9. 7.]


#----------------------------------------------------------------------

# ceil ---> ceil()


"""
import numpy as np
x=np.around([10.01,6.93])
print(x)
"""

#output
# [10.  7.]


#----------------------------------------------------------------------------


# to print our except decimal values

"""
import numpy as np
x=np.around([10.0144454,6.934545434],3)
print(x)
"""

# output
# [10.014  6.935]

"""
import numpy as np
x=np.around([10.0144454,6.934545434],5)
print(x)
"""

# output
# [10.01445  6.93455]

"""
import numpy as np
x=np.around([10.0144454,6.934545434],1)
print(x)
"""

# output
# [10.   6.9]



#---------------------------------------------------------------------------------


# numpy the End 

# lcm,gcd,trignometric, numpy cheat sheet pdf
# to know image procession 

# matplotlib, seaborn, AI


#---------------------------------------------------------------------------------

# face detection project


# numpy is very very important in project

# to find the object is rectangle or square

# square = h/w = 1  - 0.90 - 1.15
# rectangle 

#------------------------------------------------------------------------------------




