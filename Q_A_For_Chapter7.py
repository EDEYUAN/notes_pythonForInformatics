# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17
# ==============================================================================
# Q7.1 编写一个程序，读取一个文件，以大写方式逐行打印出文件内容
# ==============================================================================
fileName = raw_input('Please enter a file name:')
try:
    fhand = open(fileName)
except:
    print 'File missing'
    exit()

for line in fhand:
    print line.upper()

# ==============================================================================
# Q7.2 编写一个程序，让用户输入文件名，然后读取文件，按行的形式j进行查看。
# X-DSPAM-Confidence: 0.8475
# 遇到以“X-DSPAM-Confidence：”开头的行，提取该行中的浮点数。统计行数，计算这些行的垃圾邮件信度值。文件读取结束
# 后，打印垃圾邮件平均信度。
# ==============================================================================
fileName = raw_input('Please enter a file name:')
try:
    fhand = open(fileName)
except:
    print 'File missing'
    exit()

lineCount = 0
accValue = 0
for line in fhand:
    line = line.rstrip()
    #    print line
    if line.startswith('X-DSPAM-Confidence:'):
        lineCount += 1
        index = line.find(' ')
        value = float(line[(index + 1)::])
        accValue += value

if lineCount >= 1:
    print 'There are %d items in this doc.' % lineCount
    print 'Average spam confidence: %g' % (accValue / lineCount)
else:
    print 'no specific line in the document'

# Q 7.3有时候,程序员感到无聊或是想找点乐子,他们会在程序里加入彩蛋(无害的代码)
# (http://en.wikipedia.org/wiki/Easter_egg_(media))。
# 修改上面的程序,当用户输入	“na	na boo boo”时,打印一些有趣的消息。
# 不管文件是否存在,程序都能正常运行。
fileName = raw_input('Please enter a file name:')
try:
    fhand = open(fileName)
except:
    print 'File missing'
    exit()

lineCount = 0
accValue = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        lineCount += 1

if lineCount >= 1:
    print 'There were %s subject lines in %s.' %(lineCount, fileName)
else:
    print 'no specific line in the document'
















