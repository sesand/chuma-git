
                        # MATH MODULE
 
                   
import math
#print(dir(math))

"""
#output

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 
 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 
 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 
'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin',
'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
"""
"""

a=56.7

# FLOOR()

result=math.floor(a)
print(result)

#output
#56

#  CEIL()

result=math.ceil(a)
print(result)

#output
#57

"""

# FACTORIAL   3!--> 2*3=6

print(math.factorial(3))

#output
#6

# GCD

print(math.gcd(2,8))

#output
#2

# SQUARE ROOT

print(math.sqrt(2))  #floating value

#output
#1.4142135623730951

print(math.isqrt(2)) #int 

#output
#1

# EXPONENTIAL
# e^val

print(math.exp(3))

#outuput
#20.085536923187668

#modulo function

print(math.fmod(10,3))  #fmod  --> x>y then return reminder

#output
#1.0

print(math.fmod(3,10))  #---> x<y then return x

#output
#3.0


# COPY SIGN

x=10
y=-20
print(math.copysign(y,x))
print(math.copysign(x,y))  #copy of y sign to x val

#output
#20.0
#-10.0


# DIFFERENCE

print(4-5)

#output
#-1


# FABS

print(math.fabs(x-y))

#output
#30.0

x=9
y=6

print(math.fabs(x-y))

#output
#3.0


# POWER

print(math.pow(2,6))

#output
#64.0


#                   LIST ACCESS IN MATH

# FSUM()

l_st=[1,2,4,5,7]
print(math.fsum(l_st))   # add tha values in list


#output
#19.0


# PRODUCT

print(math.prod(l_st))
print(math.prod(l_st,start=3)) # 240*3=840 

#output
#280
#840


# COSTANT

# PI

print(math.pi)

#output
#3.141592653589793

# TAU

print(math.tau)

#output
#6.283185307179586

print(math.e)  # EXPONENTIAL VALUE

#output
#2.718281828459045

print(math.nan)  # not a number

#output
#nan

print(math.inf)   # infinity

#output
#inf


#CONSTANT IMPLEMENT

x=10
print(math.isfinite(x))
print(math.isinf(x))
print(math.isnan(x))


#output
#True
#False
#False


# isclose()

print(math.isclose(1.2,1.5)) #min 0.0 to max diff=0.1
print(math.isclose(0.1,0.2))
print(math.isclose(0.0,0.0))

#output
#False
#False
#True

print(math.isclose(1.1,1.2,abs_tol=0.2)) #0.0  diff=0.2
print(math.isclose(1.1,1.6,abs_tol=0.2)) #0.0  diff=0.2

#output
#True
#False



