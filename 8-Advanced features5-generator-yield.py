#yield 生成器讲解——廖雪峰教程
#Python yield 使用浅析  https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
#斐波那契（Fibonacci）数列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
#一般写法
def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fab1(5)
#用yield迭代器形式
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
for n in fab(8):
    print(n)
'''
yield 的作用就是把一个函数变成一个 generator生成器，带有 yield 的函数不再是一个普通函数，
Python解释器会将其视为一个generator，调用fab(8)不会执行fab函数，而是返回一个iterable对象！
在for循环执行时，每次循环都会执行fab函数内部的代码，执行到yield b时，fab函数就返回一个迭代值，
下次迭代时，代码从yield b的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到yield。

一个带有 yield 的函数就是一个 generator生成器，它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，代码简洁，而且执行流程清晰。
'''
# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
# 清单 7. 使用 isgeneratorfunction 判断
from inspect import isgeneratorfunction
print(isgeneratorfunction(fab))
# True
# 要注意区分 fab 和 fab(5)，fab 是一个 generator function，而 fab(5) 是调用 fab 返回的一个 generator，好比类的定义和类的实例的区别：
# 清单 8. 类的定义和类的实例
import types
print(isinstance(fab, types.GeneratorType))
# False
print(isinstance(fab(5), types.GeneratorType))
# True
# fab 是无法迭代的，而 fab(5) 是可迭代的：
