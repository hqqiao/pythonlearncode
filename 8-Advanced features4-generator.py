# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:47:40 2019
#一边循环一边计算的机制，称为生成器：generator。
生成器可以在循环的过程中不断推算出后续的元素,不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
generator生成器实际保存的是算法，每次调用next(gen)，就计算出下一个元素的值，直到计算到最后一个元素，
没有更多的元素时，抛出StopIteration的错误。

定义generator的另一种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
"""
#list生成
L = [ x*x for x in range(0,10) ]
print('L:',L)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#generator生成
gen = ( x*x for x in range(0,10) )
print('gen:',gen)
#<generator object <genexpr> at 0x000001E6A8B99780>
#generator保存的是算法，每次调用next(gen)就进行一次运算，计算下一个元素的值
'''
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
generator保存的是算法，每次调用next(gen)，就计算出g的下一个元素的值，直到计算到最后一个元素，
没有更多的元素时，抛出StopIteration的错误。
'''
# print(next(gen))    #0
# print(next(gen))    #1
# print(next(gen))    #4
# print(next(gen))    #9
# print(next(gen))    #16
# print(next(gen))    #25
# print(next(gen))    #36
# print(next(gen))    #49
# print(next(gen))    #64
# print(next(gen))    #81
#print(next(gen))   #StopIteration，没有更多元素

'''
next()过于繁琐，正确的方法是使用for循环，因为generator和list一样，也是可迭代对象,可通过for循环迭代
创建一个generator后，基本上不会调用next()，而是通过for循环迭代，不需要关心StopIteration的错误。
'''
from collections import Iterable

gen = ( x*x for x in range(0,10) )
print( isinstance( gen, Iterable )) #True gen是可迭代对象
for x in gen:
    print('gen-x:',x)
    
L = [ x*x for x in range(0,10) ]
print( isinstance( L, Iterable )) #True L是可迭代对象
for x in L:
    print('L-x:',x)
'''    
0
1
4
9
16
25
36
49
64
81
'''
'''
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
在数学上，斐波纳契数列以如下被以递归的方法定义： 
F(0)=0 F(1)=1 F(n)=F(n−1)+F(n−2),(n≥2,n∈N)
斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
'''
print('---------函数实现Fibonacci---------')
def fib(max):
    n,a,b = 0,0,1;
    while(n<max):
        print('Fibonacci function-b:',b)        #在每次循环中打印出斐波拉契数列的当前值b
        a,b = b,a+b
        n = n+1
    return 'done'                               #fib函数本身返回值为 'done'

print('Fibonacci function fib:',fib(7))

'''
!!!!!!!注意----
赋值语句：
a, b = b, a + b
相当于：
t = (b, a + b)      # t是一个tuple
a = t[0]
b = t[1]
但不必显式写出临时变量t就可以赋值。

初始值：a =0,b=1;print(b)-1 
t(1,0+1) >   a=1 b=1;   print(b)-1 
t(1,1+1) >   a=1,b=2;   print(b)-2 
t(2,1+2) >   a=2,b=3;   print(b)-3 
t(3,2+3) >   a=3,b=5;   print(b)-5

fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

即定义generator的另一种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
'''
print('生成器实现Fibonacci')
def fib(max):
    n,a,b = 0,0,1;
    while(n<max):
        yield b             #生成器
        a,b = b,a+b
        n = n+1
    return 'done'
print('generator',fib(8))
# generator <generator object fib at 0x00000210A6DF4AF0>
f = fib(6)
print('f=',f)       #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是generator：
# f= <generator object fib at 0x00000210A6DF4AF0>

for x in fib(4):
    print(x)    #每次调用next()的时候执行迭代器生成x
'''
generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
generator函数举例如下：每次遇到yield语句就返回
'''
def odd():      # 生成器
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5
for i in odd():
    print(i)
'''
generator，在执行过程中，遇到yield就中断，下次又继续执行:

step1
1
step2
3
step3
5
'''
'''
小结
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

请注意区分普通函数和generator函数，普通函数调用直接返回结果：
>>> r = abs(6)
>>> r
6
generator函数的“调用”实际返回一个generator对象：
>>> g = fib(6)
>>> g
<generator object fib at 0x1022ef948>
'''


#补python赋值运算
#python的 a,b=b,a+b 和 a=b b=a+b 的区别（经典）
#赋值运算，先计算赋值号（也就是=号右边的，再赋值）
print('python赋值运算讲解：a,b=b,a+b')
n,a,b=0,0,1
while n<6:
    print(b)
    a,b=b,a+b
    n=n+1
#1 1 2 3 5 8
#a, b = b, a+b
#这种赋值，先计算等值 右边 就是 b=1 a+b=1，再赋值给a和b，那么 a=1, b=1，然后依次这样


print('python赋值运算讲解：a=b，b=a+b')
n,a,b=0,0,1
while n<6:
    print(b)
    a=b
    b=a+b
    n=n+1
#1 2 4 8 16 32
#a=b，此时b=1, 那么a=1，b=a+b，那么b=2

import dis
def func(a,b):
    a,b=b,a
    print(a,b)
a=10
b=20
func(a,b)
dis.dis(func)

'''
python交换两个值得方法非常简单，即a,b=b,a，一步操作就交换了两个值.python里面可以实现无临时变量的交换 
讲解链接：python——赋值与深浅拷贝 博客园  http://www.cnblogs.com/Eva-J/p/5534037.html
因为Python的变量并不直接存储值，而只是引用一个内存地址，交换变量时，只是交换了引用的地址。
程序输出：
20 10
125           0 LOAD_FAST                1 (b)
              3 LOAD_FAST                0 (a)
              6 ROT_TWO
              7 STORE_FAST               0 (a)
             10 STORE_FAST               1 (b)

126          13 LOAD_GLOBAL              0 (print)
             16 LOAD_FAST                0 (a)
             19 LOAD_FAST                1 (b)
             22 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             25 POP_TOP
             26 LOAD_CONST               0 (None)
             29 RETURN_VALUE
可以看出主要是ROT_TWO指令的功劳：
查阅python文档可以知道有ROT_TWO （源码1398行），ROT_THREE（源码1406行）， ROT_FOUR这样的指令，
可以直接交换两个变量、三个变量、四个变量的值
'''
