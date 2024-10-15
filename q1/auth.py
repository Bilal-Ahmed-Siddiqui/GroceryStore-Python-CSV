import csv

def authenticate_user(user_file, username, password):
    with open(user_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return row['type'] 
    return None
