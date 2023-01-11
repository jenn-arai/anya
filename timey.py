import threading
import datetime

print(datetime.datetime.now())

my_schdule = {'19:56:06': 'طوط طوط طوووط صارت بلستة', '19:57:06': 'هلو هلو راح تصير بل ستة وعشرة',
              '19:58:06': 'ياربي صارت وربع', '19:58:12': 'شنيي هااي  وثلث الة شوي'}
wed, wed2, wed3 = 'الفراش اليوم اوف', 'الفراش اليوم اوف', 'الفراش اليوم اوف'
weekly_schedule = {
    'sunday': [['', '', ''], ['', '', ''], ['', '', '']],
    'monday': [
        ['مختبر صخر عدنة برمجة ', 'مختبر الخوارزمي عدنة مهارات حاسوب ', 'مختبر الموصلات عدنة لوجك دزاين '],  # A1
        ['مختبر الموصلات عدنة لوجك دزاين ', 'مختبر صخر عدنة برمجة ', 'مختبر الخوارزمي عدنة مهارات حاسوب '],  # A2
        ['مختبر الخوارزمي عدنة مهارات حاسوب ', 'مختبر الموصلات عدنة لوجك دزاين ', 'مختبر صخر عدنة برمجة ']],  # A3

    'tuesday': [['لطابق الثاني عدنة تقسيم على قاعات الامتحان ', 'قاعة 4 عدنة رياضيات ', 'قاعة 4 عدنة ديمقراطية'],
                ['لطابق الثاني عدنة تقسيم على قاعات الامتحان ', 'قاعة 4 عدنة رياضيات ', 'قاعة 4 عدنة ديمقراطية'],
                ['لطابق الثاني عدنة تقسيم على قاعات الامتحان ', 'قاعة 4 عدنة رياضيات ', 'قاعة 4 عدنة ديمقراطية']],

    'wednesday': [[wed, wed2, wed3],
                  [wed, wed2, wed3],
                  [wed, wed2, wed3]],
    'thursday': [['قاعة 4 عدنة برمجة ', 'قاعة 8 عدنة انكلش', ''],
                 ['قاعة 4 عدنة برمجة ', 'قاعة 8 عدنة انكلش', ''],
                 ['قاعة 4 عدنة برمجة ', 'قاعة 8 عدنة انكلش', '']],
}


def get_day():
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return weekdays[datetime.datetime.now().weekday()]


def get_time():
    time = datetime.datetime.now().ctime().split()[3]
    return time


def get_customer_schedule(day, group_num):
    time_keys = ['08:25:06', '10:25:06', '12:25:06']
    day_values = weekly_schedule[day][group_num]
    return {time_keys[i]: day_values[i] for i in range(len(time_keys))}

#
# print(get_day())
# print(get_time())
# for i in my_schdule:
# print(my_schdule)
# print((get_customer_schedule(get_day(), 0)))
