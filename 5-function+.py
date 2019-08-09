# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:46:28 2019

例：给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……平方和
"""
#函数参数系列二：可变参数*，允许一次性传入任意个参数，自动组装以元组tuple()形式存储。

#初始做法：由于参数个数不确定，可以把a，b，c……作为一个list或tuple传进函数做参数，
def calc(numbers):
    s = 0
    for x in numbers:
        s += x*x
    return s
#调用的时候，需要先组装出一个list或tuple，list或tuple的整体作为参数numbers的取值传入
print(calc([1,2,3]) )    #list
print(calc((1,2,3)) )    #tuple


# 改进做法：可变参数*
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple元组()

# 可变参数实现，用*，可以实现“多个参数》tuple”，“tuple/list》多个参数”的转换
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
    s =0
    for x in numbers:
        s += x*x
    return s
print(calc())
print(calc(1,2))    #在*numbers参数的情况下，自动接收到tuple,即calc(1,2)
#若已有list或者tuple，要调用其作为可变参数，可以通过*，把list或tuple的元素变成可变参数传进去
print(calc(*[1,2,3]))
nums = [1,2,3,4]
print(calc(*nums))  #*nums表示把nums这个list的所有元素作为可变参数传进去。



#函数参数系列三：关键字参数**，用于接收参数扩展，能够接收除去必选参数以外的可选项
#关键字参数允许你传入0个或任意个含参数名的参数，在函数内部会自动组装为一个dict字典{}

#关键字参数，可以扩展函数的功能。用**,实现“多个参数》dict”，“dict》多个参数”的转换
#比如，在person函数里，能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，也能收到，即可选项的功能
def person(name,age,**kw):                #函数person除必选参数name和age外，还接受关键字参数kw。
    print("name:",name,"age:",age,"other:",kw)
person("Tom",23)                    #在调用该函数时，可以只传入必选参数
person("jak",12,job="teacher")      #可以传入任意个数的关键字参数
person('Adam',45,gender='M',job='Engineer')

#也可以先组装出一个dict，然后，把该dict通过 ** 转换为关键字参数传进去：
extra ={"city":"beijing",
        "job":"teacher"
        }
person("anna",24,**extra)
print(extra)
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
'''

#关键字参数下，函数的调用者可以传入任意不受限制的关键字参数。
#至于到底传入了哪些，就需要在函数内部通过kw检查。仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw): 
    if 'city' in kw:        #检查是否有city这个参数
        pass
        #pass占位，定义一个空函数程序会报错，当没有想好函数的内容时可以用pass填充，使程序正常运行。
    if 'job' in kw:         #检查是否有job这个参数
        print("job is in ")
    print('name:',name,'age:',age,'kw:',kw)
person('Adam',45,gender='M',city = 'beijing',job='Engineer')        #但调用者仍可以传入不受限制的关键字参数



#函数参数系列四：命名关键字参数，用于限制关键字参数的名字（前有*或者前有可变参数（*eg），才能用）
#【使用命名关键字参数时，要特别注意，
#如果前面没有可变参数，就必须先加一个*作为特殊分隔符，再跟命名关键字参数。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数】

#要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
#需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def person(name,age,*,job,city):            #必选参数name，age；命名关键字参数job，city
    print('name:',name,'age:',age,'job:',job,"city:",city)
#调用方式，类似字典键值对写出命名关键字参数的键和值，必须传入参数名
person('Jack', 24, city='Beijing', job='Engineer')      

#如果前面已有可变参数（带*），则后面的参数自动认定为命名关键字参数
def person(name, age, *args, job, city):
    print (name, age, *args, job, city)
person('Jack', 24, (1,2,3), city='Beijing', job='Engineer')     #可变参数args取元组(1,2,3)，city和job为命名关键字参数
person('Jam', 21, [1,2,3], city='Nanjing', job='Engineer')      #可变参数args取列表[1,2,3]，city和job为命名关键字参数
#报错 person('Jam', 21, [1,2,3], city='Nanjing', job='Engineer',gender="F") 限制关键字参数的名字，只接收city和job作为关键字，gender报错








