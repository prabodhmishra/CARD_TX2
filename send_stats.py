import subprocess
import signal
import os
import time

f = open("/home/nvidia/device_num.txt", "r")

device_num = str(f.readline(1))

while 1:
    # tegra stats
    os.system('~/tegrastats -once | grep RAM > ~/device' + device_num + '/log.txt')
    # GPU usage
    os.system('cat /sys/devices/gpu.0/load >> ~/device' + device_num + '/log.txt')

    # Number of decoded files
    os.system('ls -1 ./soundfiles/ | wc -l > ~/device' + device_num + '/num_files.txt')
    os.system('ls -1 ./logs/ | wc -l >> ~/device' + device_num + '/num_files.txt') 
    
    time.sleep(1)

    os.system('scp -r ~/device' + device_num + ' mjwoo@192.169.1.200:/Users/mjwoo/PycharmProjects/CARD_dashboard')