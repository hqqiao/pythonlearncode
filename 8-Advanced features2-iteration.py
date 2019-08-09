# -*- coding: utf-8 -*-
#迭代Iteration (可迭代的可遍历的)
'''
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环

只要是可迭代对象，无论有无下标，python都可以迭代/循环
如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

#python数据类型划分
#不可变数据（3个）：Number（数字）、String（字符串）、Tuple（有序元组()）；
#可变数据（3个）：List（有序列表[]）、Dictionary（字典{}）、Set（集合{}）。
只有Number不可迭代，其余五种类型均可迭代，for循环
'''
from collections import Iterable
print(isinstance('abc',Iterable))   #str字符串   True
print(isinstance((1,2,3),Iterable)) #tuple元组   True
print(isinstance(123,Iterable))     #整数Number  False


print(isinstance({'tom':1,'jack':2,'anna':3},Iterable)) #dict字典 True
print(isinstance({1,2,3},Iterable)) #set集合     True
print(isinstance([1,2,3],Iterable)) #list        True

'''
2--Iterable,collections模块的Iterable类型

---isinstance函数
判断两个类型是否相同推荐使用 isinstance()。
isinstance(object, classinfo)
参数：
object -- 实例对象。
classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
返回值：
如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False
'''
                 
                 
#字符串迭代
for ch in 'abc':
    print(ch)
#tuple迭代
for x in (11,22,33,'abc'):
    print(x)
    
#list迭代     #list里面的元素的数据类型可以不同,也可以是另一个list
for x in [1,[5,6],3,4,'a']:
    print(x)
#set 不允许有可变对象，因为无法排除重复，所以set里面不可以有list dict set,可以有str number tuple
for x in {1,2,3,(1,2,3),'b'}:
    print(x)
#dict迭代
'''
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
默认情况下，dict迭代的是key。
如果要迭代value，可以用for value in d.values()
如果要同时迭代key和value，可以用for k, v in d.items()
'''
d = {
'tom':1,
'jack':2,
'anna':3}
for x in d:   #默认情况下dict迭代key
    print(x)
for value in d.values():    #迭代value取值
    print(value)
for k,v in d.items():       #迭代items全部
    print(k,':',v)
    
'''
如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
'''
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
'''
0 A
1 B
2 C
'''

    
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))         #默认下标从0开始
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons,start = 1)))
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

for i,value in enumerate(seasons):
    print(i,value)
'''
0 Spring
1 Summer
2 Fall
3 Winter
'''

''' 
--enumerate函数，一般用在for循环当中。
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值 返回 enumerate(枚举) 对象。
'''
#上面的for循环里，同时引用两个变量，在Python里很常见，比如：

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
'''
1 1
2 4
3 9
'''
'''
练习
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L)==0:
        return(None,None)
    else:
        max = L[0]; min=L[0]
        for x in L:
            if x > max:
                max = x
            if x<min:
                min = x
        return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')