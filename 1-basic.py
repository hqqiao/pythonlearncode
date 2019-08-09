"""
理解变量在计算机内存中的表示
https://www.liaoxuefeng.com/wiki/1016959663602400/1017063826246112
Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，
而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。
"""
a = 'ABC'
print(a)
b = a
print(b)
a ="XYZ"
print(a,b)

#b=ABC a=XYZ
#因为a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
#执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC'：
#执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：


##选择语句，条件判断
age = int(input("birth:"))
#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。
#Python提供了int()函数来完成这件事情
if age >= 18:
    print("your age is",age,"adult")
elif age < 6:
    print("your age is",age,"child")
else:
    print("your age is",age,"teenager")

  
'''
python range()函数可创建一个整数列表，一般用在for循环中。
函数语法 range(start, stop[, step])
参数说明：
start:计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop:计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step:步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
#求和0+……+100，,5050
sum = 0
for x in range(101):
    sum = sum+x
print(sum)

#输出1-10        
n = 1
while n<100:
    if n >10:
        break
    print(n)
    n=n+1
print("end")

#输出10以内的奇数
n = 0
while n<10:
    n = n+1
    if(n%2==0):
        continue
    print(n)
print("end")

print("-------dictionary-------")
#python数据类型划分
#不可变数据（3个）：Number（数字）、String（字符串）、Tuple（有序元组()）；
#可变数据（3个）：List（有序列表[]）、Dictionary（字典{}）、Set（集合{}）。    
'''
##字典 使用键-值（key-value）存储，具有极快的查找速度，dict的key必须是不可变对象。
#字典{}无序保存，其key要求必须为不可变对象；list[]列表有序保存且list可改变，不能作为key

和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
'''
dict ={
       "tom":12,
       "jack":13,
       "anna":23
}    
#字典创建用{}大括号
dict["lucky"]=22
dict["alen"]=24
print(dict)
print("anna" in dict)   #判断某个键是否在字典集中
print(dict.get("tom"))  #读取字典中键值对的数据

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
#转义字符输出''
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])

#Python字典(Dictionary) get()函数返回指定键的值，如果值不在字典中返回默认值。
#语法：dict.get(key, default=None)
#参数：key是字典中要查找的键。default是在指定键的值不存在时，返回该默认值。
#返回值：返回指定键的值，如果值不在字典中返回默认值None。
print('d.get(\'Thomas\') =', d.get('Thomas'))
print('d.get(\'Bob\') =', d.get('Bob', 'none'))
print(d)

#要删除key，用pop(key)方法，对应的value也会同时删除
d.pop('Michael')
print(d)


print("-------set-------")
#set相当于数学上的集合，可进行交并补等集合运算，成员关系测试和删除重复元素，用花括号{}
'''
set可以看成数学意义上的无序和无重复元素的集合
set和dict的唯一区别仅在于没有存储对应的value
但set的原理和dict一样，所以，同样不可以放入可变对象
因为无法判断两个可变对象是否相等，无法保证set内部“不会有重复元素”。
set 不允许有可变对象，因为无法排除重复，所以set里面不可以有list dict set,可以有str number tuple
'''
ss = {1,2,3,(1,2,3),'b'}
print(ss)

s = set([1, 2, 3, 4, 5, 2])      #创建一个set，需要提供一个list作为输入集合
print(s)        #删除重复元素,显示的{1,2,3,4,5}只说明这个set内部有5个元素，显示的顺序也不表示set是有序的。。
s.remove(1)     #add()和remove()，增加+删除集合中的元素
s.add(6)
print(s)   

s1 = set([1,2,3,4])
s2 = set([2,3,4,5])
print("s1&s2:",s1&s2)
print("s1|s2:",s1|s2)


print("-------list-------")
#list列表，list是一种有序的集合，可以随时添加和删除其中的元素。用len()函数可以获得list元素的个数

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
L = len(classmates)
print(L)
#索引 左起0右起-1
print(classmates[0],classmates[1],classmates[2])
print(classmates[-1],classmates[-2],classmates[-3])
#st是一个可变的有序表，可以往list中对元素进行增删改查
classmates.append('Adam')   #“增”在list最后追加元素 append(xxx)
print(classmates)          
classmates.insert(1,'Tom')  #“增”在指定位置插入元素 insert(xx, xx)
print(classmates)
classmates.pop()    #“删”删除最末尾元素 pop()
print(classmates)
classmates.pop(1)   #“删”删除指定位置的元素，用pop(i)方法，其中i是索引位置
print(classmates)
classmates[1]='Jack' #"改"修改指定位置的元素
print(classmates)
#list里面的元素的数据类型可以不同,也可以是另一个list
q = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(q))       #q只有4个元素，其中q[2]又是一个list
#相当于两个list分开写
p = ['asp','php']
s = ['python','java',p,'scheme']
if p[1] == s[2][1]:
    print('same:',p[1],s[2][1])
#空list长为0
L=[]
print(len(L))


print("-------tuple-------")
##tuple 有序元组，一旦创建不可更改，不能和list一样增删改查
#因为tuple不可变，所以代码更安全。能用tuple代替list[]就尽量用tuple()。
classmates = ('Michael', 'Bob', 'Tracy')
#定义一个空的tuple
t = ()
print(t)    #(),空元组
#定义一个只有1个元素的tuple,下示反例：
t = (1)
print(t)    #1
#结果是1，定义的不是tuple，是1这个数！
#这是因为括号()既可以表示tuple，又可以表示数学公式中小括号，产生歧义
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,消除歧义;Python在显示只有1个元素的tuple时，也会加一个逗号
t = (1,)
print(t)    #(1,)

#“可变”的tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
print(t) 
t[2][1] = 'Y'
print(t)       #('a', 'b', ['X', 'Y'])
#tuple不可变是指tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#所以，要想创建一个内容也不变的tuple就必须保证tuple的每一个元素本身也不能变