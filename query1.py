import mysql.connector

def order_items():
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dev123",
            database="kads"
        )
        cursor = connect.cursor()

        while True:
            print("\nMenu:")
            print("1. Sort by price high to low")
            print("2. Sort by price low to high")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                cursor.execute("SELECT * FROM product ORDER BY price DESC")
            elif choice == '2':
                cursor.execute("SELECT * FROM product ORDER BY price ASC")
            elif choice == '3':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please enter again.")
                continue

            products = cursor.fetchall()

            print("\nProducts:")
            for product in products:
                print(product)

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if 'connect' in locals() and connect.is_connected():
            cursor.close()
            connect.close()


if __name__ == "__main__":
    order_items()
