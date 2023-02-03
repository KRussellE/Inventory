class Shoes():

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        # Constructor method: self, country, code, product, cost and quantity.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    '''
    Add the code to return the cost of the shoe in this method.
    '''
    # Method called: get_cost.
    def get_cost(self):
        return self.cost     # Return self.cost.

    '''
    Add the code to return the quantity of the shoes.
    '''    
    def get_quantity(self):
        return self.quantity    # Return self.quantity. 

    def __str__(self):
        return "{:<15} {:<15} {:<20} {:<15} {:<15}".format(self.country, self.code, self.product, self.cost, self.quantity) #return readbale string in a table format

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_object_list = []

#==========Functions outside the class==============
'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def read_shoes_data():      #adding shoe data to list as objects
    try:
        with open ('inventory.txt', 'r') as inventory_textfile:
            
            for row in inventory_textfile:  # split it at the commas after its converted into a list.
                row = row.replace('\n', '')
                row = row.split(',')

                shoe = Shoes(row[0], row[1], row[2], row[3], row[4])    #create a shoe object which will be appendend to the list
                shoe_object_list.append(shoe)
                
    except FileNotFoundError:
        print("File not found")


    
def capture_shoes():
    """
    this function will allow a user to capture
    data about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    """

    code_found = 1
    #read data from textfile to list   
    if len(shoe_object_list) == 0:
        read_shoes_data()
        
    #ask for user inputs to append to list
    country = input("\u001b[36mPlease enter country: \u001b[37m")
    code = input("\u001b[36mPlease enter code in format as follows 'SKU12345': \u001b[37m")
    while code_found == 1:      #check if code doesn't already exist
        for row in shoe_object_list:
            if code == row.code:
                code = input("\u001b[36mSKU already exists! Please enter code in format as follows 'SKU12345': \u001b[37m")
                code_found = 1
                break
            else:
                code_found = 0

    product = input("\u001b[36mPlease enter product name: \u001b[37m")  # Ask the user to enter the product name.
    while True:
        try:
            cost = int(input("\u001b[36mPlease enter product cost to the nearest whole number: \u001b[37m"))
            break
        except ValueError:
            print(" \u001b[31mOops! Invalid number, please try again.\u001b[37m")
            
    while True:
        try:
            quantity = int(input("\u001b[36mPlease enter quantity: \u001b[37m"))
            break
        except ValueError:
            print("\u001b[31mOops! Invalid number, please try again.\u001b[37m")
        
    
    shoe = Shoes(country, code, product, cost, quantity)    #create shoe object and append to list
    shoe_object_list.append(shoe)
    
    try:
        with open ('inventory.txt', 'w') as inventory_textfile:
            for row in shoe_object_list:
                inventory_textfile.write(str(row.country) + "," + str(row.code) + "," + str(row.product) + "," + str(row.cost) + "," + str(row.quantity) + "\n")
            print("\u001b[36m\n\tNew shoe data added!\u001b[37m" + "\n")
    except FileNotFoundError:
            print("\u001b[31mFile not found\u001b[37m")


    """"
    This function will iterate over all the shoes list and
    print the details of the shoes 
    """
def view_all():
    #shoe_object_list = []
    if len(shoe_object_list) == 0:
        read_shoes_data()   #read data from textfile to list
    for row in shoe_object_list:    #loop through list of objects and use str funtion to convert objects to readable data and print into a table format
        shoe = Shoes(row.country, row.code, row.product, row.cost, row.quantity)
        print(shoe.__str__())
        
    print("\n")

    
    """
    This function will find the shoe object with the
    lowest quantity, which is the shoes that need to be
    restocked. Ask the user if he wants to add the quantity of
    these shoes and then update it. This quantity is
    updated on the file.
    """
def re_stock():
    if len(shoe_object_list) == 0:    
        read_shoes_data()
    
    min_num = int(shoe_object_list[1].quantity)
    index = 1
    
    for row, value in enumerate(shoe_object_list):
        if row == 0:
            continue
        
        value.quantity = int(value.quantity)
        
        if value.quantity < min_num:    #checking which number is smaller and assigning that number to min variable
            min_num = value.quantity
            index = row

    print(f"\u001b[36mLowest stock is:\u001b[37m {shoe_object_list[index].product} Quantity: {shoe_object_list[index].quantity}\n")
    update_quantity = input("\u001b[36mWould you like to update the shoes quantity 'yes' or 'no'? \u001b[37m").lower()
    
    if update_quantity == "yes":    #if yes is selected allow user to enter number to replinish with and add this number to list and write to textfile
        while True:
            try:
                new_quantity = int(input("\u001b[36mWhat additional quantities would you like to add: \u001b[37m "))
                break
            except ValueError:
                print("\u001b[31mOops! Invalid number, please try again.\u001b[37m")           
        new_total = shoe_object_list[index].quantity + new_quantity
        shoe_object_list[index].quantity = new_total        
        try:
            with open ('inventory.txt', 'w') as inventory_textfile:
                for row in shoe_object_list:
                    inventory_textfile.write(str(row.country) + "," + str(row.code) + "," + str(row.product) + "," + str(row.cost) + "," + str(row.quantity) + "\n")               
                print("\u001b[36m\n\tQuantity updated\u001b[37m" + "\n")                
        except FileNotFoundError:
                print("\u001b[31mFile not found\u001b[37m")
    elif update_quantity == "no":   #if no quantity remains unchanged
        print("\u001b[31mQuantity unchanged\u001b[37m\n")
        
    else:
        print("\u001b[31mIncorrect input\u001b[37m\n")

    
    
def search_shoe():
    """
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be
    printed
    """
    shoe_not_found = 0
    if len(shoe_object_list) == 0:
        read_shoes_data()
        
    shoe_search = input("\u001b[36mEnter SKU you are searching for e.g.'SKU12345': \u001b[37m") # Program asks the user to type the code.
    x = 0
    # I corrected if now the user search by code not only the code will be found but the all details.
    for row in shoe_object_list:
        if x == 0:
            print(f"\u001b[36m{row}\u001b[37m")
            x += 1
    for row in shoe_object_list:
        if shoe_search == row.code:
            return row
            break
        else:  
            shoe_not_found = 1  #if shoe is not found set variable to 1          
    if shoe_not_found == 1:
        return "\u001b[31mShoe SKU not found!\u001b[37m"
    print("\n")
  

 
def value_per_item():
    """
    this function will calculate the total value
    for each item . (value = cost * quantity). Information printed on the
    console for all the shoes.
    """
    
    if len(shoe_object_list) == 0:
        read_shoes_data()
    print("{:<15} {:<20} {:<15}".format("Code", "Product","Value")) #printing inital headings   
    for row, value in enumerate(shoe_object_list):
        if row == 0:    #don't check the first column with titles
            continue
        value.quantity = int(value.quantity)
        value.cost = int(value.cost)
        print("{:<15} {:<20} R{:<15}".format(value.code, value.product, value.quantity*value.cost)) #print values in table format
    print("\n")



def highest_qty():
    """
    Product with the highest quantity is set on sale.
    """
    if len(shoe_object_list) == 0:
        read_shoes_data()       #read data from textfile to list 
    max_num = int(shoe_object_list[1].quantity)
    index = 1
    for row, value in enumerate(shoe_object_list):
        if row == 0:
            continue    
        value.quantity = int(value.quantity)
        if value.quantity > max_num:    #checking which number is smaller and assigning that number to min variable
            max_num = value.quantity
            index = row
    print(f"\u001b[36m{shoe_object_list[index].code}({shoe_object_list[index].product}) is on SALE!!!\u001b[37m\n")


#==========Main Menu======================================================
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
print("\u001b[32m\n\t\tINVENTORY\n\u001b[37m")
def main():
    while True:
        #presenting the menu to the user 
        menu = input('''Select one of the following Options below:
        \u001b[36m1\u001b[37m - Add new shoe
        \u001b[36m2\u001b[37m - View all shoes
        \u001b[36m3\u001b[37m - Restock shoe with lowest quantity
        \u001b[36m4\u001b[37m - Search for by SKU code
        \u001b[36m5\u001b[37m - Stock on database value
        \u001b[36m6\u001b[37m - Shoe to sale
        \u001b[36m0\u001b[37m - Exit
        : \n\n''').lower()  

        if menu == "1": #add new shoe to database
            print("\u001b[36m\tAdd new shoe\u001b[37m\n")
            capture_shoes()        
        elif menu == "2":   #view all shoes
            print("\u001b[36m\tView all shoes\u001b[37m\n")
            view_all()
        elif menu == "3":   #restock shoe with lowest quantity
            print("\u001b[36m\tRestock shoe with lowest quantity\u001b[37m\n")
            re_stock()
        elif menu == "4":  #search for a shoe
            print("\u001b[36m\tSearch for by SKU code\u001b[37m\n")
            print(f"\u001b[36m{search_shoe()} \u001b[37m\n")
        elif menu == "5":   #get value of stock on hand
            print("\u001b[36m\tStock on database value\u001b[37m\n")
            value_per_item()
        elif menu == "6":   #put a shoe on sale with highest quantity
            print("\u001b[36m\tShoe to sale\u001b[37m\n")
            highest_qty()
        elif menu == "0":   #exit
            print("\u001b[36mGoodbye!\u001b[37m")
            exit()
        else:
            print("You have made a wrong choice, Please Try again!")

if __name__=="__main__":
    main()