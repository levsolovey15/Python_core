
from datetime import datetime

def days_from_date(date_str):
   
    today = datetime.today().date()
    input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    delta = today - input_date
    return delta.days

date = "2020-10-12"
result = days_from_date(date)
print(result)

