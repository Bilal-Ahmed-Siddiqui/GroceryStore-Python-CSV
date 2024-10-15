import csv

def load_groceries(grocery_file):
    groceries = {}
    with open(grocery_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            groceries[int(row['id'])] = {
                'name': row['name'],
                'price': float(row['price']),
                'stock': int(row['stock'])
            }
    return groceries

def save_groceries(grocery_file, groceries):
    with open(grocery_file, mode='w',  encoding='utf-8-sig',newline='') as file:
        fieldnames = ['id', 'name', 'price', 'stock']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for grocery_id, details in groceries.items():
            writer.writerow({
                'id': grocery_id,
                'name': details['name'],
                'price': details['price'],
                'stock': details['stock']
            })

def add_new_grocery(groceries):
    while True:
        new_id = len(groceries) + 1  
        name = input("Enter grocery name (or type 'exit' to cancel): ")
        if name.lower() == 'exit':
            print("Cancelled adding new grocery item.")
            return  

        while True:
            price_input = input("Enter grocery price (must be a positive number, or type 'exit' to cancel): ")
            if price_input.lower() == 'exit':
                print("Cancelled adding new grocery item.")
                return 
            try:
                price = float(price_input)
                if price <= 0:
                    print("Price must be a positive number. Please try again.")
                    continue
                break  
            except ValueError:
                print("Invalid input. Please enter a valid number for the price.")

        while True:
            stock_input = input("Enter stock quantity (must be a non-negative integer, or type 'exit' to cancel): ")
            if stock_input.lower() == 'exit':
                print("Cancelled adding new grocery item.")
                return 
            try:
                stock = int(stock_input)
                if stock < 0:
                    print("Stock quantity cannot be negative. Please try again.")
                    continue
                break 
            except ValueError:
                print("Invalid input. Please enter a valid integer for stock quantity.")
        
        groceries[new_id] = {
            'name': name,
            'price': price,
            'stock': stock
        }
        print(f"New grocery item '{name}' added successfully!")
        break 


def modify_grocery(groceries):
    while True:
        print("\nAvailable Groceries:")
        for grocery_id, details in groceries.items():
            print(f"ID: {grocery_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")

        grocery_id = input("Enter the grocery ID to modify (or type 'exit' to cancel): ").strip()
        if grocery_id.lower() == 'exit':
            print("Cancelled modifying grocery item.")
            return
        
        try:
            grocery_id = int(grocery_id)
        except ValueError:
            print("Invalid ID format. Please enter a valid integer ID.")
            continue

        if grocery_id not in groceries:
            print("Grocery ID not found! Please try again.")
            continue
        
        print(f"Current details of '{groceries[grocery_id]['name']}':")
        print(f"Price: {groceries[grocery_id]['price']}")
        print(f"Stock: {groceries[grocery_id]['stock']}")

        while True:
            new_price = input("Enter new price (press Enter to keep unchanged, or type 'exit' to cancel): ").strip()
            if new_price.lower() == 'exit':
                print("Cancelled modifying grocery item.")
                return
            
            if new_price:
                try:
                    groceries[grocery_id]['price'] = float(new_price)
                    break 
                except ValueError:
                    print("Invalid input. Please enter a valid number for the price.")
            else:
                break  

        while True:
            new_stock = input("Enter new stock (press Enter to keep unchanged, or type 'exit' to cancel): ").strip()
            if new_stock.lower() == 'exit':
                print("Cancelled modifying grocery item.")
                return
            
            if new_stock: 
                try:
                    groceries[grocery_id]['stock'] = int(new_stock)
                    break  
                except ValueError:
                    print("Invalid input. Please enter a valid integer for stock quantity.")
            else:
                break  

        print(f"Grocery item '{groceries[grocery_id]['name']}' updated successfully!")
        break  