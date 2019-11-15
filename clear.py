import os
import datetime

var = str(datetime.datetime.now())
f = open("/home/nvidia/device_num.txt", "r")

device_num = str(f.readline(1))

'''
os.system("mkdir oldfiles/run_16_1")
os.system("mkdir oldfiles/run_08_1")
os.system("mkdir oldfiles/logs_1")

os.system("mv soundfiles16/* oldfiles/run_16_1")
os.system("mv soundfiles08/* oldfiles/run_08_1")
os.system("mv logs/* oldfiles/logs_1")
'''
os.system("rm soundfiles16/*")
os.system('rm ../device' + device_num + '/asr/*')
os.system("rm logs/*")
