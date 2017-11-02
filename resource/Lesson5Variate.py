'''
Created on 2017年8月4日

@author: Administrator

5:语句（变量）
'''

'''
x=10
int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串 
'''

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 删除列表元素
print(list3)
del list3[2]
print("After deleting value at index 2 : ")
print(list3)

# python 创建二维列表，将需要的参数写入 cols 和 rows 即可
list_2d = [[0 for i in range(5)] for i in range(5)]
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(7)
list_2d
print(list_2d)

print()
print()

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

print(list01)
print(list02)

# 列表截取

print(list01[0])
print(list01[-1])
print(list01[0:3])

# 列表重复

print(list01 * 2)

# 列表组合

print(list01 + list02)

# 获取列表长度

print(len(list01))

# 删除列表元素

del list02[0]
print(list02)

# 元素是否存在于列表中

print('john' in list02)  # True

# 迭代

for i in list01:
    print(i)

# 比较两个列表的元素

# print (cmp(list01, list02))

# 列表最大/最小值

print(max([0, 1, 2, 3, 4]))
print(min([0, 1]))

# 将元组转换为列表

aTuple = (1, 2, 3, 4)
list03 = list(aTuple)
print(list03)

# 在列表末尾添加新的元素

list03.append(5)
print(list03)

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

list03.extend(list01)
print(list03)

# 统计某个元素在列表中出现的次数

print(list03.count(1))

# 从列表中找出某个值第一个匹配项的索引位置

print(list03.index('john'))

# 将对象插入列表

list03.insert(0, 'hello')
print(list03)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

print(list03.pop(0))
print(list03)

# 移除列表中某个值的第一个匹配项

list03.remove(1)
print(list03)

# 反向列表中元素

list03.reverse()
print(list03)

# 对原列表进行排序

# list03.sort()
print(list03)

print()
print()
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
# 创建空元组
tup1 = ();
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7);

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

 

