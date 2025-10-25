
from datetime import datetime

today = datetime.today().date()
date = "2023-10-15"
input_date = datetime.strptime(date, '%Y-%m-%d').date()
delta = today - input_date
delta_int= delta.days
print(delta)
 

