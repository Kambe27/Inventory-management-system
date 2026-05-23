import csv
import os

def process_csv_file(file_path, inventory):
    if not os.path.exists(file_path):
        return{"File not found."}
    
    report = {
        "rows_processed": 0,
        "items_updated": 0,
        "new_items_added": 0,
        "errors": []
    }
    
    try:
        with open (file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            if reader.fieldnames:
                reader.fieldnames = [str(h).strip().lower() for h in reader.fieldnames]
                
                for row_num, row in enumerate(reader, start=2):
                    report["rows_processed"] += 1
                    
                    item_id = row.get('sku', '').strip().upper()
                    name = row.get('name', '').strip()
                    quantity_str = row.get('quantity', '').strip()
                    
                    if not item_id:
                        report["errors"].append(f"Row {row_num}: Missing SKU.")
                        continue
                    
                    try:
                        quantity = int(quantity_str)
                        if quantity < 0:
                            report["errors"].append(f"Row {row_num}: Quantity cannot be negative.")
                            continue
                    except ValueError:
                            report["errors"].append(f"Row {row_num}: Invalid quantity '{quantity_str}'.")
                            continue
                        
                    if item_id in inventory:
                        inventory[item_id]['quantity'] = quantity
                        report["items_updated"] += 1
                    else:
                        inventory[item_id] = {
                            'name': name if name else "Unknown Item",
                            'quantity': quantity
                        }
                        report["new_items_added"] += 1
                        
        return report
    except Exception as e:
        return {"An error occurred while processing the file: " + str(e)}