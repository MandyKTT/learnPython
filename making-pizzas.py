#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
#导入模块方法①
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# 导入模块方法②
from pizza import make_pizza

make_pizza(16, 'pepperoni')"""

# 使用as给函数指定别名
from pizza import make_pizza as mp

mp(16, 'pepperoni')

# 使用as给模块指定别名
import pizza as p

p.make_pizza(16, 'pepperoni')

# 导入模块中的所有函数
from pizza import *

make_pizza(16, 'pepperoni')

