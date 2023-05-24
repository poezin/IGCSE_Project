smartDevices=["Smart Lock", "Smart Lighting", "Smart Speaker","Smart Aircon","Smart Security Camera","Smart Refrigerator","Smart Washing Machine", "Smart Oven", "Smart TV", "Smart Plug"]
def smart_devices():
    for i in range(len(smartDevices)):
        print(i+1,": ",smartDevices[i])
    # print("1: Smart Lock\n2: Smart Lighting\n3: Smart Speaker\n4: Smart Aircon\n5: Smart Security Camera\n6: Smart Refrigerator\n7: Smart Washing Machine\n8: Smart Oven\n:9: Smart TV\n10: Smart Plug")



def control_devices():
    try:
        user_control = int(input("Which device do you want to control? Press only a device number!!!"))

        for j in range(len(smartDevices)):
            if user_control == j:
                con_dev=int(input("Press 1 to turn on:\nPress 2 to turn off your "))
                if con_dev == 1:
                    print("Your ",smartDevices[j-1],"has been turned on.")
                elif con_dev ==2:
                    print("Your ", smartDevices[j-1],"has been turned off.")
                else:
                    print("Invalid input")
                    control_devices()
    except Exception as e:
        print("Invalid input!")
        control_devices()

def main():
    try:
        while True:
            user_input = int(input("Press 1 to see Smart Home Device List:\nPress 2 to control the device:\n Press 3 to exit: "))
            if user_input == 1:
                smart_devices()
            elif user_input == 2:
                control_devices()
            elif user_input == 3:
                break
            else:
                print("Invalid number.")
                main()
    except Exception as e:
        print("Invalid input.")
        main()
if __name__ == '__main__':
    main()