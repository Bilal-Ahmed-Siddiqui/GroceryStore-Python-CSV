import numpy as np
import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

# Helper function to convert a transaction date string to a datetime object
def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%d/%m/%Y').date()

def display_monthly_sales(transactions, start_month, end_month):
    sales_by_month = defaultdict(lambda: [0, 0])

    start_month_date = datetime.datetime.strptime(start_month, '%m/%Y').date()
    end_month_date = datetime.datetime.strptime(end_month, '%m/%Y').date()

    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        month_year = transaction_date.strftime('%m/%Y')

        if start_month_date <= transaction_date <= end_month_date:
            sales_by_month[month_year][0] += transaction['payment']
            sales_by_month[month_year][1] += 1

    months = sorted(sales_by_month.keys())
    total_sales = [sales_by_month[month][0] for month in months]
    sales_count = [sales_by_month[month][1] for month in months]

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Month-Year')
    ax1.set_ylabel('Total Sales', color='tab:blue')
    ax1.plot(months, total_sales, color='tab:blue', label='Total Sales')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Sales', color='tab:red')
    ax2.plot(months, sales_count, color='tab:red', label='Number of Sales')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.suptitle('Monthly Sales and Number of Sales')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def display_product_sales(transactions, groceries, product_id, start_month, end_month):
    sales_by_month = defaultdict(lambda: [0, 0])  

    product_id = int(product_id)
    
    start_month_date = datetime.datetime.strptime(start_month, '%m/%Y').date()
    end_month_date = datetime.datetime.strptime(end_month, '%m/%Y').date()

    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        if transaction['id'] == product_id and start_month_date <= transaction_date <= end_month_date:
            month_year = transaction_date.strftime('%m/%Y')
            sales_by_month[month_year][0] += transaction['payment']
            sales_by_month[month_year][1] += 1

    months = sorted(sales_by_month.keys())
    total_sales = [sales_by_month[month][0] for month in months]
    sales_count = [sales_by_month[month][1] for month in months]

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Month-Year')
    ax1.set_ylabel('Total Sales', color='tab:blue')
    ax1.plot(months, total_sales, color='tab:blue', label='Total Sales')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Sales', color='tab:red')
    ax2.plot(months, sales_count, color='tab:red', label='Number of Sales')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    product_name = groceries[product_id]['name']
    fig.suptitle(f'Monthly Sales and Number of Sales for {product_name}')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def display_total_sales_by_product(transactions, groceries, start_date, end_date):
    sales_by_product = defaultdict(float)  

    start_date_obj = parse_date(start_date)
    end_date_obj = parse_date(end_date)

    for transaction in transactions:
        transaction_date = parse_date(transaction['date'])
        if start_date_obj <= transaction_date <= end_date_obj:
            product_id = transaction['id']
            sales_by_product[product_id] += transaction['payment']

    sorted_sales = sorted(sales_by_product.items(), key=lambda x: x[1], reverse=True)
    product_names = [groceries[prod_id]['name'] for prod_id, _ in sorted_sales]
    total_sales = [sales for _, sales in sorted_sales]

    plt.bar(product_names, total_sales, color='skyblue')
    plt.ylabel('Total Sales')
    plt.xlabel('Grocery Products')
    plt.title('Total Sales by Product (Sorted in Descending Order)')
    plt.xticks(rotation=45)  
    plt.tight_layout()
    plt.show()
