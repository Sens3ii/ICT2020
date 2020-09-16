import math
n = float(input())
s = float(input())
pi = 3.14
n1 = (float(n/180))*pi
area = (n*(s**2))/(4*math.tan(float(pi/n1)))
print("area:",f'{area:.3f}')