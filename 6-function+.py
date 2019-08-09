# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:14:17 2019
函数参数系列总结：参数组合 
虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
在Python中定义函数，参数都可以组合使用。
但参数定义的顺序必须是：必选参数、默认参数、可变参数(*)(N+多)、命名关键字参数和关键字参数(**)(N+多)。

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数。args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""

def f1(a,b,c=0,*args,**kw):         #必选，必选，默认，可变*()，关键字**{}
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):      #必选，必选，默认,命名关键字（前有*）,关键字**{}
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


#f1可变参数和关键字参数为空时，显示()和{}，默认参数显示0
f1(1,2)            
f1(1,2,3)      
#必选和默认参数后，关键字参数前，均为可变参数()，元组存储；关键字{name:'jom'}字典型存储     
f1(1,2,3,1,2,3,4,  name='jom')      
f1(1,2,3,(1,2,3,4),name='jom')     #此处(1,2,3,4)作为元组中的一个元素((1,2,3,4),)
#只有1个元素的tuple定义时必须加一个逗号,消除歧义;
#Python在显示只有1个元素的tuple时，也会加一个逗号,因此输出显示是((1,2,3,4),)
f1(1,2,3,('a','b'),('c','d'),gender='F')



#f2中参数d为命名关键字(前有*)必须给出相应的键值对 d=……
#例f2(1, 2) TypeError: f2() missing 1 required keyword-only argument: 'd'
f2(1, 2, d=99)  #调用f2所需的最少参数为3个 a b d
f2(11,22,33,d='jam',name='anna',job='teacher')     
f2(11,22,33,d=22,   name='anna',job='teacher')      #kw为关键字参数，通过键值对进行传值


'''
可以通过元组()和字典{}来调用函数
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
'''

#f1(a,b,c=0,*args,**kw)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

#f2(a, b, c=0, *, d, **kw) 
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
args = (1,2,3)
kw = {'d':'deadline','name':'tom','age':23 }
f2(*args, **kw)



'''
练习
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
    return x * y
'''
def product(*x):
    print(*x)
    if len(x) == 0:
       raise TypeError('参数为空')
    s = 1
    for i in x:
        s *= i
    return s

#测试
#print('product() =', product())
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
        