# -*- codeing=utf-8 -*-
# @Time: 23:03
# @Author :liuwei
# @File:1.py
import support
#一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。
support.print_func('12')
support.print_func('13')

from support import print_func
print_func('14')