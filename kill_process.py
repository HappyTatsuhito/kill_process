#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import subprocess
import time

def getProcess():
    process = subprocess.check_output('ps -h', shell=True)
    process = process.split('\n')
    ps_list = []
    for i in range(len(process)-1):
        ps_list.append(process[i].split())
    return ps_list

def killAll():
    print ('all')
    ps_list = getProcess()
    for i in range(len(ps_list)):
        if 'kill_process.py' in ps_list[i][-2]:
            break
        if ps_list[i][4] != 'bash':
            subprocess.call('kill -15 ' + ps_list[i][0], shell=True)
    loop_flg = True
    while loop_flg:
        ps_list = getProcess()
        state_list = []
        for i in range(len(ps_list)):
            state_list.append(ps_list[i][2])
        if not('Sl+' in state_list):
            loop_flg = False
        time.sleep(0.1)
    ps_list = getProcess()
    for i in range(len(ps_list)):
        if 'kill_process.py' in ps_list[i][-2]:
            break
        subprocess.call('sudo kill -9 ' + ps_list[i][0], shell=True)

def killRuning():
    print ('runing')
    ps_list = getProcess()
    for i in range(len(ps_list)):
        if 'kill_process.py' in ps_list[i][-2]:
            break
        if ps_list[i][4] != 'bash':
            subprocess.call('kill -2 ' + ps_list[i][0], shell=True)

            
if __name__ == '__main__':
    args = sys.argv
    try:
        if args[1] == '-a':
            killAll()
        elif args[1] == '-r':
            killRuning()
    except IndexError:
        print ("Please select the \'-a\' or \'-r\' option.")
        
