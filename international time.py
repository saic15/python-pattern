import pytz
from datetime import datetime
a=pytz.timezone("Asia/Tokyo")
b=datetime.now(a)
print(b)