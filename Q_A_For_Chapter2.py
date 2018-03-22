# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17
###################### Chapter 2 ###########################
# Q2.2
name = raw_input('Enter your name:')
print 'Hello %s'%name

# Q2.3
hours = raw_input('Enter Hours:')
rate = raw_input('Enter Rate:')
print 'Pay:%s'%(float(hours) * float(rate))

# Q2.5 temperature converte F = ℃ × 1.8 + 32 Fahrenheit temperature
Ctep = raw_input('输入当前温度(摄氏度)：')
Ftep = float(Ctep) * 1.8 + 32
print '对应的华氏温度为：%s'%(Ftep)