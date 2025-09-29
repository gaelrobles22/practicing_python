# import time

# print(time.time())

# import datetime

# fecha = datetime.datetime(2024, 1, 1)
# print(fecha)

from datetime import datetime

fecha = datetime(2024, 1, 1)
print(fecha)

ahora = datetime.now()
print(ahora)


fechaStr = datetime.strptime("2024-01-03", "%Y-%m-%d")
print(fechaStr)
