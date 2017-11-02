'''
Created on 2017年8月3日

@author: Administrator

2:变量类型
'''
#变量赋值
'''
Python 中的变量赋值不需要类型声明。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值
'''
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print (counter)
print (miles)
print (name)

#多个变量赋值
a = b = c = 1
#您也可以为多个对象指定多个变量
a, b, c = 1, 2, "john"

'''
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
'''
#数字
var1=11
var2=12
var3=13
var1=100
print(var1)
#您可以通过使用del语句删除单个或多个对象的引用
#del var1
del var1, var2
print(var3)

#字符串
s = 'ilovepython'
print(s[1:5]) #上面的结果包含了s[1]的值l，而取到的最大范围不包括上边界
#加号（+）是字符串连接运算符，星号（*）是重复操作
str = 'Hello World!'
 
print (str)           # 输出完整字符串
print (str[0])       # 输出字符串中的第一个字符
print (str[2:5])      # 输出字符串中第三个至第五个之间的字符串
print (str[2:])      # 输出从第三个字符开始的字符串
print (str * 2)      # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串

#列表
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个的元素 
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列表

#元组
'''元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。'''
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第三个的元素 
print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)       # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组
#以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
#tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

#字典
'''字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print (dict['one'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值

n=1
print(type(n))
print(isinstance(a, int))

#笔记
'''
变量赋值简单粗暴不需要声明类型, 灵活多变,非常好用。
数字数据类是不可改变的数据类型，改变数字数据类型会分配一个新的对象。
字符串的操作有基本的功能不需要再自己进行拼接遍历的操作。
列表用 "[ ]" 标识类似 C 语言中的数组。
元组用 "( )" 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
字典用 "{ }" 标识。字典由索引 key 和它对应的值 value 组成。

python 的所有数据类型都是类,可以通过 type() 查看该变量的数据类型
此外还可以用 isinstance 来判断
区别就是:
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
 
 数据类型 分为数字型和非数字型。
数字型包括整型，长整型，浮点型，复数型；
非数字型包括字符串，列表，元组和字典 ；
非数字型的共同点：都可以使用切片、链接（+）、重复（*）、取值（a[]）等相关运算;
非数字型的不同点：
列表 可以直接赋值，元组不可以赋值，字典按照 dict[k]=v 的方式赋值。
'''
