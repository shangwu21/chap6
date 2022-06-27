# -*- codeing=utf-8 -*-
# @Time: 22:53
# @Author :liuwei
# @File:1.py

total = 0;
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("Inside the function local total : ", total)
    return total;

# 调用sum函数
sum(10, 20);
print("Outside the function global total : ", total)

def print_func( par ):
   print ("Hello : ", par)
   return;
print_func('python')