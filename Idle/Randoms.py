import random                                        
alphabet = "abcdefghijklmnopqrstuvwxyz"             
password = ""                                   
length = int(input("How long will your password be?")) # Creates a random password
for x in range(length):
    rnd = random.randint(0,25)
    character = (alphabet[rnd])
    password = password + character                 
print(password)                                     

letters = []
for x in range(length): #Creates a list for letters in guess
    letters.append("a")


guess=""
attempts = 0
while guess != password:            #turns guess list into string
    guess = ""
    attempts = attempts + 1
    for x in letters:
        guess += x
        print(guess)
        break

item = length
while item > 0:
    for i in range(26):     #Alters the list for guesses 
        letters[item] = (alphabet[i])
        print (letters)
    item = item - 1
