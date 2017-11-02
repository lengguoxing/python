# -*- coding: utf-8 -*-
li=["alex","ereic"]
s="_".join(li)

print(s)

name_list=["eirc","alex"]

name_list.append('seven')
name_list.append('seven')
name_list.append('seven')
print(name_list)
print(name_list.count("seven"))


# 转换为列表
s1="李璐"

li=list(s1)

print(li)

t2=("akes","jsdhs","lijie")

l2=list(t2)

print(l2)



#元组
#tuple

t=(11,22,33)

n=tuple((11,22,33,["k1","vm"]))

print(n)
#字典
dic={'k1':123,'k2':321}
n=dic.fromkeys(['k1','k2'],"alex")

print(n)
#奇偶判断
num=122

if num%2==0:
    print("偶数")
else:
    print("奇数")

#判断一个字符串在不在一个列表里
num1="alex"

li1=["alex","eirc"]

if num1 in li1 and num1.startswith("a"):
    print("在")
else:
    print("不在")
#字符字节转化
name="刘海"
b=bytes(name,encoding="utf-8")
print(b)
c=str(b,encoding="utf-8")
print(c)

#元素分类列表安按要求分类到字典里：
li=[11,12,16,85,15,1,9,58,66,87,98,100]

dic={ "k1":[],"k2":[]}
for i in li:
    if i<=66:
        dic["k1"].append(i)
    else:
        dic["k2"].append(i)
print(dic)

#去空格按输出首字母是"a"or"A'的元素
li=["aler"," aric","Alex","alex ","WSXSA","wase","dafd","gsdf","wesse"]
dic={"k1":"aler","k2":" aric","k3":"Alex","k4":"alex ","k5":"WSXSA","k5":"wase"}
for i in dic.values():
    new_i=i.strip()
    if new_i.startswith('a') or new_i.startswith("A"):
        print("结果:" + new_i)
    if new_i.endswith("e"):
        print("结果:"+new_i)

#简单购物车
li=["手机","电脑","箱包","轮船","飞机","大炮","航母"]
for i,j in enumerate(li,1):
    print(i,j)
num=input("请输入商品ID：")
num1=int(num)

len_li=len(li)
if num1>0 and num1<=len_li:
  good = li[num1 - 1]
  print(good)
else:
    print("对不起！没有该商品")


#省市县三级联动：

dic={
    "四川":{
          "成都":["双流","都江堰","青城山"],
           "广安":["岳池","华蓥","武胜","邻水"],
            },
  "广东": {
    "广州": ["不知道", "晓不得", "不了解"],
    "深圳": ["东莞", "五连发", "几十家", "技术男"],
            },
    "贵州": {
    "贵阳": ["茅台", "五粮液", "老干妈"],
    "武夷山": ["长江", "黄河", "黑龙江"],
            }
    }
for i in dic:
    print(i)
f1=input("请输入省份:")
a=dic[f1]
for j in a:
    print(j)

s1=input("请输入市：")
b=dic[f1][s1]
# print(b)
for s in b:
    print(s)




