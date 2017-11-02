# -*- coding: utf-8 -*-


li=["电脑","汽车","U盘","手机","游艇"]
for key, item in enumerate(li,1):
    print(key,item)


inp=input("请输入商品:")

inp_num= int(inp)

print(li[inp_num-1])



