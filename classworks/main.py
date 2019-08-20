import config
import mysql.connector

def get_products():
    con = mysql.connector.connect(**config.config)

    cursor = con.cursor()

    query = "SELECT product_name, price, title, description " \
            "FROM product JOIN category ON product.category = category.id " \
            "WHERE product.price > %s ORDER by product.price DESC"

    price = 0

    cursor.execute(query, (price, ))

    for (name, price, category, descr) in cursor:
        print(name, price, category, descr)
    cursor.close()
    con.close()

def set_new_products():
    con = mysql.connector.connect(**config.config)

    cursor = con.cursor()

    query = "UPDATE product SET product_name = %s WHERE product.id = 3"
    values = ("New name", )
    cursor.execute(query, values)

    con.commit()
    cursor.close()
    con.close()

set_new_products()