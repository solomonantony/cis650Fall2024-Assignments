#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Your name diner") #edit to show your name
    print("__________")
    print('D for Drinks order')
    print('A for Appetizers order')
    print('S for Salads order')
    print('E for Entrees order')
    print('T for Desserts order')
    print('C for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Cc':
      close_order()
    else:
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    show_main_menu()


