def now():
    print('2019-8-7')
f = now # 函数对象now赋值给变量f
f()     # 通过变量f调用函数now  # 2019-8-7
'''
# 函数也是对象，且函数对象可以被赋值给变量，
# 所以可以通过变量调用函数

# 函数对象有name属性，可以拿到函数的名字
'''
print(now.__name__)  # now
print(f.__name__)    # now
'''
若要增强now()函数的功能，比如在函数调用前后自动打印日志，
但又不希望修改now函数的定义
这种在函数运行期间动态增加功能的方式，称为“装饰器Decorator”
本质上，decorator就是一个返回函数的高阶函数。
decorator接受一个函数做参数，并返回一个函数
'''
def log(func):      # 装饰器log接受一个函数func做参数，返回函数wrapper
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        # func.__name__ 打印参数func函数的名字
        return func(*args,**kw)
    return wrapper
'''
python格式化输出——  %字符：标记转换说明符的开始
%s是一种字符串格式化的语法，基本用法是将值插入到%s占位符的字符串中。
%s,表示格式化一个对象为字符            
'''
string = "good"  # 类型为字符串
print("string=%s" % string)   # 输出的打印结果为 string=good
pi = 3.141592653
print('%10.3f' % pi) # 字段宽10，精度3  3.142(占10个字符的宽度)
'''
*args
#可变参数*
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple元组()
#可变参数实现，用*，可以实现“多个参数》tuple”，“tuple/list》多个参数”的转换
**kw
关键字参数**，用于接收参数扩展，能够接收除去必选参数以外的可选项
#关键字参数允许你传入0个或任意个含参数名的参数，在函数内部会自动组装为一个dict字典{}
#关键字参数，可以扩展函数的功能。用**,实现“多个参数》dict”，“dict》多个参数”的转换
'''

# 借助python的@语法，把decorator置于函数的定义处
@log
def now():
    print('2019-8-7')
now()   # 调用now函数，不仅运行now函数本身，还会在运行now()函数前打印一行日志
# call now():
# 2019-8-7

# 上面46-52行把decorator置于函数的定义处，相当于执行语句：
now = log(now)
now()
# 输出结果为：
# call wrapper():
# call now():
# 2019-8-7
'''
由于log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''