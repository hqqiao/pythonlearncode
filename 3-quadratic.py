# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:20:05 2019

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
提示：计算平方根可以调用math.sqrt()函数：
>>> import math
>>> math.sqrt(2)
1.4142135623730951
"""
import math
def quadratic(a,b,c):
    if not isinstance((a+b+c),(int,float)):
        raise TypeError('bad operand type')
    s =b*b-4*a*c
    if(a==0):
        x1 = x2 = (-c)/b
        return x1,x2
    elif(s<0):
        print("None")
    elif(s==0):
         x1=x2=((-b)+math.sqrt(s))/(2*a)
         return x1,x2
    else:
        x1= ((-b)+math.sqrt(s))/(2*a)
        x2= ((-b)-math.sqrt(s))/(2*a)
        return x1,x2

print("quadratic(1, 2, 1) =", quadratic(1, 2, 1))  
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(2, 9, 4) =', quadratic(2, 9, 4))
print('quadratic(1, 3,-4) =', quadratic(1, 3,-4))
#print("quadratic('a','b','c')=",quadratic('a','b','c'))
#参数检查显示异常 TypeError: bad operand type
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
    
    
    
    