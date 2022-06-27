import psutil
import numpy as np
import datetime

#read
pid = psutil.pids()
boottime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
cpucount = psutil.cpu_count

#prozess
maxpid = np.max(pid)
minpid = np.min(pid)

#print
print("CPU cputcount: ", cpucount)
print("Maximal Pid:", maxpid)
print("Minmal Pid:", minpid)
print("Boottime: ", boottime)
