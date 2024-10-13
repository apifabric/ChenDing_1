import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    """Description: Stores customer details."""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)

class Address(Base):
    """Description: Stores customer addresses."""
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)

class Order(Base):
    """Description: Stores orders placed by customers."""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    date_placed = Column(DateTime, default=datetime.datetime.now)
    total_amount = Column(Float, nullable=True)

class Product(Base):
    """Description: Stores information about products."""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

class OrderDetail(Base):
    """Description: Stores details of each product in an order."""
    __tablename__ = 'order_details'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

class Supplier(Base):
    """Description: Stores supplier information."""
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)

class Inventory(Base):
    """Description: Tracks inventory for products."""
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)

class Shipment(Base):
    """Description: Tracks shipments to customers."""
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    shipment_date = Column(DateTime, nullable=False)

class Payment(Base):
    """Description: Stores payment information for orders."""
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)

class Feedback(Base):
    """Description: Stores customer feedback for orders."""
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    comments = Column(String, nullable=True)

class Employee(Base):
    """Description: Stores information about employees."""
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    hire_date = Column(DateTime, default=datetime.datetime.now)

class StoreLocation(Base):
    """Description: Stores the locations of company stores."""
    __tablename__ = 'store_locations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, nullable=False)

# Database setup
DATABASE_URI = 'sqlite:///system/genai/temp/create_db_models.sqlite'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

# Sample data insertions using ORM
Session = sessionmaker(bind=engine)
session = Session()

# Creating some sample data
customer1 = Customer(name='John Doe', email='john.doe@example.com', phone='123-456-7890')
customer2 = Customer(name='Jane Smith', email='jane.smith@example.com', phone='098-765-4321')

address1 = Address(customer_id=1, street='123 Elm St', city='Somewhere', state='CA', zip_code='90210')
address2 = Address(customer_id=2, street='456 Oak Ave', city='Anywhere', state='TX', zip_code='73301')

product1 = Product(name='Laptop', description='A high-performance laptop', price=999.99)
product2 = Product(name='Mouse', description='Wireless mouse', price=25.99)

order1 = Order(customer_id=1, total_amount=1025.98)
order2 = Order(customer_id=2, total_amount=25.99)

order_detail1 = OrderDetail(order_id=1, product_id=1, quantity=1)
order_detail2 = OrderDetail(order_id=1, product_id=2, quantity=1)
order_detail3 = OrderDetail(order_id=2, product_id=2, quantity=1)

supplier1 = Supplier(name='Tech Corp', contact_name='Alice Adams', phone='232-212-9202')

inventory1 = Inventory(product_id=1, quantity_in_stock=50)
inventory2 = Inventory(product_id=2, quantity_in_stock=200)

shipment1 = Shipment(order_id=1, shipment_date=datetime.datetime.now())

payment1 = Payment(order_id=1, amount_paid=1025.98, payment_date=datetime.datetime.now())

feedback1 = Feedback(order_id=1, customer_id=1, comments='Great service!')

employee1 = Employee(name='Mark Employee', position='Sales Manager')

store_location1 = StoreLocation(address='789 Main Rd, Smalltown, NY')

# Add instances to session and commit
session.add_all([
    customer1, customer2,
    address1, address2,
    product1, product2,
    order1, order2,
    order_detail1, order_detail2, order_detail3,
    supplier1, inventory1, inventory2,
    shipment1, payment1, feedback1,
    employee1, store_location1
])
session.commit()
session.close()
