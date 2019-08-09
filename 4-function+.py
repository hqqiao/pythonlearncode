# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:41:40 2019
"""
#函数参数系列一：默认参数(必须指向不变对象)
#默认参数可以简化函数的调用。设置默认参数,可以降低函数难度
#一是必选参数在前，默认参数在后
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print("power(2)=",power(2))
print("power(2,4)=",power(2,4))
print("power(2,4)=",power(2,n=4))

'''
默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
无论是简单调用还是复杂调用，函数只需要定义一个。
有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数。
比如调用enroll('Bob', 'M', 7)，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
当不按顺序提供部分默认参数时，需要把参数名写上。
比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
'''
def enroll(name,gender,age=6,city='beijing'):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)
    
enroll("anna","female")
enroll("jam","male",7,"nanjing")




#定义默认参数要牢记一点：默认参数必须指向不变对象！
#不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
#此外，由于对象不变，多任务环境下同时读取对象不需要加锁，顺利读取。
def add_end(L = None):
    if L is None:
        L = []
    L.append("END")
    return L
print(add_end([1])) 
print(add_end())
print(add_end())
print(add_end())

#反例 默认参数为list可变对象，数据修改错误
def add_end(L =[]):
    L.append("END")
    return L
print(add_end([1])) #在有参数的情况下正常
#默认参数L变量指向[]的可变对象，每次调用若改变L内容，则下次调用时，默认参数的内容改变，不再是定义时的[]了。
print(add_end())
print(add_end())
print(add_end())    
