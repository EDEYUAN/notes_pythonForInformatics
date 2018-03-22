# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17

#################### Chapter 4 ###########################
# Q4.6 重写之前的工资计算程序，加班时间的工资按原工资的150%计算。创建一个computepay函数，包含两个参数hours和rate。
def computepay(workTime, payRate):
    if workTime > 40:
        pay = (float(workTime) - 40) * 1.5 * float(payRate) + \
              40 * float(payRate)
    else:
        pay = float(workTime) * float(payRate)
    print 'Pay:%s' % (pay)


print 'Q4.6'
errorFlag = 0
hours = raw_input('Enter Hours:')
rate = raw_input('Enter Rate:')
try:
    workTime = float(hours)
    payRate = float(rate)
except:
    print 'Error: please enter numeric input'
    errorFlag = 1

if not errorFlag:
    computepay(workTime, payRate)


# Q4.7 重写之前的分数计算程序，使用computegrade函数，score作为参数，返回一个评分等级的字符串。
def computegrade(score):
    if score > 1:
        return 'Beyond upper limitation'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'


print 'Q4.7'
errorFlag = 0
try:
    score = float(raw_input('Enter score lie in range [0.01 1]:'))
except:
    print('Bad score\n Error: please enter numeric input\n')
    errorFlag = 1

if not errorFlag:
    print computegrade(score)