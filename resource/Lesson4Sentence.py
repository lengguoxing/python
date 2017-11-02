'''
Created on 2017年8月3日

@author: Administrator

4:语句（条件语句+循环）
'''

# Python程序语言指定任何非0和非空（null）值为True，0 或者 null为False。
# Python 编程中 if 语句用于控制程序的执行
flag = False
name = 'luren'
if name == 'luren':         # 判断变量否为'python'
    flag = True               # 条件成立时设置标志为真
    print('welcome boss')    # 并输出欢迎信息
else:
    print(name)              # 条件不成立时输出变量名称
    
# 简单的语句组
var = 101
 
if (var == 100) : print("变量 var 的值为100")
 
print("Good bye 1!")

# 循环
count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1
 
print("Good bye 2!")

i = 1
while i < 10:   
    i += 1
    # print ("i ", i)
    if i % 2 > 0:     # 非双数时跳过输出
        # print ("i%2 > 0 ", i)
        continue
    print("continue ", i)         # 输出双数2、4、6、8、10
    
i = 1
while i < 10:   
    i += 1
    if i % 2 > 0:     # 非双数时跳过输出
        break
    print("break ", i)         # 输出双数2
 
i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
    
# for循环的语法格式如下：
# for iterating_var in sequence:
   # statements(s)
   
for letter in 'Python':     # 第一个实例
    print('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print('当前水果 :', fruit)
 
print("Good bye 3!")

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print('当前水果 2:', fruits[index])
 
print("Good bye 4!")


i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i % j): break
        j = j + 1
    if (j > i/j) : print (i, " 是素数")
    i = i + 1
 
print("Good bye 5!")

# 使用内置 enumerate 函数进行遍历:
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)

# 使用list.append()模块对质数进行输出。
# 输出 2 到 100 简的质数
prime = []
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
print(prime)

# 打印空心等边三角形 
rows = 11
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print(" * ", end='')
        elif i == rows - 1:
            if k % 2 == 0:
                print(" * ", end='')
            else:
                print("   ", end='')
        else:
            print("   ", end='')
    print("\n")

# 打印1-9三角形阵列:
for i in range(1, 11):
    for k in range(1, i):
        print(k, end='')
        k += 1
    i += 1
    print("\n")
    
'''在python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列
的下标'''
s = 'qazxswedcvfr'
for i in range(0,len(s), 2):
    print(s[i])
'''enumerate() :
    在每次循环中，可以同时得到下标和元素
    际上，enumerate(),在每次循环中返回的是包含每个元素的定值表，两个元素分别赋值
 index，char'''
for (index,char) in enumerate(s):
    print("index=%s ,char=%s" % (index, char))
    
# 冒泡排序,来至于高学军:
# 冒泡排序# 定义列表 list
arays = [1,8,2,6,3,9,4]
for i in range(len(arays)):
    for j in range(i+1):
        if arays[i] < arays[j]:
            # 实现连个变量的互换
            arays[i], arays[j] = arays[j], arays[i]
print(arays)
    
# Python 循环嵌套
'''Python for 循环嵌套语法：    
for iterating_var in sequence:
for iterating_
var in sequence:
   statements(s)
statements(s) 

while expression:
   while expression:
      statement(s)
   statement(s)
'''

# 以下实例使用了嵌套循环输出2~100之间的素数：
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " 是素数")
    i = i + 1
 
print("Good bye!")

# 使用循环嵌套来获取100以内的质数
num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
       num.append(i)
print(num)

# 使用嵌套循环实现×字塔的实现
i = 1
# j=1
while i <= 9:
    if i <= 5:
        print("*"*i)

    elif i <= 9 :
        j = i-2*(i-5)
        print("*"*j)
    i += 1
else :
    print("")
   
# 冒泡排序
array = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
L = len(array)
for i in range(L):
    for j in range(L-i):
        if array[L-j-1] < array[L-j-2]:
            array[L-j-1], array[L-j-2] = array[L-j-2], array[L-j-1]
for i in range(L):
    print(array[i], end='')
    
print()
    
# Python语言 break 语句语法：
for letter in 'Python':     # 第一个实例
    if letter == 'h':
        break
    print('当期字母 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
    print('当期变量值 :', var)
    var = var - 1
    if var == 5:   # 当变量 var 等于 5 时退出循环
        break
 
print("Good bye!")
    
# python 语言 continue 语句语法格式如下
for letter in 'Python':     # 第一个实例
    if letter == 'h':
        continue
    print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
    var = var -1
    if var == 5:
        continue
    print('当前变量值 :', var)
print("Good bye!")
   

# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句。
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)

print("Good bye!")



