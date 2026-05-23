#this python file handles the inventory management of the store, including adding new items, updating stock levels, and removing items from the inventory.

import json
import os

DATA_FILE = 'data/inventory_data.json'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    


def load_inventory():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error loading inventory data. Starting with an empty inventory.")
            return {}
    return {}


def save_inventory(inventory):
    with open(DATA_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)    
    
    
def add_new_item(inventory):
    while True:
        clear_screen()
        print("Add New Item to Inventory")
        print("\n0. Back to Main Menu")
        
        item_id = input("Enter Item ID (e.g SKU123): ").strip()
        if item_id == '0':
            break
        if item_id in inventory:
            print("Item ID already exists. Please try again.")
            continue
        
        name = input("Enter Item Name: ").strip()
        if name == '0':
            break
        
        quantity = input("Enter Quantity: ").strip()
        if quantity == '0':
            break
        
        try:
            quantity = int(quantity)
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue   
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue   
        
        inventory[item_id] = {
            'name': name,  
            'quantity': quantity
        }
        save_inventory(inventory)
        print(f"Item '{name}' added successfully!")
        break


def update_stock_levels(inventory):
    while True:
        clear_screen()
        print("Update Stock Levels")
        print("\n0. Back to Main Menu")
        
        item_id = input("Enter Item ID to update: ").strip()
        if item_id == '0':
            break   
        
        if item_id not in inventory:
            print("Item ID not found. Please try again.")
            continue   
        
        current_name = inventory[item_id]['name']
        current_quantity = inventory[item_id]['quantity']
        print(f"Current Name: {current_name} | Current Quantity: {current_quantity}")
        
        new_quantity = input("Enter New Quantity: ").strip()
        if new_quantity == '0':
            break
        
        try:
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue    
        
        inventory[item_id]['quantity'] = new_quantity
        save_inventory(inventory)
        print(f"Stock level for '{current_name}' updated successfully!")
        break
           
                
def remove_item(inventory):
    while True:
        clear_screen()
        print("Remove Item from Inventory")
        print("\n0. Back to Main Menu")
        
        item_id = input("Enter Item ID to remove: ").strip()
        if item_id == '0':
            break
        
        if item_id not in inventory:
            print("Item ID not found. Please try again.")
            continue
        
        item_name = inventory[item_id]['name']
        confirm = input(f"Are you sure you want to remove '{item_name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            del inventory[item_id]
            save_inventory(inventory)
            print(f"Item '{item_name}' removed successfully!")
            break
        else:
            print("Item removal cancelled.")
            break
        
             
def view_inventory(inventory):
    while True:
        clear_screen()
        print("Current Inventory")
        
        if not inventory:
            print("Inventory is empty.")
        else:
            print(f"{'Item ID':<15} {'Name':<30} {'Quantity'}")
            print("-" * 60)
            for item_id, details in inventory.items():
                print(f"{item_id:<15} {details['name']:<30} {details['quantity']}")
                        
        
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
                