#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from subprocess import Popen, PIPE
 
pin_number=20
proc = Popen(
    "echo %s > /sys/class/gpio/export" % pin_number,
    shell=True,
    stdout=PIPE, stderr=PIPE
)
 
proc.wait() 
proc = Popen(
    "cat /sys/class/gpio/gpio%s/value" % pin_number,
    shell=True,
    stdout=PIPE, stderr=PIPE
)
proc.wait()
res = proc.communicate()  # get tuple('stdout', 'stderr')
count = res[0].replace("\n","")
count = int(count)
 
if count == 0:
        id=0
else:
        print('1').replace("\n","")