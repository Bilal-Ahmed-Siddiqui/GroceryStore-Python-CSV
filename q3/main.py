import auth  
import grocery 
import transaction  
import search
import graphs
import sys

def main():
    user_file = 'users.csv'

    if len(sys.argv) != 3:
        print("Usage: python script.py <transaction_file> <grocery_file>")
        sys.exit(1)  

    transaction_file = sys.argv[1]  # First argument for the transaction file
    grocery_file = sys.argv[2]  # Second argument for the grocery file

    groceries = grocery.load_groceries(grocery_file)
    transactions = transaction.load_transactions(transaction_file)
    
    groceries = grocery.load_groceries(grocery_file)
    transactions = transaction.load_transactions(transaction_file)

    print("Welcome to the Grocery Store Management System!")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    user_type = auth.authenticate_user(user_file, username, password)
    
    if user_type is None:
        print("Invalid username or password. Access denied.")
        return

    print(f"Login successful. You are logged in as a {user_type}.")
    
    while True:
        print("\nMain Menu:")
        print("1. Enter Sales Transaction")
        print("2. Search Sale Transactions/grocery")
        print("3. Display Sales Graphs")
        if user_type == 'manager':
            print("4. Add New Grocery Product")
            print("5. Modify Grocery Product")
        print("0. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            transaction.handle_transaction(groceries, transactions)

        elif choice == "2":
            # search menu loop
            while True:
                print("\nSearch Menu:")
                print("A. Search transaction by date")
                print("B. Search transaction by Product Name")
                print("C. Search transaction by Product Name and Date Range")
                print("D. Search Grocery by Name")
                print("0. Back to Main Menu")

                searchChoice = input("Enter your choice: ").strip().upper()

                if searchChoice == 'A':
                    date = input("Enter date (DD/MM/YYYY): ")
                    search.search_transactions_by_date(transactions, date)

                elif searchChoice == 'B':
                    query = input("Enter product name (partial or full): ")
                    search.search_transactions_by_product_name(transactions, groceries, query)

                elif searchChoice == 'C':
                    query = input("Enter product name (partial or full): ")
                    start_date = input("Enter start date (DD/MM/YYYY): ")
                    end_date = input("Enter end date (DD/MM/YYYY): ")
                    search.search_transactions_by_product_and_date_range(transactions, groceries, query, start_date, end_date)

                elif searchChoice == 'D':
                    query = input("Enter grocery name (partial or full): ")
                    search.search_grocery_by_name(groceries, query)

                elif searchChoice == '0':
                    print("Returning to Main Menu...")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "3":
            # Graph menu loop
            while True:
                print("\nGraph Menu:")
                print("A. Display Monthly Sales")
                print("B. Display Product Sales")
                print("C. Display Total Sales by Product")
                print("0. Back to Main Menu")

                graphChoice = input("Enter your choice: ").strip().upper()

                if graphChoice == 'A':
                    startDate = input("Enter start month (MM/YYYY): ")
                    endDate = input("Enter end month (MM/YYYY): ")
                    graphs.display_monthly_sales(transactions,startDate,endDate);

                elif graphChoice == 'B':
                    startDate = input("Enter start month (MM/YYYY): ")
                    endDate = input("Enter end month (MM/YYYY): ")
                    print("\nAvailable Groceries:")
                    for grocery_id, details in groceries.items():
                        print(f"ID: {grocery_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")
                    product_id = input("Enter Product Id: ")
                    graphs.display_product_sales(transactions,groceries, product_id, startDate,endDate)

                elif graphChoice == 'C':
                    startDate = input("Enter start date (DD/MM/YYYY): ")
                    endDate = input("Enter end date (DD/MM/YYYY): ")
                    graphs.display_total_sales_by_product(transactions, groceries, startDate, endDate)


                elif graphChoice == '0':
                    print("Returning to Main Menu...")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "4" and user_type == 'manager':
            grocery.add_new_grocery(groceries) 
            
        elif choice == "5" and user_type == 'manager':
            grocery.modify_grocery(groceries) 
            
        elif choice == "0":
            print("Saving and logging out...")
            transaction.save_transactions(transaction_file, transactions)
            grocery.save_groceries(grocery_file, groceries)
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()
