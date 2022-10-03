Ans_1 = input("Are they DC or Marvel?")

if Ans_1.lower() == ("dc"):
    Ans_2 = input("Are they male?")
    if Ans_2.lower() == ("yes"):
        print("You are thinking of Batman.")
    else:
        print("You are thinking of Wonder Woman")
else:
    Ans_3 = input("Can they fly?")
    if Ans_3.lower() == ("yes"):
        print("You are thinking of Iron Man")
    else:
        print("You are thinking of Spider Man")
        
