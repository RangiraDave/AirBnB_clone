#!/usr/bin/python3
from datetime import datetime

today = datetime.now()
print(today)

d = today.strftime("%Y-%m-%dT%H:%M:%S.%f")
print(d)
