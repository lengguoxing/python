'''
Created on 2017年8月3日

@author: Administrator

1:基础语法
'''

print('hello world')
print("Hello, Python!")

#行和缩进
if True:
    print("True")
else:
  print("False")
  
#多行语句  
total = 'item_one ' + \
        'item_two ' + \
        'item_three '
print(total)   
days = ['Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday']
print(days)

#引号
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。包含了多个语句"""

#注释
# 第一个注释
print("Hello, Python!")  # 第二个注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

#等待用户输入
#str = input("\n\nPress the enter key to exit.")
#print("input is "+str)

#同一行显示多条语句,语句之间使用分号(;)分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#Print 输出
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号：
x="a"
y="b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出(貌似在这里不起作用)
print(x),
print(y),

print ('hello,',end='')  
print ('world!') 

#多个语句构成代码组
if x=="a":
    print("x==a")
elif x!="a":
    print("x!=a")

#命令行参数
'''
$ python -h 
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ... 
Options and arguments (and corresponding environment variables): 
-c cmd : program passed in as string (terminates option list) 
-d     : debug output from parser (also PYTHONDEBUG=x) 
-E     : ignore environment variables (such as PYTHONPATH) 
-h     : print this help message and exit 
'''
 