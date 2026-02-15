"""" Compute Sales Module
CLA-T-1201 - A01796592 - Assignment 5.2 - Problem 1
This module contains the compute_sales function which calculates the total
sales for a given list of transactions.
"""
import sys
import time
import json


class ComputeSales:
    """Class to compute total sales from a list of transactions."""
    def __init__(self, p_list, transactions):
        self.dict_product = p_list
        self.dict_transactions = transactions

    def total_sales(self):
        """Calculate the total sales from the transactions."""
        total_transaction = 0
        try:
            self.validate_transactions()
            for transaction in self.dict_transactions:
                product_name = transaction["Product"]
                quantity = transaction["Quantity"]
                price = next(
                    (p["price"] for p in self.dict_product
                        if p["title"] == product_name), None)
                if price is None:
                    raise ValueError(
                        f"Product not found: {product_name}")
                total_transaction += quantity * price
        except ValueError as exc:
            raise ValueError(f'Invalid transaction data: {exc}') from exc
        return total_transaction

    def validate_transactions(self):
        """Validate that all transactions are numbers."""
        if not self.dict_transactions:
            raise ValueError("The list of transactions is empty.")
        valid_products = {
            p["title"] for p in self.dict_product
        }
        filtered_transactions = []
        for transaction in self.dict_transactions:
            if transaction["Product"] in valid_products:
                filtered_transactions.append(transaction)
        self.dict_transactions = filtered_transactions


if __name__ == "__main__":
    start_time = time.time()
    products_file = sys.argv[1]
    sales_file = sys.argv[2:]
    with open(products_file, 'r', encoding='utf-8') as f1:
        product_list = json.load(f1)
    with open('sales_result.txt', 'w', encoding='utf-8') as report:
        report.write('Sales File\t\tTotal Sales\n')
        print("Sales file\t\tTotal Sales")
        for sales in sales_file:
            try:
                with open(sales, 'r', encoding='utf-8') as f2:
                    sales_list = json.load(f2)
                compute_sales = ComputeSales(product_list, sales_list)
                total = compute_sales.total_sales()
                report.write(f'{sales}\t{total}\n')
                print(f'{sales}\t{total}')
            except (ValueError, FileNotFoundError) as exc:
                print(f'Error processing file: {exc}')
    end_time = time.time()
    print('Sales report generated: sales_result.txt')
    print(f'Time taken: {end_time - start_time:.2f} seconds')
