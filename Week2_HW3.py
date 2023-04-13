# Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# Note: Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

shopping_list = []

def add_items():
  item = input("What would you like to buy? ")
  shopping_list.append(item)
  print(f"{item} has been added to your shopping list.")

def delete_items():
  item = input("What would you like to remove? ")
  if item in shopping_list:
    shopping_list.remove(item)
    print(f"{item} has been removed from your grocery list")
  else:
    print(f"Sorry! the {item} is not in your grocery list")
    
def show_list():
  print("Here is your current shopping list")
  for item in shopping_list:
    print(item)

def ask_user():
  while True:
    action = inpout("Do you want to: Show/Add/Delete or Quit?")
    if action.lower() == "add":
      add_item()
    elif action.lower() == "delete":
      delete_item()
    elif action.lower() == "show":
      delete_item()
    elif action.lower() == "quit":
      break
    else:
      print("Sorry! I have no idea what you are trying to do. Please enter either Show, Add, Delete, or Quit.")
 ask_user()
 
 print("Here is your final shopping list:")
 for item in shopping_list:
    print(item)
