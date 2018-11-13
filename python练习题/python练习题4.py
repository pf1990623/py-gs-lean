# 输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，先把前两个月加起来，再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时，应该考虑多加一天。
# -*- coding:UTF-8 -*-
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
sum = 0
months = ( (0,31,59,90,120,151,181,212,243,273,304,334))
if 0 < month < 12:
    sum = months[month - 1 ]
else:
    print('data error')
sum +=day
print(sum)
leap = 0
if (year % 400 == 0 ) or ((year % 4 == 0) and (year % 100 !=0)):
    leap = 1
if leap == 1 and month > 2:
    sum+=1
print('it is the %dth day.' % sum)

# 此答案有bug:如果我2月份输入30号，程序就会判断错误