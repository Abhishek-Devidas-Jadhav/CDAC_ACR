def print_color_text(my_string,my_color):
    match my_color:
        case "red":
            print(f"\033[91m{my_string}\033[00m",end="")
        case "green":
            print(f"\033[92m{my_string}\033[00m",end="")
        case "yellow":
            print(f"\033[93m{my_string}\033[00m",end="")
        case "light_blue":
            print(f"\033[94m{my_string}\033[00m",end="")
        case "purple":
            print(f"\033[95m{my_string}\033[00m",end="")
        case "cyan":
            print(f"\033[96m{my_string}\033[00m",end="")
        case "gary":
            print(f"\033[97m{my_string}\033[00m",end="")
        case "black":
            print(f"\033[90m{my_string}\033[00m",end="") 
