import time
import os
import shutil

days = time.localtime( time.time() )
print(days)

path = input("Enter Source Path : ")
os.path.exists(path)
os.walk(path)

ctime = os.stat(path).st_ctime

if (ctime > days):
    os.remove(path)

else:
    print("Path Doesn't Exist")
