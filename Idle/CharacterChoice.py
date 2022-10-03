print("Please choose from: Walter White, Saul Goodman, Gustavo Fring, Lalo Salamanca, Kim Wexler or Chuck McGill.")
Q1 = input("Does your character appear in breaking bad?")
if Q1.lower() == ("yes"):
    Q2 = input("Does your character have hair?")
    if Q2.lower() == ("no"):
        Q3 = input("Does your character cook meth?")
        if Q3.lower() == ("yes"):
            print ("You are thinking of Walter white")
        else:
            print ("You are thinking of Gustavo Fring")
    else:
        print("You are thinking of Saul Goodman")
else:
    Q4 = input("Is your character a lawyer?")
    if Q4.lower() == ("yes"):
        Q5 = input("Is your character allergic to electricity?")
        if Q5.lower() == ("yes"):
            print("You are thinking of Chuck McGill")
        else:
            print("You are thinking of Kim Wexler")
    else:
        print("You are thinking of Lalo Salamanca")

Final = input("Was I correct?")
if Final.lower() == ("yes"):
    print("Fantastic!")
else:
    print("I'll try harder next time")
                     
