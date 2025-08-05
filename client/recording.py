import pyautogui

# delete old screenshots?
del_list=[]
print(f"Delete old screenshots? [y/n] ",end="")
if input() == 'y':
    print(f"Deleting old screenshots!")
    for filename in os.listdir(folder_path):
       file_path = os.path.join(folder_path, filename)
       if os.path.isfile(file_path):
          os.remove(file_path)
          del_list.append(filename)
          #print(f"{filename},",end = " ")
    print(f"Screenshots deleted: {del_list}")
else:
    print(f"Keeping old screenshots")
print()

# take multiple screenshots for given number of times
print("Capturing images: ")
for i in range(times):
    time.sleep(sleep_duration)
    image_name=datetime.datetime.now()
    image1 = pyautogui.screenshot(f"{folder_path}/{image_name}.png")
    print(f"{image_name}.png")
