import random
while True:
    ran_num=random.randint(1,6)

    if ran_num==1:
        print("The number is 1")
    elif ran_num==2:
        print("The number is 2")
    elif ran_num==3:
        print("The number is 3")
    elif ran_num==4:
        print("The number is 4")
    elif ran_num==5:
        print("The number is 5")
    else:
        print("The number is 6")

    user_input=input("Do you want to play again (y/n)?")
    if user_input=='y':
        continue
    else:
        break
