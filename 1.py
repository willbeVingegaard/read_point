import time
def timeshift(a):
    timeArray = time.localtime(a)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return  timeStr
print(timeshift(1655240591))
