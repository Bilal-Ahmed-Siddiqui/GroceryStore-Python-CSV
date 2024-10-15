import auth  
import grocery  
import transaction  
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
        if user_type == 'manager':
            print("2. Add New Grocery Product")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            transaction.handle_transaction(groceries, transactions)

        elif choice == "2" and user_type == 'manager':
            grocery.add_new_grocery(groceries) 
            
        elif choice == "3":
            print("Saving and logging out...")
            transaction.save_transactions(transaction_file, transactions)
            grocery.save_groceries(grocery_file, groceries)
            break
        
        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()
