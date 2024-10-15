import auth  
import grocery 
import transaction  
import search
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
        if user_type == 'manager':
            print("3. Add New Grocery Product")
            print("4. Modify Grocery Product")
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


        elif choice == "3" and user_type == 'manager':
            grocery.add_new_grocery(groceries) 
            
        elif choice == "4" and user_type == 'manager':
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
