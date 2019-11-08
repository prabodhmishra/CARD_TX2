#!/bin/sh

import os
import inotify.adapters
import datetime

start = datetime.datetime.now()

os.system("ffmpeg -f alsa -i hw:2 -f segment -segment_time 30 -loglevel quiet -ar 16000 soundfiles16/audio_%04d.wav &")

notifier = inotify.adapters.Inotify()
notifier.add_watch('/home/nvidia/CARD_TX2/soundfiles16')

for event in notifier.event_gen():
    # print "working..."
    # print event
    if event is not None:
        # print event      # uncomment to see all events generated
        if 'IN_CREATE' in event[1]:
            if event[3] != "audio_0000.wav":
                inc = datetime.datetime.now()
                print "file '{0}' created in '{1}'".format(event[3], event[2])
                print "Elapsed time: " + str((inc - start).total_seconds())
                # os.system("free -m | awk 'NR==2{printf \"Memory Usage: %s/%sMB (%.2f%%)\\n\", $3,$2,$3*100/$2 }'")
                # os.system("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\\n\", $(NF-2)}'")
                #os.system("ffmpeg -i soundfiles16/" + tempaudio + " -loglevel quiet -ac 1 -ar 8000 soundfiles08/" + tempaudio)
                templog = tempaudio[:-4] + ".log"
                os.system('sox soundfiles16/' + tempaudio +  ' -t raw -c 1 -b 16 -r 8k -e signed-integer - | nc  localhost 5050 >> logs/' + templog)
                #os.system("./decode.sh soundfiles08/" + tempaudio + " >> logs/" + templog)
            tempaudio = event[3]
