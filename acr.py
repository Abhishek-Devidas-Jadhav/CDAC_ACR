#importing module loader
try:
    import my_libraries.my_module_loader as mml
except:
    print("Cannot find module loader!")
    exit(0)
    
#print(mml.current_machine)#Debugging
match mml.current_machine:
    case "client":
        #print(mml.recording.test_flag)#Debugging
        mml.recording.delete_screenshots()
        mml.recording.start_screenshots()
