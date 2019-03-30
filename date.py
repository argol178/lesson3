from datetime import datetime, timedelta
dt_now = datetime.now()
now = dt_now.strftime('%d.%m.%Y %H:%M')


delta_yest = timedelta(days = 1)
dt_yest = dt_now - delta_yest
yest = dt_yest.strftime('%d.%m.%Y %H:%M')


delta_month = timedelta(days = 30)
dt_month = dt_now - delta_month
month = dt_month.strftime('%d.%m.%Y %H:%M')

print("Вчера было {}, сейчас {}, а месяц назад было {}".format(yest,now,month))

date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")

print(date_dt)