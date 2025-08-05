import os
import datetime
import time

#importing color module
try:
    from my_libraries.my_color import print_color_text as my_color
except:
    print("\033[93mWarning:\033[00mCould NOT load my_color module! Will run without color!")
    def my_color(text,no_color): print(text,end="")

#importing config module
try:
    import config
except:
    my_color("config.py ","green")
    my_color("file NOT found! Please copy config from ","red")
    my_color("config_exmple.py\n","green")
    exit(0)

match len(config.code_for):
    case 0:
        my_color("Write module to be run in list code_for in config.py file","red")
    case 1:
        print(f"Running {config.code_for[0]} module")
    
#import client.recording

