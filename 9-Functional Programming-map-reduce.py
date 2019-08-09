from functools import reduce
'''
python内置了map()和reduce()
# map()函数接收两个参数，一个是函数名，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回,也就是一个惰性序列，
需要用list()函数获得所有结果并返回list，
即把f(x)作用在list的每一个元素并把结果生成一个新的list。
map()作为高阶函数，把运算规则抽象化，可以计算任意复杂的函数。
'''
# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
def f(x):
    return x*x
r = map(f,[1,2,3])    # “把f(x)作用在list的每一个元素并把结果生成一个新的list”
print('list(r)=',list(r))
print('r=',r)
# list(r)= [1, 4, 9]
# r= <map object at 0x0000028489D62E10>  r是map对象
print('list(map(str,[1,2,3,4,5]))=',list(map(str,[1,2,3,4,5])))
# list(map(str,[1,2,3,4,5]))= ['1', '2', '3', '4', '5']


'''
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
def f1(a,b):
    return a+b
print(reduce(f1,[1,2,3,4,5]))
# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

#如果考虑到字符串str也是一个序列，配合map()，我们就可以写出把str转换为int的函数
def fn(x,y):
    return  x*10+y
def char2num(s):
    # str转换成int
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]        # dict[key]=value 字典对应值
L = map(char2num,'123')
print('list(L)=',list(L))
print('fn(1,2)=',fn(1,2))
print('fn(12,3)=',fn(12,3))
n = reduce(fn,map(char2num,'123')) #累计计算
print('n=',n)

#写成一个大函数，即自定义的把字符串转化为整数的函数str2int
Digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def char2num1(s):
        return Digits[s]
    def fn1(x,y):
        return x*10+y
    # print('list(map(charm1, s))',list(map(char2num1, s)))      #[2, 3, 4, 5, 6, 7]
    return reduce(fn1,map(char2num1,s))
print("str2int('234567')", str2int('234567') )
# print('((((2*10+3)*10+4)*10+5)*10+6)*10+7=',((((2*10+3)*10+4)*10+5)*10+6)*10+7)
#  234567

# 使用lambda函数进一步优化代码
Digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num2(s):
    return Digits[s]
def str2int2(s):
    return reduce(lambda x, y: x*10+y, map(char2num2, s))
print("str2int2('12345')=", str2int2('12345'))


'''
Python title()方法
描述
Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
语法
title()方法语法：str.title();
返回值
返回"标题化"的字符串,就是说所有单词都是以大写开始。
'''

# 练习一：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.title()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print(list(map(lambda x: x.title(), ['adam', 'LISA', 'barT'])))

# 练习二：请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x*y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 练习三;利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    power = 0
    if '.' in s:
        print(s.index('.'))     #小数点在第几位
        power = len(s) - s.index('.') - 1
    integers = [digits[x] for x in s if x is not '.']
    return reduce(lambda x, y: x * 10 + y, integers) * 10**(- power)    #乘10的负power次方，化为浮点数

print('str2float(\'123.456\') =', str2float('123.456'))


 #练习1
 # -*- coding: utf-8 -*-
def normalize(name):
    L=name[0].upper()+name[1:].lower()
    return L

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 练习3
from functools import reduce
def str2float(s):
    for i in range(len(s)):
        if s[i]=='.':
            break
    L=s[:i]+s[i+1:] #把小数点去掉
    m=len(s)-i-1   #小数点在第几位
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def f(x,y):
        return x*10+y
    def char2num(s):
        return dic[s]
    return reduce(f,map(char2num,L))/10**m

print('str2float(\'123.456\') =', str2float('123.456'))


def str2floatlearn(s):

    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    s1,s2 = s.split('.')    #用.分隔开s1，s2
    return reduce(lambda x,y : x*10+y, map(lambda x:digits[x], s1+s2)) / (10**len(s2))
print('str2floatlearn(\'123.456\') =', str2floatlearn('123.456'))