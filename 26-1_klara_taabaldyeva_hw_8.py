import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_by_price_and_quantity_limit(conn):
    try:
        sql = '''SELECT * FROM products WHERE price <= 100 and quantity >= 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_by_product_name(conn, product_name):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+product_name+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


database = r'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''

connection = create_connection(database)
if connection is not None:
    print('Connected successfully')
    # create_table(connection, sql_create_products_table)
    # create_product(connection, ("Twix", 70.55, 215))
    # create_product(connection, ("Apple juice ", 119.99, 150))
    # create_product(connection, ("Banana bread", 59.50, 70))
    # create_product(connection, ("Bread", 49.50, 55))
    # create_product(connection, ("Milk", 90.99, 90))
    # create_product(connection, ("Cheese", 210.55, 65))
    # create_product(connection, ("Pen", 25.55, 365))
    # create_product(connection, ("Red pen", 30.50, 235))
    # create_product(connection, ("Coconut milk", 170.99, 65))
    # create_product(connection, ("Strawberry juice", 90.55, 120))
    # create_product(connection, ("Lay's crab", 135.55, 255))
    # create_product(connection, ("Pringles crab", 250.45, 245))
    # create_product(connection, ("Coca-Cola", 85.15, 350))
    # create_product(connection, ("Sprite", 85.15, 320))
    # create_product(connection, ("Fanta", 85.15, 290))
    # select_all_products(connection)
    # select_by_price_and_quantity_limit(connection)
    select_by_product_name(connection, 'milk')
    connection.close()
    print('DONE')
