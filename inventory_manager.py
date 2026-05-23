#this python file handles the inventory management of the store, including adding new items, updating stock levels, and removing items from the inventory.

import json
import os
from csv_importer import process_csv_file

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
        
        imports_folder = "imports"
        
        if not os.path.exists(imports_folder):
            print(f"No '{imports_folder}' folder found. Please create one and add CSV files to import.")
            input("Press Enter to return to the main menu...")
            break
        
        csv_files = [f for f in os.listdir(imports_folder) if f.lower().endswith('.csv')]
        
        if not csv_files:
            print(f"No CSV files found in the '{imports_folder}' folder. Please add files to import.")
            input("Press Enter to return to the main menu...")
            break
        
        print("Available CSV files:")
        for idx, file in enumerate(csv_files, start=1):
            print(f"{idx}. {file}")
            
        print("\n0. Back to Main Menu")
        
        choice = input("Enter the number of the CSV file to import: ").strip()
        if choice == '0':
            break
        
        try:
            choice_num = int(choice)
            if choice_num < 1 or choice_num > len(csv_files):
                print("Invalid choice. Please try again.")
                continue
            
            selected_file = csv_files[choice_num - 1]
            file_path = os.path.join(imports_folder, selected_file)
            
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the CSV file.")
            continue
        
        print(f"Processing '{selected_file}'...")
        report = process_csv_file(file_path, inventory)
        
        if "error" in report:
            print(report["error"])
            continue
        
        save_inventory(inventory)
        
        clear_screen()
        
        print(f"Import Report for '{selected_file}':")
        print(f"Rows Processed: {report['rows_processed']}")
        print(f"Items Updated: {report['items_updated']}")
        print(f"New Items Added: {report['new_items_added']}")
        
        if report['errors']:
            print("\nErrors:")
            for error in report['errors']:
                print(f"- {error}")
                
        input("\nPress Enter to return to the main menu...")
        break
    
                
        