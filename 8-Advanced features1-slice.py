# -*- coding: utf-8 -*-
#1-构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
L =[]
n =1
while n<=99:
    L.append(n)
    n+=2
print(L)

#2-取一个list或tuple的部分元素
#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
'''
python range()函数可创建一个整数列表，一般用在for循环中。
函数语法 range(start, stop[, step])
参数说明：
start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
stop:计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step:步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
#方法一：循环取值
r = []
n = 3
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
for i in range(n):
    r.append(L[i])
print(r)
#方法二：切片[起始:终止前:间隔几个]
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。
#即索引0，1，2，正好是3个元素。
#如果第一个索引是0，还可以省略，L[:3]

r=L[0:]     #从索引0开始直到最后 ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(r)    
r=L[0:4]    #从索引0开始，0,1,2,3共4个 ['Michael', 'Sarah', 'Tracy', 'Bob']
print(r)

#同样支持倒数切片 从右边开始为-1
r=L[-4:-1]  #从-4开始，到-1为止但不包括索引-1,['Sarah', 'Tracy', 'Bob']
print(r)
r=L[-5:]    #从-5即最开始的Michael开始，直到所有，即后五个数
print(r)

'''
切片操作总结：
[start:stop:step]
a = [0,1,2,3,4,5,6,7,8,9]
b = a[i:j] 表示复制a[i]到a[j-1]，以生成新的list对象
b = a[1:3] 那么，b的内容是 [1,2]
当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
当i,j都缺省时，a[:]就相当于完整复制一份a了

b = a[i:j:s]，s表示步进，缺省为1.
a[i:j:1]相当于a[i:j]
当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍,即全部倒序复制
上述例子为 a[-1:-11:-1]
'''
a = [0,1,2,3,4,5,6,7,8,9]
print('a[-1:-11:-1]',a[-1:-11:-1])
# a[-1:-11:-1] [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


#切片应用举例[start:end:interval] list/tuple/string
'''
在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring）
其实目的就是对字符串切片。
Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单

本例总结代码经验：
出现'list' object is not callable错误的原因
通常都是因为在之前定义了与函数名称相同的变量，导致在调用函数时报错。
但重复定义的不一定是list，有可能是其他函数名
在命名变量时要注意，应避免和python的函数名、关键字冲突。
'''


s = list(range(100))
print(s)
print(s[:10])   #前十个数
print(s[-10:])  #倒数十个数
print(s[10:20:2])   #前11-20个数,每两个取一个：
print(s[::5])       #所有数，每五个取一个
print(s[:])         #直接全部复制一个list

'''
tuple也是一种list，唯一区别是tuple不可变。
因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
>>> (0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
因此，字符串也可以用切片操作，只是操作结果仍是字符串：
>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[::2]
'ACEG'
'''
a = (0,1,2,3,4,5)
b = a[:3][:1]
print(b)   
#(0,) 可以连续两次切片，从而得到只含一个元素的元组。

c = 'ABCDEFG'
d = c[::2]
print(d)

'''
练习：利用切片操作，实现一个trim()函数，去除字符串首尾的空格
注意不要调用str的strip()方法：
'''


# -*- coding: utf-8 -*-
def trim(s):
    
    while s[0:1]==" ":  #首部有空格,每次检查一个字符，依次向后
        s=s[1:]
    while s[-1:]==" ":  #尾部有空格，每次检查一个字符，依次向前
        s=s[0:-1]    
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
