#importing module loader
try:
    import my_libraries.my_module_loader as mml
except:
    print("Cannot find module loader!")
    exit(0)
import time

#print(mml.current_machine)#Debugging
match mml.current_machine:
    case "client":
        #print(mml.recording.test_flag)#Debugging
        mml.recording.delete_screenshots()
        mml.recording.start_screenshots()
    case "server":
        while True:
            try:
                print(f"Here before write_to_csv")#Debugging
                #mml.server_function.object_category_index()#Debugging
                mml.server_function.write_to_csv(f"{mml.config.project_home}/server/.screenshots/my_csv.csv",{"a":"test"})
                """
                mml.server_function.write_to_csv(f"{mml.config.project_home}/server/.screenshots/my_csv.csv",
                mml.server_function.object_detect('/home/a/temp/models/research/object_detection/test_images/image2.jpg',
                mml.model_load.model,
                mml.server_function.object_category_index()))
                """
            except :
                print(f"exception occured!")
                pass
            time.sleep(1)#Debugging
        #mml.model_load
