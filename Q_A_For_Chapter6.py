# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17
#==========================================================================
# ## Q6.5 使用以下语句存储一个字符串： str = ’X-DSPAM-Confidence: 0.8475’
#     使用find方法和字符串切片，提取出字符串中冒号后面的部分，然后使用float函数，将提取出来的字符串转换为浮点数。
#
#
#==========================================================================
str1 = 'X-DSPAM-Confidence: 0.8475'
index = str1.find(' ')
str2 = str1[index+1::]
print str2
num = float(str2)
print type(num), 'num = %g'%num  # 注意浮点数的占位符格式
