import database
#
# def menu():
#     print("""
#     Please select one of the following options:
#     [1] Display stock levels
#
#     """)
#
#     selected_option = int(input())
#     print(f"Your selection option is {selected_option}")
#     return selected_option
#
# def run():
#     selected = menu()
#     if selected == 1:
#         database.display_products_with_stock_levels()
#     else:
#         print("cant display")

#
# def menu():
#
#     print("""
#     Please select one of the following options:
#     [1] Display stock levels
#     [2] Display suppliers
#
#     """)
#     selection_option = int(input())
#     print(f"Your selection option : {selection_option}")
#     return selection_option
#
# def run():
#     selection_option = menu()
#     if selection_option == 2:
#         database.display_product_supplier()
#     else:
#         print("cant display ")

# def menu():
#     print("""
#     Please select one of the following options:
#     [1] Display stock levels
#     [2] Display suppliers
#     [3] Display supplier locations
#     """)
#     selection_option = int(input())
#     print(f"Your selection : {selection_option}")
#     return selection_option
#
#
# def run():
#     selection_option = menu()
#     if selection_option == 3:
#         database.display_product_supplier_locations()
#     else:
#         print("cant display message")
#
#
# run()

# def menu():
#     print("""
#     Please select one of the following functions:
#     [1] Display stock level
#     [2] Display supplier
#     [3] Display supplier location
#     [4] Display missing suppliers
#     """)
#     selection_option = int(input())
#     print(f"Your selection option is : {selection_option}")
#     return selection_option
#
# def run():
#     selection_option = menu()
#     if selection_option == 4:
#         database.display_product_missing_suppliers()
#     else:
#         print("cant display ")
#
# run()

def menu():
    print("""
    please select one of the following functions:
    [1] Display stock level
    [2] Display supplier 
    [3] Display supplier location
    [4] Display missing suppliers
    
     """)

    selection_option = int(input())
    print("Your selection_option is = {}", format(selection_option))
    return selection_option


def run():
    selection_option = menu()
    if selection_option == 5:
        database.display_supplier_missing_product()
    else:
        print("cant display")


run()



