import pyautogui
import os
import subprocess
import datetime
import time
import random
import re

#User-defined module
import config
from config import client_screenshot_path as client_screenshot_path

#test_flag = 1#Debugging
#String maketrans() method to replace characters
replace_to_underscore = str.maketrans({".":"_"," ": "_", "-": "_", ":": "_"})

#setting client ip and session id
try:
    client_ip=str(subprocess.check_output(f"ip addr | grep {config.client_nic} | grep -oE [0-9].*\\.[0-9]*/[0-9]*", shell=True, text=True))[:-4].translate(replace_to_underscore)
except:
    client_ip="127_0_0_1"
try:
    session_id=str(int(random.random()*pow(10,config.client_session_id_digits)))
except:
    session_id="0"

#make dirtectory .screenshots if it do not exist
if os.path.exists(client_screenshot_path)==0:
    print(f"Making folder at loction {client_screenshot_path}")
    os.mkdir(client_screenshot_path)

# delete old screenshots?
def delete_screenshots():
    del_list=[]
    print(f"Delete old screenshots? [y/n] ",end="")
    if input() == 'y':
        print(f"Deleting old screenshots!")
        for filename in os.listdir(client_screenshot_path):
           file_path = os.path.join(client_screenshot_path, filename)
           if os.path.isfile(file_path):
              os.remove(file_path)
              del_list.append(filename)
              #print(f"{filename},",end = " ")
        print(f"Screenshots deleted: {del_list}")
    else:
        print(f"Keeping old screenshots")
    print()

# take multiple screenshots for given number of times
def start_screenshots():
    #client_ip=str(os.system("ip addr | grep {config.client_nic} | grep -oE [0-9].*\\.[0-9]*/[0-9]*"))[:-3].translate(replace_to_underscore)
    #client_ip=subprocess.check_output("ip addr", shell=True, text=True)
    #print(client_ip)#Debugging
    #client_ip=str(re.search(config.client_nic,client_ip))
    #print(client_ip)#Debugging
    #client_ip=str(re.search(client_ip,"[0-9].*\\.[0-9]*/[0-9]*"))
    #client_ip=client_ip[:-3].translate(replace_to_underscore)

    print("Capturing images: ")
    for i in range(config.times):
        time.sleep(config.sleep_duration)
        image_name=f"{client_ip}_{session_id}_{str(datetime.datetime.now())[:-7].translate(replace_to_underscore)}"
        #image_name=str(datetime.datetime.now())[:-7].replace(" ","_").replace("-","_").replace(":","_")
        image1 = pyautogui.screenshot(f"{client_screenshot_path}/{image_name}.png")
        print(f"{image_name}.png")
