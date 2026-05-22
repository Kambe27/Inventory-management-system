#this python file handles the inventory management of the store, including adding new items, updating stock levels, and removing items from the inventory.

import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def display_menu():
    print("Inventory Management System")
    print("1. Add New Item")
    print("2. Update Stock Levels")
    print("3. Remove Item")
    print("4. View Inventory")
    print("5. Bulk Import from CSV")
    print("6. Exit")
    

def load_inventory():
    print("Loading inventory...")
    
    return{}

def save_inventory(inventory):
    print("Saving inventory...")    
    
    
def add_new_item(inventory):
    while True:
        clear_screen()
        print("Add New Item to Inventory")
        print("\n0. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def update_stock_levels(inventory):
    while True:
        clear_screen()
        print("Update Stock Levels")
        print("\n0. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
                
def remove_item(inventory):
    while True:
        clear_screen()
        print("Remove Item from Inventory")
        print("\n0. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
                
def view_inventory(inventory):
    while True:
        clear_screen()
        print("Current Inventory")
        print("\n0. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
                
def bulk_import(inventory):
    while True:
        clear_screen()
        print("Bulk Import from CSV")
        print("\n0. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
                
def main():
    clear_screen()
    inventory = load_inventory()
    
    while True:
        print("\n")
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        clear_screen()
        if choice == '1':
            add_new_item(inventory)
        elif choice == '2':
            update_stock_levels(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            view_inventory(inventory)
        elif choice == '5':
            bulk_import(inventory)
        elif choice == '6':
            save_inventory(inventory)
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()