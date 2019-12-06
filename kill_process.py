#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import subprocess

def killAll():
    print ('all')
    process = subprocess.check_output('ps -h', shell=True)
    process = process.split('\n')
    ps_list = []
    for i in range(len(process)-1):
        ps_list.append(process[i].split())
        if ps_list[i][-2] == 'kill_process.py':
            break
        if ps_list[i][4] != 'bash':
            subprocess.call('kill -15 '+ps_list[i][0], shell=True)
    loop_flg = True
    while loop_flg:
        state_list = []
        process = subprocess.check_output('ps -h', shell=True)
        for i in range(len(process.split('\n'))-1):
            state_list.append(process.split('\n')[i].split()[2])
        if not('Sl+' in state_list):
            loop_flg = False
    process = subprocess.check_output('ps -h', shell=True)
    process = process.split('\n')
    id_list = []
    for i in range(len(process)-1):
        id_list.append(process[i].split()[0])
        if process[i].split()[-1] == 'kill_process.py':
            break
        subprocess.call('sudo kill -9 '+id_list[i], shell=True)

def killRuning():
    print ('runing')
    process = subprocess.check_output('ps -h', shell=True)
    process = process.split('\n')
    ps_list = []
    for i in range(len(process)-1):
        ps_list.append(process[i].split())
        if ps_list[i][-2] == 'kill_process.py':
            break
        if ps_list[i][4] != 'bash':
            subprocess.call('kill -2 '+ps_list[i][0], shell=True)
        
if __name__ == '__main__':
    args = sys.argv
    if args[1] == '-a':
        killAll()
    elif args[1] == '-r':
        killRuning()
