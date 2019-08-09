# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:01:17 2019
阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
所以，fact(n)可以表示为n * fact(n-1)，只有n=1时需要特殊处理
"""
#阶乘运算
def fact(x):
    if x==1:
        return 1
    return x *fact(x-1)
print(fact(4))
print(fact(5))
#print(fact(1000))       #栈溢出，RecursionError: maximum recursion depth exceeded in comparison

'''
使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
>>> fact(1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: maximum recursion depth exceeded in comparison
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
'''
#return fact_iter(num-1,num*product)仅返回递归函数本身
#num-1和num*product在函数调用前就会被计算，不影响函数调用。
def  fact(x):
    return fact_iter(x,1)
    
def fact_iter(num,products):
    if num==1:
        return products
    return fact_iter(num-1,num*products)

print(fact(3))
print(fact(4))
print(fact(5))

#   n=int(input("numbers:"))
#   print(fact(n))

'''
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

小结
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
针对尾递归优化的语言可以通过尾递归防止栈溢出。
尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''

'''
练习
汉诺塔的移动可以用递归函数非常简单地实现。
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法，例如：
# -*- coding: utf-8 -*-
def move(n, a, b, c):

    if n == 1:
        print(a, '-->', c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
汉诺塔问题是源于印度一个古老传说的益智玩具，三根柱子A、B、C，在A柱子上从下往上按照大小顺序摞着N片黄金圆盘，现需将所有圆盘转移到C柱上。
规定：小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
#无论多少个圆块，可以抽象成为同一套思路：
想办法把(n-1)个a柱上的圆块先移动到b柱，
然后把最底部最大的一个圆块移动到c柱，
最后把b柱上的(n-1)个圆块移动到c柱
'''

def move(n, a, b, c):
    if not isinstance(n,int):
        raise TypeError('n must be integer')
    if n == 1:
        print(a, '-->', c)  #定义从a移动到c的操作
   
    elif n > 1: 
        move(n-1,a,c,b) #把(n-1)个a柱上的圆块先移动到缓冲区b柱
        move(1,a,b,c)   #把a柱底部最大的一个圆块移动到c柱 #move(1,a,b,c)即为 print(a, '-->', c)
        move(n-1,b,a,c) #最后把b柱上的(n-1)个圆块移动到c柱
    else:
        raise TypeError('n must be greater than 0')


move(5, 'A', 'B', 'C')
print('*************')
move(4, 'A', 'B', 'C')
print('*************')
move(3, 'A', 'B', 'C')
print('*************')
move(2, 'A', 'B', 'C')
print('*************')
move(1, 'A', 'B', 'C')


#1,3,7,15,31
#次数为2^n-1,n=(1,2,3,4……)
        