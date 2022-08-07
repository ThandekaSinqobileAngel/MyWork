#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This program is for managing Nike warehouse. It enables users to:
# Search products by code.
# Determine the product with the lowest quantity and restock it.
# Determine the product with the highest quantity.
# Calculate the value of each item entry, based on the quantity and cost of the
# item. The value is calculated by multiplying the cost by the quantity for each item entered.

from tabulate import tabulate
"""Tabulate module is imported for data to be organised"""

class Shoe:
    
    country = ""
    code = ""
    product = ""
    cost = ""
    quantity = ""
    for_sale = False
    total_value = 0
    
    def read_data(self):
        """This function opens file and reads data from the file
           If no file is available, user is informed."""
        
        shoes = []
        try:
            with open("inventory.txt", "r") as inventory_file:
                for i, line in enumerate(inventory_file):
                    if i > 0:
                        split_line = (line.replace("\n", "")).split(",")
                        shoe = Shoe()
                        shoe.country = split_line[0]
                        shoe.code = split_line[1]
                        shoe.product = split_line[2]
                        shoe.cost = split_line[3]
                        shoe.quantity = split_line[4]
                        shoe.value_per_item()
                        shoes.append(shoe)
        except FileNotFoundError:
            print("Inventory file not found")
        read_list_to_file(shoes)
        return shoes

    def mark_for_sale(self, is_for_sale):
        """is_for_sale is set to True"""
        self.for_sale = is_for_sale

    def value_per_item(self):
        """Calculates item total value"""
        self.total_value = int(self.cost) * int(self.quantity)


def lowest_quantity(shoes):
    """Determines the product with the lowest amount in stock and asks
    user how much stock they would like to add. Then adds user value
    to stock of item and calls value_per_item() to reads new values to
    a text file with read_list_to_file()."""

    quantity = []

    for shoe in shoes:
        quantity.append(int(shoe.quantity))
    lowest_total = min(quantity)
    index = quantity.index(lowest_total)
    draw_line()
    print("{} has the least amount of stock.\nTotal Stock: \t{}"
          .format(shoes[index].product, lowest_total))

    draw_line()
    user_input = input("Enter restock amount: \n>")
    while not user_input.isnumeric():
        draw_line()
        user_input = input("Incorrect entry!\n"
                           "Enter restock amount again: \n>")

    lowest_total = lowest_total + int(user_input)
    shoes[index].quantity = str(lowest_total)
    shoes[index].value_per_item()
    read_list_to_file(shoes)
    draw_line()
    print("{} restocked.\nTotal Stock {}".format(shoes[index].product,
                                                 lowest_total))
    draw_line()


def highest_quantity(shoes):
    """Determines the product with the highest amount in stock and sets
    the items for_sale value to True"""

    quantities = []

    for shoe in shoes:
        quantities.append(int(shoe.quantity))

    highest_total = max(quantities)
    index = quantities.index(highest_total)
    shoes[index].mark_for_sale(True)

    draw_line()
    print("{} has the most amount of stock and has been marked for sale!"
          "\nTotal Stock: \t{}".format(shoes[index].product,
                                       highest_total))
    draw_line()


def read_list_to_file(shoes):
    """Reads values of a list of Shoe() objects to text file."""

    with open("inventory.txt", "w") as inventory_file:
        inventory_file.write("Country,Code,Product,Cost,Quantity,Value\n")
        for i, shoe in enumerate(shoes):
            shoe.value_per_item()
            new_line = (",".join([shoe.country, shoe.code, shoe.product,
                                  shoe.cost, shoe.quantity,
                                  (str(shoe.total_value) + "\n")]))
            inventory_file.write(new_line)


def display_data():
    """Reads data from text file to a list and prints the data to
    console in a readable manner using tabulate module"""

    table = []
    try:
        with open("inventory.txt", "r") as inventory_file:
            for i, line in enumerate(inventory_file):
                new_line = str(i) + "," + (line.replace("\n", ""))
                table.append(new_line.split(","))
    except FileNotFoundError:
        print("Inventory file not found!")
    print(tabulate(table[1:], headers=table[0][1:], tablefmt="github"))


def locate_item(shoes):
    """Locates shoe in list with corresponding code and returns the shoe"""

    draw_line()
    user_code = (input("Enter the code of the product you are"
                       " looking for:\n").lower()).replace("sku", "")
    draw_line()
    for shoe in shoes:
        if shoe.code.replace("SKU", "") == user_code:
            print("Requested Product: \n")
            print(tabulate([[shoe.code, shoe.country, shoe.product,
                             shoe.quantity]],
                           headers=["Code", "Country", "Product",
                                    "Quantity"],
                           tablefmt="github"))
            draw_line()
            return shoe
    print("Product not found!")


def draw_line():
    """Displays line to console"""
    print("-" * 80)


"""Menu is displayed to the user to choose from. If user enters an incorrect
   value. Appropriate message is displayed, until correct value entry is made"""

shoe_list = Shoe().read_data()

while True:
    print(("*" * 37) + " PRODUCT LIST " + ("*" * 37))
    display_data()
    draw_line()
    menu = input("What would you like to do?\n"
                 "(Enter the corresponding number)\n"
                 "1 - Search product by code\n"
                 "2 - Mark product with most stock as for sale\n"
                 "3 - Restock product with least stock\n"
                 "\n0 - Quit\n")

    if menu == "1":
        locate_item(shoe_list)
    elif menu == "2":
        highest_quantity(shoe_list)
    elif menu == "3":
        lowest_quantity(shoe_list)
    elif menu == "0":
        draw_line()
        print("Thank you for using this program")
        draw_line()
        break
    else:
        draw_line()
        print("No option selected!")


# In[ ]:





# In[ ]:





# In[ ]:




