from datetime import datetime, timezone, timedelta
import time

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))

#userdate = input('Enter the date YYYY-mm-dd format: ')
#userdate= datetime.strptime(userdate, '%Y-%m-%d')

#print(userdate)

def measir_runtime(func):
  start = time.time()
  powers(5000000)
  end = time.time()
  print (end - start)

def powers(limit):
  return [x**2 for x in range(limit)]

measir_runtime(lambda: powers(500000))

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
