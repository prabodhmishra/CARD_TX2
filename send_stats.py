#!/usr/bin/python

import subprocess
import signal
import os
import time
import sys

if len(sys.argv) != 3 or len(sys.argv) != 4:
    print 'Error!!! Incorrect number of arguments:', len(sys.argv), 'arguments passed.'
    print 'eg. python send_stats.py username IP_address directory_path'
    exit()
elif len(sys.argv) == 3:
    testpath = 'PycharmProjects/CARD_dashboard_github'
    
username = str(sys.argv[1])
loc = str(sys.argv[1]) + '@' + str(sys.argv[2])
path = str(sys.argv[3])
testpath = loc + ':/Users/' + username + '/' + path
print 'Sending files to: ', testpath

f = open("/home/nvidia/device_num.txt", "r")

device_num = str(f.readline(1))
last_sent = 0

while 1:
    # tegra stats
    os.system('~/tegrastats -once | grep RAM > ~/device' + device_num + '/log.txt')
    # GPU usage
    os.system('cat /sys/devices/gpu.0/load >> ~/device' + device_num + '/log.txt')

    # Number of decoded files
    os.system('ls -1 ./soundfiles16/ | wc -l > ~/device' + device_num + '/num_files.txt')
    os.system('ls -1 ./logs/ | wc -l >> ~/device' + device_num + '/num_files.txt')

    audlogfiles = os.popen('ls -1 ./logs/ | wc -l').read()
    cnt_audlogs = int(audlogfiles[:-1])
    new_files = (cnt_audlogs - 1) - last_sent
    if new_files > 0:
        os.system('rm ~/device' + device_num + '/asr/*')
        for x in range(new_files):
            os.system('cp ./logs/audio_' + '{:04d}'.format(last_sent+x) + '.log ~/device' + device_num + '/asr/')
        last_sent += new_files

    time.sleep(1)

    #os.system('scp -r ~/device' + device_num + ' mjwoo@198.21.158.154:/Users/mjwoo/PycharmProjects/CARD_dashboard_github')
    os.system('scp -r ~/device' + device_num + ' ' + loc + ':/Users/' + username + '/' + path)