'''
Created on 2017年8月9日

@author: Administrator

python特性
'''

x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

'''Set（集合）
集合（set）是一个无序不重复元素的序列。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。'''
 
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中') 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam') 
print(a) 
print(a - b)     # a和b的差集 
print(a | b)     # a和b的并集 
print(a & b)     # a和b的交集 
print(a ^ b)     # a和b中不同时存在的元素

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=', ')
    a, b = b, a+b
print()
print("----------")
    
a=10;b=388;c=98
print(a,b,c,sep='@') 
print("----------")   

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))
print (next(it))
print("----------")

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
    
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print()
print("----------@")
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()  
          
print()
print("----------#")


        