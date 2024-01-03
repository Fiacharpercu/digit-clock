from time import localtime, strftime
import sys
import time

while True:
    ct = localtime()
    str_date = strftime('%Y-%m-%d', ct)
    str_time = strftime('%H:%M:%S', ct)
    sys.stdout.write(f'\r{str_date} {str_time}')
    sys.stdout.flush()
    time.sleep(1)
