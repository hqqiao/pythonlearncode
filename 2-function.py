# -*- coding: utf-8 -*-
#定义空函数
def nop():
    pass
#自定义函数+参数数据类型检查
def my_abs(x):
    '''
    isinstance() 函数来判断一个对象是否是一个已知的类型。
    isinstance(object, classinfo)
    object -- 实例对象。
    classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
    返回值:如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。
    '''
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    #python标准异常之TypeError，对类型无效的操作
    #触发异常--可以使用raise语句自己触发异常
    #raise语法格式：raise [Exception [, args [, traceback]]]
    #Exception是异常的类型，args是自已提供的异常参数。
    #触发异常后，后面的代码就不会再执行
    if x >= 0:
        print(x)
    else:
        print(-x)
my_abs(1)       #1
my_abs(-1)      #1
#print(my_abs("a"))  #输出TypeError: bad operand type

#多个返回值
import math
#导入math包，后续使用数学的一些函数cos、sin
def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return (nx,ny)
r= move(100, 100, 60, math.pi/6)
print(r)
#由输出可见python函数的多个返回值形成一个元组tuple

#函数总结
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
#定义函数时，需要确定函数名和参数个数；
#如果有必要，可以先对参数的数据类型做检查；
#函数体内部可以用return随时返回函数结果；
#函数执行完毕也没有return语句时，自动return None。
#函数可以同时返回多个值，但其实就是一个tuple。