import datetime

# Helper function to check for partial case-insensitive matches
def is_match(query, text):
    return query.lower() in text.lower()

def search_transactions_by_date(transactions, date):
    try:
        date_obj = datetime.datetime.strptime(date, '%d/%m/%Y').date()
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")
        return

    matching_transactions = [t for t in transactions if datetime.datetime.strptime(t['date'], '%d/%m/%Y').date() == date_obj]
    
    if matching_transactions:
        print(f"Transactions on {date}:")
        for t in matching_transactions:
            print(t)
    else:
        print(f"No transactions found on {date}.")

def search_transactions_by_product_name(transactions, groceries, query):
    matching_transactions = []

    for transaction in transactions:
        grocery_name = groceries[transaction['id']]['name']  
        if is_match(query, grocery_name):
            matching_transactions.append(transaction)

    if matching_transactions:
        print(f"Transactions for product matching '{query}':")
        for t in matching_transactions:
            print(t)
    else:
        print(f"No transactions found for product matching '{query}'.")

def search_transactions_by_product_and_date_range(transactions, groceries, query, start_date, end_date):
    try:
        start_date_obj = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
        end_date_obj = datetime.datetime.strptime(end_date, '%d/%m/%Y').date()
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")
        return

    matching_transactions = []

    for transaction in transactions:
        grocery_name = groceries[transaction['id']]['name']
        transaction_date = datetime.datetime.strptime(transaction['date'], '%d/%m/%Y').date()
        if is_match(query, grocery_name) and start_date_obj <= transaction_date <= end_date_obj:
            matching_transactions.append(transaction)

    if matching_transactions:
        print(f"Transactions for product matching '{query}' between {start_date} and {end_date}:")
        for t in matching_transactions:
            print(t)
    else:
        print(f"No transactions found for product matching '{query}' in the given date range.")

def search_grocery_by_name(groceries, query):
    matching_groceries = {grocery_id: details for grocery_id, details in groceries.items() if is_match(query, details['name'])}

    if matching_groceries:
        print(f"Grocery products matching '{query}':")
        for grocery_id, details in matching_groceries.items():
            print(f"ID: {grocery_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")
    else:
        print(f"No grocery products found matching '{query}'.")
