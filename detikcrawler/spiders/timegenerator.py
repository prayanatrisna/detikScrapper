import time
from datetime import timedelta,date
def generate_datetime(start_month, end_month, year):
    date_all = []
    sep = '/'
    start_date = date(year, start_month, 1)
    
    if (end_month == 12):
        year=year+1
    
    end_date = date(year, (end_month+1)%12, 1)
    for single_date in daterange(start_date, end_date):
      date_all.append(single_date.strftime("%m"+sep+"%d"+sep+"%Y"))
    return date_all

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)