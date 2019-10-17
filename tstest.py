import subprocess
import signal
import os
import time

# f = open("~/device_num.txt", "r")

# device_num = f.read()
device_num = 3
while 1:
    # tegra stats
    os.system('~/tegrastats -once | grep RAM > ~/device' + str(device_num) + '/log.txt')
    # GPU usage
    os.system('cat /sys/devices/gpu.0/load >> ~/device' + str(device_num) + '/log.txt')

    # Number of decoded files
    os.system('ls -1 ./soundfiles/ | wc -l > ~/device' + str(device_num) + '/num_files.txt')
    os.system('ls -1 ./logs/ | wc -l >> ~/device' + str(device_num) + '/num_files.txt') 
    
    time.sleep(1)

    os.system('scp -r ~/device' + str(device_num) + ' mjwoo@172.22.44.52:/Users/mjwoo/PycharmProjects/CARD_dashboard')

