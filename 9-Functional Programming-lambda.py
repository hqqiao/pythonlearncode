# 匿名函数
print(list(map(lambda x: x*x, [1, 2, 3, 4]))) # [1, 4, 9, 16]
'''
# map()函数接收两个参数，一个是函数名，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回,也就是一个惰性序列，
需要用list()函数获得所有结果并返回list，
即把f(x)作用在list的每一个元素并把结果生成一个新的list。
map()作为高阶函数，把运算规则抽象化，可以计算任意复杂的函数。
'''
def f(x):
    return x*x
print(list(map(f,[1, 2, 3, 4])))    # [1, 4, 9, 16]
'''
lambda x: x*x 实际上相当于 f(x)
关键字lambda表示匿名函数，冒号前面的x表示函数参数
匿名函数限制只能有一个表达式，不用写return，返回值就是该表达式的结果
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
匿名函数是一个函数对象，可以把匿名函数赋值给一个变量，再利用变量来调用该函数
也可以把匿名函数作为函数返回值返回
'''
g = lambda x:x*x
print(g)    # <function <lambda> at 0x000002085C4711E0>
print(g(3)) # 9

def build(x,y):
    return lambda : x*x+y*y     # 匿名函数作为函数返回值返回 是函数对象
h = build(1,2)  # h是函数对象
print('h=',h)
print('h()=',h())   # 调用lambda函数
# h= <function build.<locals>.<lambda> at 0x000001CFE16D5C80>
# h()= 5
'''
练习
请用匿名函数改造下面的代码：
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)
'''
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)
'''
# 和map()类似，filter(function,list)也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

# 需要注意filter()函数返回的是一个Iterator迭代器，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

filter()的作用是从一个序列中筛出符合条件的元素,使用惰性计算，
只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素
'''
L0 = list(filter(lambda x: x%2 == 1, range(1,20)))
print(L0)
L1 = list(filter(lambda x: x%2, range(1,20)))
# 偶数结果是0，0为假；奇数结果是1，非0为真
print(L1)

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]