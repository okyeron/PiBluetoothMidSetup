import subprocess
import json 
import os 
import shutil

def set_up_maschine():
    results = subprocess.check_output("dmesg", universal_newlines=True).split('\n')
    for device in results:
        if "Native Instruments".lower() in device.lower():
            print(device)

set_up_maschine()