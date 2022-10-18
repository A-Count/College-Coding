import ast

identify = []   #variables for later use
biggest = 0
VAT = 1.2

product = {}
name = []
ID = []
Department = []
Location = []
Stock = []
Price = []
Price_VAT = []

with open("Allsorts_Database.txt", "r") as file:
    info = file.read().rstrip("/n")



def system_menu():  #function to use menu
    global menu
    menu = int(input("""Welcome!
Press 1 to add a new product
Press 2 to store an existing product
Press 3 to change a value
Press 4 to remove a product
Press 5 to search for a product
Press 6 to view database
Press 7 to exit programme"""))

def product_input():    #function to input product details and create list name
    global product_name
    global list_name
    global department
    global location
    global quantity
    global price
    global price_VAT #makes variables global
    
    product_name = input("Please enter name of product") 
    list_name = product_name
    department = input("Please enter department product is from") 
    location = input("Please enter warehouse location of product") 
    quantity = int(input("Please enter amount of product in store"))
    price = int(input("Please enter price of product")) 
    price_VAT = price * VAT 
    
def dict_file():    #function to add data to dictionary, list and file
    list_name = [product_name.lower(), product_id, department, location, quantity, price, price_VAT]
    product[product_name.lower] = list_name
    with open("Allsorts_Database.txt","w") as f:
        for key, value in product.items():
            f.write("%s:%s" % (key,value))
            f.write("""
                    """)    
    f.close()

def search_func():
    global line_number
    global search
    search = input("Enter name of product")
    file = open("Allsorts_Database.txt","r")
    lines = file.readlines()
    for line in info.splitlines():
        if line.find(search) != -1:
            line_number = lines.index(line)
            

#    name.append(product_name)
#    ID.append(product_ID)
#    Department.append(department)
#    Location.append(location)
#    Stock.append(quantity)
#    Price.append(price)
#    Price_VAT.append(price_VAT)
#    file = open("Allsorts_Database","w")
#    file.write("Name:" + name)
#    file.write("ID:" + ID)
#    file.write("Department:" + Department)
#    file.write("Location:" + Location)
#    file.write("Stock:" + Stock)
#    file.write("Price:" + Price)
#   file.write("VAT:" + Price_VAT)
#    file.close
system_menu()

while menu != 7:
    if menu == 1:   #adding a new product to the database
        product_input()
        for x in identify:
            if int(x) > biggest:
                x = biggest
        product_id = biggest + 1 #making new ID num for product
        dict_file()

        system_menu()

    elif menu == 2: #adding an existing product to the database.
        product_input()
        product_id = input("Please enter product ID")
        identify.append(product_id)
        dict_file()
        
        system_menu()

    elif menu == 3:#updating a product in the database
        search_func()
        

    elif menu == 4:#removing a product from the database
        search_func()
        with open("Allsorts_Database.txt", "r") as read_file:
            lines = read_file.readlines()

            currentline = 1
        with open("Allsorts_Database","w") as write_file:
            for line in lines:
                if currentline == line_number:
                    pass
                else:
                    write_file.write(line)

                currentline + 1
        
        system_menu()
        
    elif menu == 5:#searching for a product in the database
        search_func()
        current_line = 1
        with open("Allsorts_Database.txt","r")as read_file:
            lines = read_file.readlines()
            for line in lines:
                if current_line == line_number:
                    print(current_line)
                else:
                    pass
                current_line + 1
        
        system_menu()

    elif menu == 6: #reading all data from database
        file = open("Allsorts_Database.txt","r")
        print(file.read())
        system_menu()
