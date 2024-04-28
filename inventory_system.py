'''f=open("D:\\coding\\test.txt")
a=input("this is a testing file")
f.write(a)
s=f.read()'''

# input_file_path = "D:\\coding\\test.txt"
# output_file_path = "D:\coding\\result.txt"

# with open("D:\\coding\\test.txt", 'r') as file:
#     lines = file.readlines()

# report_card = ""
# for idx, line in enumerate(lines):
#     data = line.strip().split(',')
#     student_id = idx + 1
#     name = data[0]
#     marks = list(map(int, data[1:]))
#     total_marks = sum(marks)
#     average_marks = total_marks / len(marks)

#     if average_marks >= 90:
#         grade = 'A'
#     elif average_marks >= 80:
#         grade = 'B'
#     elif average_marks >= 70:
#         grade = 'C'
#     elif average_marks >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'

#     report_card += f"ID: {student_id}\nName: {name}\nMarks: {', '.join(map(str, marks))}\nTotal Marks: {total_marks}\nAverage Marks: {average_marks:.2f}\nGrade: {grade}\n\n"

# with open("D:\\coding\\result.txt", 'w') as file:
#     file.write(report_card)


# import os
# import time
# from colorama import Fore, Back, Style
# USERNAME = "123"
# PASSWORD = "123"
# shop_items = {}
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')
# def login():
#     print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Admin
# Login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#     user = input(Fore.YELLOW + '👤 Enter your Username : ')
#     password = input('🔑 Enter your Password : ')
#     if user == USERNAME and password == PASSWORD:
#         print(Fore.GREEN + 'Login Success ✅')
#         time.sleep(1)
#         return True
#     else:
#         print(Fore.RED + "Invalid Username or Password")
#         return False
# def add_item():
#     global shop_items
#     item_id = int(input("Enter the Item ID : "))
#     item_name = input("Enter the name of the Item : ")
#     price = int(input("Enter the Price of the Item : ₹"))
#     quantity = int(input("Enter the Quantity available in Stock : "))
#     shop_items[item_id] = {
#         "name": item_name,
#         "price": price,
#         "quantity": quantity
#     }
#     print(Fore.GREEN + "Item Added Successfully!")
#     input("Press Enter to continue...")
#     show_menu()
# def show_items():
#     print(Fore.BLUE + f"Items Available for Sale ({len(shop_items)})")
#     print(Fore.YELLOW + "ID\tName\tPrice\tStock")
#     for key, value in shop_items.items():
#         print(f"
# {key}\t{value['name']}\t{value['price']}\t{value['quantity']}")
#     print(Style.RESET_ALL)
# def delete_item():
#     global shop_items
#     show_items()
#     item_to_delete = int(input("Enter Item Id : "))
#     if item_to_delete in shop_items:
#         del shop_items[item_to_delete]
#         print(Fore.RED + "Item Deleted Successfully!")
#     else:
#         print(Fore.RED + "No such Item Found.")
#     input("Press Enter to continue...")
#     show_menu()
# def update_item():
#     global shop_items
#     show_items()
#     item_id = int(input("Enter Item ID : "))
#     if item_id in shop_items:
#         name = input("Enter New Name (Optional): ")
#         if name:
#             shop_items[item_id]['name'] = name
#         price = float(input("Enter new Price (Optional): "))
#         if price:
#             shop_items[item_id]['price'] = price
#         quantity = int(input("Enter the number of items to add or
# remove (-ve/+ve).\nEnter 0 to skip: "))
#         if quantity:
#             shop_items[item_id]['quantity'] += quantity
#         print(Fore.GREEN + "Item Updated Successfully!")
#     else:
#         print(Fore.RED + "No such Item Found.")
#     input("Press Enter to continue...")
#     show_menu()
# def show_menu():
#     clear_screen()
#     print(Fore.BLUE + "Please select from the menu:\n")
#     print(Back.YELLOW + " Operation : Press ")
#     print(Style.RESET_ALL)
#     print(Fore.MAGENTA + "Add New Item : 1 ")
#     print("Delete Item : 2 ")
#     print("Update Item : 3 ")
#     print("View All Items : 4 ")
#     print(Fore.LIGHTBLUE_EX)
#     user_choice = input("\nEnter Your Choice (Number): ")
#     if user_choice == '1':
#         clear_screen()
#         add_item()
#     elif user_choice == '2':
#         clear_screen()
#         delete_item()
#     elif user_choice == '3':
#         clear_screen()
#         update_item()
#     elif user_choice == '4':
#         clear_screen()
#         show_items()
#         input("\nPress Enter to continue...")
#         show_menu()
#     else:
#         print(Fore.RED + "Invalid choice. Please try again.")
#         input("Press Enter to continue...")
#         show_menu()
# if __name__ == "__main__":
#     clear_screen()
#     print(Fore.YELLOW +
# "~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welocome to
# Shop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
#     if login():
#         show_menu()


inventory = {
        "A": {"name": "pineapple", "price": 20, "quantity": 5},
        "B": {"name": "Carrot", "price": 10, "quantity": 5},
        "C": {"name": "Guava", "price": 5, "quantity": 5},
    }

cart = {}
total_amount = 0

print("Welcome to the Supermarket!")

while True:
        print("\nAvailable Items:")

        for id, details in inventory.items():
            print(f"{id}: {details['name']} - ₹{details['price']} ({details['quantity']} in stock)")

        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '3']:

            id = input("Enter the ID of the item: ")

            if id in inventory:

                if choice == '1':
                    quantity_available = inventory[id]["quantity"]
                    quantity = int(input(f"Enter quantity (available: {quantity_available}): "))

                    if quantity <= quantity_available:
                        inventory[id]["quantity"] -= quantity
                        cart[id] = cart.get(id, 0) + quantity
                        total_amount += quantity * inventory[id]["price"]
                        print(f"{quantity} {inventory[id]['name']} added to cart!")

                    else:
                        print(f"Insufficient quantity of {inventory[id]['name']} available.")

                else:

                    if id in cart:
                        quantity_in_cart = cart[id]
                        quantity = int(input(f"Enter quantity to remove (in your cart: {quantity_in_cart}): "))

                        if quantity <= quantity_in_cart:
                            inventory[id]["quantity"] += quantity
                            cart[id] -= quantity
                            total_amount -= quantity * inventory[id]["price"]
                            if cart[id] == 0:
                                del cart[id]
                            print(f"{quantity} {inventory[id]['name']} removed from cart.")

                        else:
                            print(f"Insufficient quantity of {inventory[id]['name']} in your cart.")

                    else:
                        print(f"Item with ID '{id}' not found in your cart.")

        elif choice == '2':

            if not cart:
                print("Your cart is empty.")

            else:
                print("\nYour Cart:")
                for id, quantity in cart.items():
                    details = inventory[id]
                    print(f"{quantity} {details['name']} - ₹{details['price']} each")
                print(f"\nTotal Amount: ₹{total_amount}")

        elif choice == '4':

            if not cart:
                print("Your cart is empty. Please add items before checkout.")

            else:
                print("\nYour Cart:")
                for id, quantity in cart.items():
                    details = inventory[id]
                    print(f"{quantity} {details['name']} - ₹{details['price']} each")
                print(f"\nTotal Amount: ₹{total_amount}")
                print("You only have to use cash any other method is not allowed")
                print("Thank you for shopping!")
                break

        elif choice == '5':
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Please try again.")