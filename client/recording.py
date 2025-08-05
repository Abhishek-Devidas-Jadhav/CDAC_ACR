import pyautogui
import os
import datetime
import time
import config
from config import client_screenshot_path as client_screenshot_path
test_flag = 1#Debugging


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
    print("Capturing images: ")
    for i in range(config.times):
        time.sleep(config.sleep_duration)
        replace_to_underscore = str.maketrans({" ": "_", "-": "_", ":": "_"})
        image_name=str(datetime.datetime.now())[:-7].translate(replace_to_underscore)
        #image_name=str(datetime.datetime.now())[:-7].replace(" ","_").replace("-","_").replace(":","_")
        image1 = pyautogui.screenshot(f"{client_screenshot_path}/{image_name}.png")
        print(f"{image_name}.png")
