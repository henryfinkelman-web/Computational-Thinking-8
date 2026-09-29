answer1 = input("School is starting - do you want to skip?    ")
if answer1 == "yes":
    answer2 = input("ok then do you want to go get breakfeast")
    if answer2 == "yes":
        print("ok lets get cereal")
    elif answer2 == "No": 
        print("lets just want to sleep in")
        print("Ok you get 2 hours of extra sleep")
    else:
   
       

elif answer1 == "no":
    answer3 = input("do you wanna go to first block comp?")
    if answer3 == "yes":
        print("ok we have to hurry to get to class.")
    elif answer3 == "no":
        print("ok just hide in the bathroom.")
        phone = input("Do you want to use your phone?")
        if phone == "yes" or phone == "Yes":
            print("oh no a teacher is coming hide your phone")
        elif answer3 == "no":
            print("ok lets just keep quiet")
        else: 
            print("yes or no")
                    
    else:
        print("Answer only Yes or No")

else:
    print("Well, that isn’t an option!")
