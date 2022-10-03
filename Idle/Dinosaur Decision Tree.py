Q1 = input("Does it walk on all fours?")
if Q1.lower() == ("yes"):
    Q2 = input("Does it have spikes?")
    if Q2.lower() == ("yes"):
        print("This is a Stegosaurus.")
    else:
        Q3 = input("Does it have horns?")
        if Q3.lower() == ("yes"):
            print("This is a Triceratops.")
        else:
            print("This is a Brachiosaurus.")
else:
    Q4 = input("Can it fly?")
    if Q4.lower() == ("yes"):
        print("This is a Pterodactyl.")
    else:
        Q5 = input("Is it tall?")
        if Q5.lower() == ("yes"):
            print("This is a T-Rex")
        else:
            print("This is a Velociraptor")
