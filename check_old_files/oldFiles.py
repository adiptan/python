#check old files https://www.youtube.com/watch?v=mjyKFuwXVxY&t=1574s
import os
import time

days_ago = 5						#how many days you need to check
nowTime = int(time.time())				#now time in second
checkTime = int(24 * 60 * 60 * days_ago)  		#days in second
folders = ("/home/etp/python","/home/etp/flask-app")
ageTime = int(nowTime - checkTime)

def check_old_files(folder):
    for dirs, subdirs, files in os.walk(folder):
        for file in files:
            filesName = os.path.join(dirs, file)
            filesTime = int(os.path.getmtime(filesName))
            if filesTime < ageTime:
               print(str(filesName))


for folder in folders:
    check_old_files(folder)
