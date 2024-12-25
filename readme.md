# Online Store Project - B2C Application

## Project Overview

This project represents the creation of a **B2C online store** designed to manage a product catalog, customer orders, and inventory. The store supports essential e-commerce features, including customer registration, order placement, and inventory management. This application can be customized for different types of stores, such as a **music store**, **bookstore**, or similar product-focused businesses.

### Key Features:
- **User Registration & Login**: Customers can create accounts and log in to view their order history and account details.
- **Product Catalog**: Customers can browse products, search by categories, and view product details.
- **Order Management**: Users can add products to their cart, place orders, and view their order history.
- **Payment Processing**: Customers can select a payment method, and the system processes the order.
- **Inventory Management**: The system tracks product availability and updates stock levels accordingly.
- **Admin Panel**: Admin users can manage products, track orders, and view customer details.

## Project Scope

This online store project is designed to handle core e-commerce functions:
- **Browsing Products**: Customers can view a list of available products, filter them by categories or keywords, and get detailed product information.
- **Placing Orders**: Customers can add products to their shopping cart and proceed to checkout to complete an order.
- **Order History**: Customers can view their previous orders and the current status of each order.
- **Admin Management**: Admin users can manage the inventory by adding, updating, or removing products and can also view and manage customer orders.

### Entity Relationship Diagram (ERD)

The ERD represents the key entities in the application and their relationships. It includes:

- **Entities**: Customer, Product, Order, OrderItem, Payment, Admin, Inventory
- **Relationships**: A customer can place multiple orders; each order contains multiple products. The inventory is updated when products are ordered, and admins can manage these entities.

## Database Schema

### Tables

1. **Customers**:
   - Stores customer information, including name, email, and password.
  
2. **Products**:
   - Stores information about products available for sale, including name, description, price, and stock level.

3. **Orders**:
   - Stores order information, linking to the customer and containing the order date and status.

4. **OrderItems**:
   - Records the details of products in each order, including product ID, quantity, and price.

5. **Payments**:
   - Tracks payment information for each order, including the payment method and status.

### SQL Queries

Several SQL queries are used to interact with the database, including:
- **Selecting products**: Retrieve a list of all available products.
- **Updating inventory**: Adjust stock levels when orders are placed.
- **Summing order revenue**: Calculate the total revenue from customer orders.

## Triggers

### Trigger 1: Update inventory after an order is placed
A trigger is used to automatically adjust the stock levels in the `Products` table when an item is ordered. This ensures the inventory reflects real-time changes when orders are placed.

### Trigger 2: Prevent placing an order if there are unpaid orders
A trigger checks if a customer has any unpaid orders before allowing them to place a new order. If there are unpaid orders, the new order is blocked.

## Embedded SQL in Application

### Ordering Items
The application allows customers to place orders by selecting products from the catalog. When an order is placed, the system records the details of the order and updates the inventory accordingly.

### Customer Analysis
Admin users can run analysis queries to review customer orders, total revenue, or inventory status. This helps in making informed decisions regarding restocking and promotions.

## Transactions

### Non-Conflicting Transactions
These transactions run without issues, such as:
- **Inserting a new customer**: Adding a new customer to the system without any conflicts.
- **Updating product inventory**: Decreasing the stock level after a successful sale.

### Conflicting Transactions
These transactions involve conflicting operations, such as:
- **Two customers ordering the last item**: When two customers attempt to purchase the same last available product, the system handles the conflict and prevents overselling.
  
## User Guide

### Features

1. **Registration & Login**:
   - Customers can register with their name, email, and password. After registration, they can log in to access their order history and personal account details.

2. **Product Catalog**:
   - The store offers a wide selection of products that customers can browse. Customers can search for products by category, name, or description.

3. **Placing Orders**:
   - Once products are added to the shopping cart, customers can proceed to checkout. They select a payment method, confirm the order, and track its progress.

4. **Admin Panel**:
   - Admin users can manage the product catalog by adding new products, updating existing ones, and removing outdated products. They can also manage customer orders and update payment statuses.

### How to Run the Application

1. **Set Up the Database**:
   - Set up the required database schema by running the provided SQL commands. Ensure the database is connected to the application.
   
2. **Install Dependencies**:
   - Install necessary libraries or dependencies based on the programming language being used (e.g., `sqlite3` for Python).

3. **Run the Application**:
   - Start the application and use the provided user interface to browse products, place orders, and manage customer accounts.

4. **Admin Functions**:
   - Admin users can log in to manage products, track orders, and view customer details from the admin panel.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact Information

For any questions or feedback, feel free to reach out:

- **Krishna Shukla**
- **Email**: kriishukla@gmail.com
