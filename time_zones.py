from datetime import datetime
import pytz

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone) # now() acepta un objeto de tipo pytz que contiene la time zone
print(f'Ciudad de México: {mexico_date.strftime("%d/%m/%Y, %H:%M:%S")}')

japan_timezone = pytz.timezone("Asia/Tokyo")
japan_date = datetime.now(japan_timezone)
print(f'Tokyo: {japan_date.strftime("%d/%m/%Y, %H:%M:%S")}')

diference_time = japan_date - mexico_date
print(diference_time)