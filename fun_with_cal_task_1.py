import calendar

y, m, d = map(int, input().split())
days = {
    0: 'Monday', 
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday', 
    5: 'Saturday',
    6: 'Sunday'
}

try:
    day_num = calendar.weekday(y, m, d)
    print(days[day_num])

except Exception as e:
    print(e)