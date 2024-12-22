import mysql.connector
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dev123',
    'database': 'kads'
}
orderId = 2234
class Customer:
    def __init__(self, customer_id, full_name, email, contact_details, address_line1,
                 address_line2=None, address_line3=None, password=None):
        self.customer_id = customer_id
        self.full_name = full_name
        self.email = email
        self.contact_details = contact_details
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.password = password

def fetch_customer_by_email_password(email, password):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "SELECT CustomerID, FullName, Email, ContactDetails, AddressLine1, AddressLine2, AddressLine3, Password FROM customer WHERE Email = %s AND Password = %s"
        cursor.execute(query, (email, password))
        customer_data = cursor.fetchone()
        print(customer_data)
        if customer_data:
            return customer_data[0]
        else:
            print("Invalid email or password!")
            return None
    except mysql.connector.Error as error:
        print("Failed to log in:", error)
        return None
    finally:
        if 'connection' in locals() or 'connection' in globals():
            connection.close()

def display_products():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "SELECT ProductID, Name, Price FROM product"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            print(product)
    except mysql.connector.Error as error:
        print("Failed to fetch products:", error)
    finally:
        if 'connection' in locals() or 'connection' in globals():
            connection.close()


def create_order(customerID):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    try:
        cursor.execute("START TRANSACTION")

        # Lock the rows in the product table
        cursor.execute("SELECT * FROM  CART")
        items = cursor.fetchall()
        for item in items:
            print(item)
            productId = item[0]
            quantity = item[1]
            price = item[2]

            cursor.execute("SELECT MAX(SUBSTRING(OrderID, 2)) FROM ORDERS")
            last_order_id = cursor.fetchone()[0]
            if last_order_id:
                new_order_id = str(int(last_order_id) + 1).zfill(3)
            else:
                new_order_id = '001'

            current_time = datetime.now()
            order_time = current_time.strftime('%H:%M:%S')
            order_date = current_time.strftime('%Y-%m-%d')

            query = "INSERT INTO ORDERS (OrderID, OrderDetail, CustomerID, Status, PaymentMethod, OrderTime, OrderDate, OrderAmount, Quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
            new_order_id, productId, customerID, "pending", "card", order_time, order_date, price, quantity))
            # Reduce product's stock
            cursor.execute("UPDATE PRODUCT SET Stock = Stock - %s WHERE ProductID = %s", (quantity, productId))

        cursor.execute("COMMIT")

    except Exception as e:
        print("An error occurred:", e)
        cursor.execute("ROLLBACK")

    finally:
        cursor.close()
        connection.close()

def buy_gadgets(customer_id):
    while True:
        display_products()
        product_id = input("Enter product ID: ")
        quantity = int(input("Enter quantity: "))
        # Add product to cart and calculate cost
        add_to_cart(product_id, customer_id, quantity)
        choice = input("Press 'C' to continue shopping or 'X' to checkout: ")
        if choice.upper() == 'X':
            create_order(customer_id)
            break

def add_to_cart(product_id, customer_id, quantity):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "INSERT INTO cart (ProductID, Quantity, CustomerID) VALUES (%s, %s, %s)"
        cursor.execute(query, (product_id, quantity, customer_id))
        connection.commit()
        print("Product added to cart successfully!")
    except mysql.connector.Error as error:
        print("Failed to add product to cart:", error)
    finally:
        if 'connection' in locals() or 'connection' in globals():
            connection.close()

def delete_cart_table():
    connect = mysql.connector.connect(**DB_CONFIG)
    cursor = connect.cursor()
    cursor.execute("DROP TABLE IF EXISTS CART")
    connect.commit()
    cursor.close()
    connect.close()

def main():
    while True:
        print("\n1. SignUp")
        print("2. LogIn")
        print("3. Exit")
        delete_cart_table()
        choice = input("Enter your choice: ")
        if choice == '1':
            full_name = input("Enter full name: ")
            email = input("Enter email: ")
            contact_details = input("Enter contact details: ")
            address_line1 = input("Enter address line 1: ")
            address_line2 = input("Enter address line 2 (optional): ")
            address_line3 = input("Enter address line 3 (optional): ")
            password = input("Enter password: ")
            customer = Customer(full_name, email, contact_details, address_line1, address_line2, address_line3, password)
            customer.signup()
        elif choice == '2':
            email = input("Enter Email: ")
            password = input("Enter password: ")
            customerId = fetch_customer_by_email_password(email, password)
            if customerId:
                print("Logged in successfully!")
                while True:
                    connection = mysql.connector.connect(**DB_CONFIG)
                    cursor = connection.cursor()
                    cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS cart (
                                ProductID VARCHAR(60) NOT NULL,
                                Quantity BIGINT NOT NULL,
                                CustomerID VARCHAR(20) NOT NULL,
                                FOREIGN KEY (ProductID) REFERENCES PRODUCT(ProductID),
                                FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID)
                            )
                            """
                    )
                    connection.commit()
                    cursor.close()
                    print("\n1. Buy Gadgets")
                    print("2. Display Profile")
                    print("3. Logout")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        buy_gadgets(customerId)
                    elif choice == '2':
                        print(customerId)
                    elif choice == '3':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()