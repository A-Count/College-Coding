positive_feelings = ["fine", "good", "happy", "great", "ok", "okay"]

greeting = input("How are you today?").lower()

if greeting in positive_feelings[0:-1]:
    print("Me too.")
else:
    print("Sorry to hear that.")

q1 = int(input("How many siblings do you have?"))

if q1 == 0:
    print("I'm an only child too.")
elif q1 > 3:
    print("Thats a lot of people!")
else:
    print("Nice")

q2 = input(("What is your favourite food?"))
print("Wow that's delicious")

q3 = input("Do you like videogames?")

if "yes" in q3.lower():
    input("Me too, what's your favourite?")
    print("That's a great game!")
    
q4 = input("What's your favourite film?")
print("Wow i love " + q4)

q5 = input("Before I leave, what's your name?")
print ("Nice talking to you " + q5)
