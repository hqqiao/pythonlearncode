#!/user/bin/python3

#1--python字符串,+连接,*重复,字符串从左开始0从右开始-1

str1 = 'Runoob'
print(str1)      # 输出字符串
print(str1[0:-1])# 输出第一个到倒数第二个的所有字符
#Python 中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
print(str1[0])   # 输出字符串第一个字符
print(str1[2:5]) # 输出从第三个开始到第五个前的字符  左闭右开原则。
print(str1[2:])  # 输出从第三个开始的后的所有字符
print(str1 * 2)  # *用于输出字符串两次
print(str1 + '你好')  # +用于连接字符串
print('------------------------------')
print('hello\nrunoob')  # 使用 反斜杠(\)+n  ，为转义特殊字符，换行
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，原样输出，不会发生转义

#2--input等待用户输入
input("\n\n按下enter键后退出")

#3--print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
#print默认输出换行
x = 'a'
y = 'b'
print(x)
print(y)
#在print语句的结尾加 end="" 输出不换行
print(x,end='')
print(y,end='')
print() #默认输出换行
print() #默认输出换行
print() #默认输出换行

#4--print和sys.stdout的区别
import sys
x = 'ruboot'
sys.stdout.write(x)         #stdout输出默认无换行，需要自己追加换行符\n
sys.stdout.write(x+'\n')

print(x)                    #python输出，调用sys.stdout的write方法并换行

"""
stdout与print 的区别
print将你需要的内容打印到了控制台，然后追加了一个换行符
print会调用sys.stdout的write方法并换行
下边两行结果是一样的：
sys.stdout.write('hello'+'\n')
print 'hello'
交互式命令行执行的输出结果为：
>>> print("hello")
hello
>>> import sys;sys.stdout.write("hello")
hello5
>>> import sys;sys.stdout.write("hello"+"\n")
hello
6
>>>
使用交互式命令行执行，输出结果如下，其中7为字符数
>>> import sys;x='ruboot';sys.stdout.write(x+"\n")
ruboot
7
"""
