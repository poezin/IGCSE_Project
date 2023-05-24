import random
ran_num=random.randint(1,10)
count=0
while True:

    user_input=int(input("Enter a number: "))
    if user_input==ran_num:
        print(f"You won. The number is {user_input}")
        break
    else:
        print("Sorry. Guess again.")
        count+=1
        if count==4:
            print("You lose:")
            break
