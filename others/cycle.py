# -*- coding: utf-8 -*-

#简易购物车
asset_all=0
il=input("请输入总资产：")
asset_all=int(il)

goods=[
    {"name":"电脑","price":5099},
    {"name":"手机","price":2999},
    {"name":"键盘","price":99},
    {"name":"iPad","price":3299},
    {"name":"游艇","price":500000},
    {"name":"巴雷特","price":6000},
    ]
car_list=[]
for i in goods:
    print(i["name"],i["price"])
while True:
    i2=input("请选择商品(y结算)：")
    if i2.lower()=="y":
        break
    for j in goods:
       if j["name"]==i2:
         car_list.append(j)
         print(car_list)

all_price=0
for item in car_list:
    p=item["price"]
    all_price+=p
if all_price>asset_all:
    print("对不起穷逼你买不起")
else:
    print("恭喜购买成功")