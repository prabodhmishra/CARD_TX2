import subprocess
import signal
import os
import time


while 1:
    # tegra stats
    os.system('~/tegrastats -once | grep RAM > ./dash_files/log.txt')
    # GPU usage
    os.system('cat /sys/devices/gpu.0/load >> ./dash_files/log.txt')

    # Number of decoded files
    os.system('ls -1 ./soundfiles16/ | wc -l > ./dash_files/num_files.txt')
    os.system('ls -1 ./logs/ | wc -l >> ./dash_files/num_files.txt') 
    
    time.sleep(1)

	# os.system('sshpass -p "123456" scp log.txt mjwoo@198.21.159.113:/Users/mjwoo/PycharmProjects/CARD_dashboard')

