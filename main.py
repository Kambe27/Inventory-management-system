from inventory_manager import *


def display_menu():
    print("Inventory Management System")
    print("1. Add New Item")
    print("2. Update Stock Levels")
    print("3. Remove Item")
    print("4. View Inventory")
    print("5. Bulk Import from CSV")
    print("6. Exit")


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