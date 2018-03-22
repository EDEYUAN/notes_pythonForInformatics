# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17
#################### Chapter 3 ###########################
# Q3.1 重写薪水计算公式，如果员工工作时间超过40小时，按平常薪水的1.5倍支付
print 'Q3.1'
hours = raw_input('Enter Hours:')
rate = raw_input('Enter Rate:')
if hours > 40:
    pay = (float(hours) - 40) * 1.5 * float(rate) + \
          40 * float(rate)
else:
    pay = float(hours) * float(rate)
print 'Pay:%s' % (pay)

# Q3.2 运用try和except重写支付程序，让程序可以正常处理非数字输入的情况，如果是非数字输入，打印消息并退出程序
print 'Q3.2'
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
    if workTime > 40:
        pay = (float(workTime) - 40) * 1.5 * float(payRate) + \
              40 * float(payRate)
    else:
        pay = float(workTime) * float(payRate)
    print 'Pay:%s' % (pay)

# Q3.3编写一个程序，提示分数在0.0和1.0之间。如果分数超出这个范围则打印出错误。如果分数在0.0和1.0之间，判读正确的Grade
print 'Q3.3'
errorFlag = 0
try:
    score = float(raw_input('Enter score lie in range [0.01 1]:'))
except:
    print('Bad score\n Error: please enter numeric input\n')
    errorFlag = 1

if not errorFlag:
    if score > 1:
        print('Beyond upper limitation')
    elif score >= 0.9:
        print 'A'
    elif score >= 0.8:
        print 'B'
    elif score >= 0.7:
        print 'C'
    elif score >= 0.6:
        print 'D'
    else:
        print 'F'