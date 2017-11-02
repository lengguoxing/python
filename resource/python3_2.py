'''
Created on 2017年8月9日

@author: Administrator
'''

import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        print('-',n)
        if (counter > n): 
            return
        print('#before ',n)
        yield a
        #print('#after ',n)
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()  
        
        