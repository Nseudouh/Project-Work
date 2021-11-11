import sqlite3
# column_product = 0
# column_description =1
# quantity = 0
#
# def display_products_with_stock_levels():
#     db = sqlite3.connect("catalogue2.db")
#     cursor = db.cursor()
#     sql = "SELECT name, description, quantity " \
#           "FROM product " \
#           "NATURAL JOIN stock"
#     cursor.execute(sql)
#     record = cursor.fetchall()
#     print(record)
#     print(f"There are {len(record)}records in the catalogue")
#     for value in record:
#         print(f"Product: {value[column_product]}")
#         print(f"Description : {value[column_description]}")
#         print(f"quantity ; {value[quantity]}")
#     db.close()

# display_products_with_stock_levels()
#
# def display_product_supplier():
#     db = sqlite3.connect("catalogue2.db")
#     cursor = db.cursor()
#     sql = "SELECT product.name, supplier.name " \
#            "FROM product " \
#            "INNER JOIN supplier ON product.supplier_id = supplier.supplier_id;"
#     cursor.execute(sql)
#     records = cursor.fetchall()
#
#     for value in records:
#         print("The supplier for each product are as follows :")
#         print(f"Product; {value[0]}, Supplier ; {value[1]}")
#
#     db.close()
#
# display_product_supplier()

# def display_product_supplier_locations():
#     db = sqlite3.connect("catalogue2.db")
#     cursor = db.cursor()
#     sql = "SELECT product.name, supplier.name, location.city, location.country " \
#           "FROM PRODUCT " \
#           "INNER JOIN supplier ON product.supplier_id = supplier.supplier_id " \
#           "INNER JOIN location ON supplier.location_id = location.location_id "
#     cursor.execute(sql)
#     records = cursor.fetchall()
#     for values in records:
#         print("The supplier for each products are as follows :")
#         print(f"Product name: {values[0]}, Supplier: {values[1]}, Supplier location : {values[3]}")

def display_product_missing_suppliers():
    db= sqlite3.connect("catalogue2.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name"\
          "FROM PRODUCT "\
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.supplier_id "
    cursor.execute(sql)
    records = cursor.fetchall()
    for values in records:
        print("The supplier for each products are as follows: ")
        print(f"product name : {values[0]}, Supplier: {values[1]} ")

    db.close()







