# Python内置的sorted()函数对list进行排序
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
print(sorted([1, -2, 4, 5, 7, -9]))
print(sorted([1, -2, 4, 5, 7, -9], key=abs))    # 依据绝对值排序
# [-9, -2, 1, 4, 5, 7]
# [1, -2, 4, 5, 7, -9]
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
# ['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
# 忽略大小写，按照字母序排序,即都变为大写或者都变为小写
# ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower, reverse=True))
# 通过reverse = True 实现反向排序

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
# 请用sorted()对学生列表分别按名字排序以及按成绩从高到低排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda t: t[0]))    # 以元组中第一个元素作为sorted排序对象
print(sorted(L, key=lambda t: t[1], reverse=True))   # 以元组中第二个元素作为sorted排序对象,倒序排序
print(sorted(L, key=lambda t: -t[1]))   # 以元组中第二个元素作为sorted排序对象,倒序排序,-t[1]

def by_name(t):
    return t[0]
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L,key=by_score,reverse=True)
print(L3)