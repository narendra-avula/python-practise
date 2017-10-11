
__author__ = 'narendra'


from datetime import date, datetime
# a = date(date.today().year, 1, 1)
# b = date(date.today().year, 12, 31)
# print a
# print b
#
# print datetime.combine(a, datetime.min.time())
# print datetime.combine(b, datetime.min.time())

# today_date = datetime.date(2011, 7, 27)
# print today_date


year = 2016

start_time = datetime.combine(date(year, 1, 1), datetime.min.time())
end_time = datetime.combine(date(year, 12, 31), datetime.max.time())
print start_time
print end_time