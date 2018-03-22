# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17
#################### Chapter 5 ###########################
# =========================================================================
# Q5.1 编写一个程序，重复读取数据，直到用户输入“done”。一旦输入“done”，打印总和、个数与平均值。如果用户输入的
# 不是数字，使用try和except捕获异常，打印错误信息，然后跳过继续执行循环。
# =========================================================================
nrOfDigital = 0
accValue = 0
loopFlag = 1
while loopFlag:
    try:
        inNum = raw_input('Enter a digital number:')
        if inNum.lower() == 'done':
            loopFlag = 0
        else:
            num = float(inNum)
            nrOfDigital += 1
            accValue += num
    except:
        print 'Error, pls enter a number !'
        continue

print '总和：%s' % accValue
print '个数：%s' % nrOfDigital
if nrOfDigital:
    print '平均值：%s' % (accValue / nrOfDigital)
else:
    print '平均值：0'

## Q5.2 编写一个程序，提示用户输入一组数字，输出最大值和最小值，不要求平均值。
maxValue = 0
minValue = 0
array = []
loopFlag = 1
while loopFlag:
    try:
        inNum = raw_input('Enter a digital number or cmd ‘Done’:')
        if inNum.lower() == 'done':
            loopFlag = 0
        else:
            num = float(inNum)
            array.append(num)
    except:
        print 'Error, pls enter a number !'
        continue

print 'Max value is %s' % (max(array))
print 'Min value is %s' % (min(array))