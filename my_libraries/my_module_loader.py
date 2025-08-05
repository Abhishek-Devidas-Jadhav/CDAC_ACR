#importing color module
current_machine=""
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
    
"""#function to set purpose of this machine based on in_name 
def set_current_machine(in_name):
    global current_machine
    current_machine=in_name
    #print(f"Testing {current_machine}")#Debugging
    match current_machine:
        case "client":
            #print("loading librarries")#Debugging
            import client.recording as recording"""

#statements to call set_current_machine
match len(config.module_list):
    case 0:
        my_color("Write module to be run in list code_for in config.py file","red")
        exit(0)
    case 1:
        current_machine=config.module_list[0]
        my_color(f"{current_machine} selected...","green")
    case _:
        my_color("Multiple machine usage detected! Please select one for this process:\n","green")
        for i in range(len(config.module_list)):
            my_color(f"{i}. {config.module_list[i]}","blue")
        print("Your choice: ",end="")
        current_machine=config.module_list[int(input())]
        my_color(f"{current_machine} selected...","green")

match current_machine:
    case "client":
        import client.recording as recording