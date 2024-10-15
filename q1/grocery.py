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
        new_id = len(groceries) + 1  # Generate a new ID as an integer
        
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

