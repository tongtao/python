# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 第三章 模块


# 3-1 模块和包的概念

#   在文件系统中，包就是文件夹，模块就是xxx.py文件
#   包也可以有多级
#   包 文件夹下面有__init__.py，且每级都必须要有！


# 3-2 导入模块

# from math import log
# from logging import log as logger   # logging的log现在变成了logger
# print log(10)   # 调用的是math的log
# logger(10, 'import from logging')   # 调用的是logging的log

import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')

# from os.path import isdir, isfile
# print isdir(r'/data/webroot/resource/python')
# print isfile(r'/data/webroot/resource/python/test.txt')


# 3-3 动态导入模块

# Task: Python 2.6/2.7提供了json 模块，
#       但Python 2.5以及更早版本没有json模块，不过可以安装一个simplejson模块，
#       这两个模块提供的函数签名和功能都一模一样。试写出导入json 模块的代码，
#       能在Python 2.5/2.6/2.7都正常运行。

try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})


# 3-4 使用__future__

#   当新版本的一个特性与旧版本不兼容时，该特性将会在旧版本中添加到__future__中，
#   以便旧的代码能在旧版本中测试新特性。

# Task: 在Python 3.x中，字符串统一为unicode，不需要加前缀 u，
#       而以字节存储的str则必须加前缀 b。
#       请利用__future__的unicode_literals在Python 2.7中编写unicode字符串。

# from __future__ import unicode_literals 这句使用__future__必须在文件最开始

s = 'am I an unicode?'
print isinstance(s, unicode)


# 3-5 安装第三方模块

# easy_install
# pip   推荐

# 命令行下  pip install web.py    安装web.py第三方模块
# 查询第三方模块名字，通过pypi.python.org