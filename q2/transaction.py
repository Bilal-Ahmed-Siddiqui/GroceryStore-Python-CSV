import csv
from datetime import datetime

def load_transactions(transaction_file):
    transactions = []
    with open(transaction_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append({
                'date': row['date'],
                'time': row['time'],
                'id': int(row['id']),
                'quantity': int(row['quantity']),
                'payment': float(row['payment']),
            })
    return transactions

def save_transactions(transaction_file, transactions):
    with open(transaction_file, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'time', 'id', 'quantity', 'payment'])
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)

def add_transaction(transactions, grocery_id, quantity, payment):
    # Generate current date and time
    now = datetime.now()
    transaction_date = now.strftime("%d/%m/%Y")
    transaction_time = now.strftime("%I:%M:%S %p")

    new_transaction = {
        'date': transaction_date,
        'time': transaction_time,
        'id': grocery_id,
        'quantity': quantity,
        'payment': payment,
    }

    transactions.append(new_transaction)
def handle_transaction(groceries, transactions):
    while True: 
        print("\nAvailable Groceries:")
        for grocery_id, details in groceries.items():
            print(f"ID: {grocery_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")

        grocery_id_input = input("Enter grocery ID (or type 'exit' to cancel): ")
        if grocery_id_input.lower() == 'exit':
            print("Exiting the transaction entry.")
            return 

        try:
            grocery_id = int(grocery_id_input)
            if grocery_id not in groceries:
                print("Invalid grocery ID! Please try again.")
                continue  

            while True:  
                quantity_input = input("Enter quantity sold (or type 'exit' to cancel): ")
                if quantity_input.lower() == 'exit':
                    print("Exiting the transaction entry.")
                    return  

                quantity = int(quantity_input)
                if quantity > groceries[grocery_id]['stock']:
                    print("Not enough stock available! Please enter a valid quantity.")
                else:
                    break 

            total_price = groceries[grocery_id]['price'] * quantity
            print(f"The total amount to be paid is: {total_price:.2f}")

            while True: 
                payment_input = input("Enter payment received (or type 'exit' to cancel): ")
                if payment_input.lower() == 'exit':
                    print("Exiting the transaction entry.")
                    return 

                payment = float(payment_input)
                if payment < total_price:
                    print("Insufficient payment received! Please enter a valid payment.")
                else:
                    break 

            groceries[grocery_id]['stock'] -= quantity
            add_transaction(transactions, grocery_id, quantity, payment)
            print("Sales transaction recorded successfully!")

        except ValueError:
            print("Invalid input. Please enter the correct values.")

