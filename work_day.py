from datetime import datetime
from calendar import monthrange
from datetime import timedelta

day = datetime.today().strftime("%d.%m.%Y-%j")

day_of_week = { 0: 'понеділок', 1: 'вівторок', 2: 'середа', 3: 'четвер', 4: 'п’ятниця', 5: 'субота', 6: 'неділя'}

hollydays = {'2022.01.01': 'Новий рік', '2022.01.07': 'Різдво', '2022.03.08': 'Міжнародний жіночий день', '2022.04.24':'Великдень',
             '2022.05.01': 'День праці', '2022.05.09': 'День Перемоги', '2022.06.12': 'Трійця', '2022.06.28': 'День Конституції України',
             '2022.08.24': 'День Незалежності України', '2022.10.14': 'День захисника України',  '2022.12.12': 'Різдво' }
months = {
        1: 'січня', 2: 'лютого', 3: 'березня', 4: 'квітня', 5: 'травня', \
        6: 'червня', 7: 'липня', 8: 'серпня',  9: 'вересня', 10: 'жовтня', 11: 'листопада', 12: 'грудня'
    }
offday = {'5': 'субота', '6': 'неділя'}
exceptions = []

day_w = datetime(2022, 2, 21)
# sructured
# # day_w = datetime(2022, 2, 21).timetuple()
# year = day_w.tm_year

year = day_w.timetuple().tm_year
day = day_w.timetuple().tm_mday
month = day_w.timetuple().tm_mon
year_day_num = datetime(year, month, day).timetuple().tm_yday
day_week_num = day_w.timetuple().tm_wday
day_number2date = datetime.strptime(str(year) + "-" + str(year_day_num), "%Y-%j").strftime("%d.%m.%Y")
days_in_year = datetime(2022, 12, 31).timetuple().tm_yday
# visokosny god
# print(day_w)
# print(year)
# print(day)
# print(month)
# print(year_day_num)
# print(day_number2date)
# print(f'Days in 2022 year is: {days_in_year}')
# print(day_week_num)


def work_period(date_month_year):
    first_count_day = datetime.strptime(date_month_year, "%d.%m.%Y")
    first_work_day =''
    last_work_day =''
    year = first_count_day.timetuple().tm_year
    day = first_count_day.timetuple().tm_mday
    month = first_count_day.timetuple().tm_mon
    days_in_month = monthrange(year, month)[1]
    first_day_in_month = datetime(year, month, 1)
    last_day_in_mounth = first_day_in_month + timedelta(days=(days_in_month-1))

    # Find first work day:
    if str(first_count_day.strftime("%Y.%m.%d")) in hollydays or str(first_count_day.timetuple().tm_wday) in offday:
        # print('this is not work day_need to find it')
        while first_work_day == "":
            if first_count_day.strftime("%Y.%m.%d") in hollydays or str(first_count_day.timetuple().tm_wday) in offday:
                first_count_day = first_count_day + timedelta(days=1)
                # print(first_count_day,  'holly day')
            else:
                first_work_day = f'{first_count_day.timetuple().tm_mday} {months[first_count_day.timetuple().tm_mon]} {first_count_day.timetuple().tm_year} р.'
                print(first_work_day , 'first work day')
    else:
        # print('this is work day allready')
        first_work_day = f'{first_count_day.timetuple().tm_mday} {months[first_count_day.timetuple().tm_mon]} {first_count_day.timetuple().tm_year} р.'
        print(first_work_day, 'first work day')

    # find last work day:
    if str(last_day_in_mounth.strftime("%Y.%m.%d")) in hollydays or str(last_day_in_mounth.timetuple().tm_wday) in offday:
        # print('last day is not work day_need to find it')
        while last_work_day == "":
            if last_day_in_mounth.strftime("%Y.%m.%d") in hollydays or str(last_day_in_mounth.timetuple().tm_wday) in offday:
                last_day_in_mounth = last_day_in_mounth - timedelta(days=1)
                # print(last_day_in_mounth,  'holly day')
            else:
                last_work_day = f'{last_day_in_mounth.timetuple().tm_mday} {months[last_day_in_mounth.timetuple().tm_mon]} {last_day_in_mounth.timetuple().tm_year} р.'
                print(last_work_day , 'last work day')
    else:
        last_work_day = f'{last_day_in_mounth.timetuple().tm_mday} {months[last_day_in_mounth.timetuple().tm_mon]} {last_day_in_mounth.timetuple().tm_year} р.'
        print(last_work_day, 'last work day')

    return (first_work_day, last_work_day)


print(work_period('1.01.2022')[0])
