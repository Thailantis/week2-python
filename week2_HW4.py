# Turn the shopping cart program from yesterday into an object-oriented program
# The comments in the cell below are there as a guide for thinking about the problem. 
# However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.
# Create a class called cart that retains items and has methods to add, remove, and show

  class Cart(): 
  def __init__ (self):
        self.items = {}
        
    def add_items(self, item, quantity):
        if item in self.items:
            self.items[item] +=quantity
        else:
            self.items[item] = quantity
    print(f" {quantity} {item} has been added to your shopping list.")
    
    def delete_items(self, item, quantity):
        if item in self.items:
            if quantity < self.items[item]:
                self.items[item] -= quantity
            print(f"You removed {quantity} {item}s from your cart")
        elif quantity == self.items[item]:
            del self.items[item]
            print(f"You removed {item} from your cart")
        else:
            print(f"You don't have {quantity} {item}s in your cart")
        else:
            print(f"You don't have {item} in your cart")
            
    def show_list(self):
        if not self.items:
            print("Your cart is empty")
        else:
            print("Your cart: ")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
if __name__ == '__main__':                
    cart = Cart()
    
    while True:
        print("Enter 'add' to add an item to your cart")
        print("Enter 'remove' to remove an item to your cart")
        print("Enter 'show' to show your current items in the cart")
        print("Enter 'quit' to exit the Superstore USA program")
        
    choice = input("What would you like to do?")
    
    if choice == "add":
        item = input("What would you like to buy? ")
        quantity = int(input("How many would you like? "))
        cart.add_item(item, quantity)
        
    elif choice == "delete":
        item = input("What would you like to remove? ")
        quantity = int(input("How many would you like to remove? "))
        cart.remove_item(item, quantity)
        
    elif choice == "show":
        cart.show_items()
        
    elif choice == "quit":
        print("Thanks for shopping with us! Come Again!")
        break
    
    else:
        print("You're weird moron. Please try again!")
    
print("Your final cart: ")
cart.show_items()

# 2. Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

class PythonString:
    
    def __init__(self, string):
        self.string = ""
        
    def get_String(self):
        while not self.string:
            self.string = input("Please enter your string: ")
        
    def print_String(self):
        if self.string:
            print(self.string.upper())
        else:
            print("No string has been entered")
            
string_manipulator = PythonString()
string_manipulator.get_String
string_manipulator.print_String
