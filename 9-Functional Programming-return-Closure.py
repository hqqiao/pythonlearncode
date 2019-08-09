'''
返回函数-函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

一个函数可以返回一个计算结果，也可以返回一个函数。
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''
'''
可变参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple元组()
#可变参数实现，用*，可以实现“多个参数》tuple”，“tuple/list》多个参数”的转换
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数

'''
# 1-基础应用例，实现可变参数求和，返回和值
def calc_sum(*args):        # 可变参数args 在函数调用时自动组装成为tuple元组()
    ax = 0
    for x in args:
        ax += x
    return ax
print(calc_sum(1,2,3,4,5,6))    #21

# 2-返回求和函数
# 不需要立刻求和，在后面代码中根据需要再计算。
# 可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum

'''
在函数lazy_sum中又定义了函数sum，
内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种结构称为“闭包（Closure）”
闭包的本质就是嵌套定义，在函数内部再定义函数，将函数内部和函数外部连接起来。
闭包有两种不同的方式，在函数内部直接调用/返回一个函数名称
闭包作用——保存函数的状态信息，使函数的局部变量信息依然可以保存
闭包特性：被闭包函数引用的外层函数的参数以及局部变量会保存在内存中，直到闭包函数被销毁
'''

f = lazy_sum(1,2,3,4,5,6)
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print(f)
# 求和函数 <function lazy_sum.<locals>.sum at 0x0000020903355C80>
# 再调用f()后，才返回求和结果
print(f())
# 求和结果 21

# 在调用lazy_sum时，每次调用都会返回一个新的函数，与传入的参数是否一致无关。
# f1、f2、f3各个新函数之间的调用互不影响
f1 = lazy_sum(1,2)
f2 = lazy_sum(1,2,3)
f3 = lazy_sum(1,2)
print(f1,f1())
print(f2,f2())
print(f3,f3())
# <function lazy_sum.<locals>.sum at 0x00000221C8945C80> 3
# <function lazy_sum.<locals>.sum at 0x00000221C8945D08> 6
# <function lazy_sum.<locals>.sum at 0x00000221C8945D90> 3

'''
需要注意
（1）返回的函数在其定义内部引用了局部变量args，
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
所以，闭包用起来简单，实现起来可不容易
闭包特性：被闭包函数引用的外层函数的参数以及局部变量会保存在内存中，直到闭包函数被销毁
（2）返回的函数并没有立刻执行，而是直到调用了f()才执行
下面为示例程序：
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)    #每次循环（1,2,3）都创建一个新函数f，并把创建的3个函数都返回了。
    return fs

g1, g2, g3 = count()
print(g1,g1())
print(g2,g2())
print(g3,g3())
# <function count.<locals>.f at 0x00000261A8755EA0> 9
# <function count.<locals>.f at 0x00000261A8755F28> 9
# <function count.<locals>.f at 0x00000261A876B048> 9
# g1(),g2(),g3()结果全部都是9！原因就在于返回的函数引用了局部变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
'''
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：
'''
def count():
    def f(j):
        def g():
            return j*j
            # 把循环的部分单独再创建一个函数g()，用该函数的参数绑定循环变量j当前的值，
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值在平方后的数值被传入f()
    return fs
h1, h2, h3 = count()    # 把count()结果里的元素按顺序分别赋值给 h1 h2 h3.
print(h1,h1())
print(h2,h2())
print(h3,h3())
# <function count.<locals>.f.<locals>.g at 0x00000195B4A8A158> 1
# <function count.<locals>.f.<locals>.g at 0x00000195B4A8A1E0> 4
# <function count.<locals>.f.<locals>.g at 0x00000195B4A8A268> 9
'''
若内部作用域想修改外部作用域的变量，需要用到global和nonloacl关键字
修改全局变量需要用global关键字
修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量需要nonlocal关键字
'''
# 原始例子：
num = 1
def fun1():
    # print(num)    # 在不改变num作用域的情况下，在函数内使用num报错
    num = 123
    print('inner-num:',num)
fun1()
print('outer-num:',num)

# 运行结果如下：
# inner-num: 123
# outer-num: 1

# 用global修改num作用域
num = 1
def fun1():
    global num
    print('inner-num-1:',num)    # 通过global改变num作用域，可以在函数内使用num
    num = 123
    print('inner-num-2:',num)
fun1()
print('outer-num:',num)

# 运行结果如下：
# inner-num-1: 1
# inner-num-2: 123
# outer-num: 123

'''
练习:
利用闭包返回一个计数器函数，每次调用它返回递增整数
闭包特性:被闭包函数引用的外层函数的参数以及局部变量会保存在内存中，直到闭包函数被销毁

# -*- coding: utf-8 -*-
def createCounter():
    def counter():
        return 1
    return counter

# 提供测试程序:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 从测试程序看出 counterA是获得计数值的函数，每次调用得到逐一递增的计数值
所以createCounter()要返回一个计数器函数的实现，每次调用counter()得到累加值。
def createCounter():
    # ‘1’ 记录调用次数的变量
    def counter():
        # ‘2’每次调用累加计数变量  需要考虑变量作用域问题
        return 1    
    return counter
'''

# 使用yield迭代器
def createCounter():
    def interator():
        n = 0
        while True:
            n = n+1
            yield n
    f = interator()
    return f.__next__
    # 后面有对这个函数的调用，需要函数形式，所以这里返回函数名f.__next__ 而非函数值f.__next__()
    # counterA = createCounter0() print(counterA()）返回函数名

# 或者下面这么写也可以 返回函数名 counter而非 counter()函数值
def createCounter0():
    def interator():
        n = 0
        while True:
            n = n + 1
            yield n
    f = interator()
    def counter():
        return next(f)
    return counter

c = createCounter0()
print(c()) # 需要调用c，函数形式，所以上面的函数返回值均为函数名f.__next__，counter，而非函数值
print(c())
print(c())
# 使用global关键字
def createCounter1():
    global n
    n = 0
    def counter():
        global n
        n += 1
        return n
    return counter
# 使用nonloacl关键字
def createCounter2():
    n = 0           # n嵌套作用域 非全局作用域
    def counter():
        nonlocal n  # 修改n的作用域 用nonloacl关键字
        n += 1
        return n
    return counter

# # 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')