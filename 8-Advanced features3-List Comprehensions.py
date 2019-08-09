# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:32:17 2019
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
"""
#example:生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
s=list(range(1,11))
print(s)

#生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
#法一：循环
l=[]
for x in range(1,11):
    l.append(x*x)
print(l)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#法二:列表生成式
#写列表生成式时，把要生成的元素x*x放到前面，后面跟for循环，就可以把list创建出来
d = [x*x for x in range(1,11)]
print(d)    
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
e = [x*x for x in range(1,11) if x%2 ==0]
print(e)
#[4, 16, 36, 64, 100]

#还可以使用两层循环，可以生成全排列
# + 是字符串连接，m+n的连接方法有3*3=9种
f = [m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print(f)

'''
运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录


os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
这个列表以字母顺序。它不包括'.'和'..'即使它在文件夹中
listdir()方法语法格式如下：
os.listdir(path)
参数
path -- 需要列出的目录路径
返回值
返回指定路径下的文件和文件夹列表。

'''
import os
h = [d for d in os.listdir('.')]    #列出当前的文件和目录
print(h)


#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, ":", v)
#所以列表生成式也可以同时使用两个变量生成list
f=[k +':'+ v for k ,v in d.items()]
print('f:',f)

'''
Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
items()方法语法：
dict.items()
参数:NA。
返回值:返回可遍历的(键, 值) 元组数组。
'''

#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
j = [b.lower() for b in L]
print(j)
'''
Python lower() 方法转换字符串中所有大写字符为小写。
lower()方法语法：
str.lower()
'''



'''
练习
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
使用内建的isinstance函数可以判断一个变量是不是字符串：

>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]       
#str类型会使isinstance返回True，if条件成立 执行字母小写化
 
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
