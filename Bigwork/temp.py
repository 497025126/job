# -*- coding:utf-8 -*-
# 该文件用于调试的
a = 35
temp = '35-50万'
res = [int(1000 * float(('%.1f' % (int(i) / 12)))) for i in temp.strip('万').split('-')]
print(res)