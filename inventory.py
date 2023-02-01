# ========The beginning of the class==========
# function that initialises the following attributes: country, code, product, cost, and quantity.
class Shoe:

	def __init__(self, country, code, product, cost, quantity):
		self.country = country
		self.code = code
		self.product = product
		self.cost = cost
		self.quantity = quantity

	# this code returns the cost of the shoe
	def get_cost(self):
		return self.cost

	# this code returns the quantity of the shoes
	def get_quantity(self):
		return self.quantity

	# this code returns the country
	def get_country(self):
		return self.country

	# this code returns the code
	def get_code(self):
		return self.code

	# this code returns the country
	def get_product(self):
		return self.product

	# this code returns a string representation of a class
	def __str__(self):
		return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

	def __repr__(self):
		return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


# ==========Functions outside the class==============
# =============Shoe list===========
# The list will be used to store a list of objects of shoes.
shoe_list = []


def read_shoes_data():
	# This function will open the file inventory.txt and read the data from this file.
	# A shoes object is created with the data. This object is then appended into the shoes list.
	try:
		with open('inventory.txt', 'r+') as f:
			shoe_data = f.readlines()
			for lines in shoe_data[1:]:
				data = lines.strip("\n").split(",")
				current_shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
				shoe_list.append(current_shoe)
			return shoe_list


	except FileNotFoundError:
		print("This file does not exist. Try again!")


def capture_shoes():
	# This function allows a user to capture data about a shoe.
	# The data is used to create a shoe object, and it's then appended inside the shoe list.

	shoe_country = input("Please enter the country the shoe was made: \n")
	shoe_code = input("Please enter the product code of the shoe: \n")
	shoe_product = input("Please enter the product name: \n")
	while True:
		try:
			shoe_cost = int(input("Please enter the cost of the shoe (numbers only please): \n"))
			shoe_quantity = int(input("Please enter the quantity of shoe (numbers only please): \n"))
			break
		except ValueError:
			print("Please enter an integer")

	new_inventory = Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)
	shoe_list.append(new_inventory)

	with open('inventory.txt', 'a+') as f:
		for line in shoe_list:
			f.write(f"\n{line.country},{line.code},{line.product},{line.cost},{line.quantity}")
		print("The new shoe data was successful added to the inventory. Thanks!")


def view_all():
	# This function iterates over the shoes list.
	# It then prints the details of the shoes returned from the __str__  function.
	read_shoes_data()
	for line in shoe_list:
		print(
			f"Country: {line.country}\nCode: {line.code}\nProduct: {line.product}\nCost: {line.cost}\nQuantity: {line.quantity}\n")


def re_stock():
	# This function finds the shoe object with the lowest quantity.
	# The object with the lowest stock is then re-stocked.
	# This quantity is updated on the file for this shoe.
	read_shoes_data()
	lowest_quantity = int(shoe_list[0].quantity)
	shoe_position = 0
	for count, i in enumerate(shoe_list):
		if int(i.quantity) <= lowest_quantity:
			lowest_quantity = int(i.quantity)
			shoe_position = count
	print(f"The shoe with the lowest quantity is: {shoe_list[shoe_position]}")

	while True:
		try:
			new_stock = int(input("To restock the lowest quantity shoe, please enter the new stock quantity: "))
			shoe_list[shoe_position].quantity = new_stock
			break
		except ValueError:
			print("Please enter an integer")

	with open('inventory.txt', 'w+') as f:
		f.write("Country,Code,Product,Cost,Quantity")
		for line in shoe_list:
			f.write(f"\n{line.country},{line.code},{line.product},{line.cost},{line.quantity}")
		print("The new shoe data was successful added to the inventory. Thanks!")


def search_shoe():
	read_shoes_data()
	# This function will search for a shoe from the list using the shoe code.
	# And returns this object so that it will be printed.
	while True:
		shoe_search = input("Please enter the code of the shoe you want to search: ")
		for line in shoe_list:
			if line.get_code() == shoe_search:
				print(line)
				break
		else:
			print("Incorrect code. Try again")


def value_per_item():
	read_shoes_data()
	# This function will calculate the total value for each item.
	# This formula will be used: value = cost * quantity.
	# The total value for each time is then printed out on the console for all the shoes.
	for line in shoe_list:
		total_value = (int(line.get_cost())) * (int(line.get_quantity()))
		print(f"The total value of item with code {line.get_code()} is R{total_value}")


def highest_qty():
	read_shoes_data()
	# This code determines the product with the highest quantity and prints this shoe as being for sale.
	highest_quantity = int(shoe_list[0].quantity)
	shoe_position = 0
	for count, i in enumerate(shoe_list):
		if int(i.quantity) >= highest_quantity:
			highest_quantity = int(i.quantity)
			shoe_position = count
	print(f"The item: {shoe_list[shoe_position]} is now on SALE!")


# #==========Main Menu=============
# Menu inside a while loop that executes each function above.

menu_string = '''====Stock taking Menu====
1 - Read shoes data
2 - Capture shoes data
3 - View all shoes
4 - Restock lowest quantity shoe
5 - Search for a shoe
6 - Total value per item
7 - Highest quantity 
0 - Exit
Please select one of the following options above:  '''

while True:
	menu = input(menu_string)
	if menu == '1':
		read_shoes_data()
	elif menu == '2':
		capture_shoes()
	elif menu == '3':
		view_all()
	elif menu == '4':
		re_stock()
	elif menu == '5':
		search_shoe()
	elif menu == '6':
		value_per_item()
	elif menu == '7':
		highest_qty()
	elif menu == "0":
		print("Goodbye")
		break
	# this error message is printed when the wrong letter is selected from the menu
	else:
		print("You have made a wrong choice, Please Try again.")