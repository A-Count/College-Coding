data = "Some Data"

def read():
    with open("data.txt", "r")as file:
        file.close()

def write():
    with open("data.txt", "w") as file:
        file.write(data + "\n")
        file.close

def append():
    with open("data.txt", "a")as file:
        file.write(data + "\n")
        file.close()

write()
append()
with open("data.txt", "a")as file:
    file.seek(1)
    file.write("First")
    file.close
