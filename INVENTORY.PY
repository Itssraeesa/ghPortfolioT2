#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Initializing attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Return the cost of the shoe
        return self.cost

    def get_quantity(self):
        # Return the quantity of the shoes
        return self.quantity

    def __str__(self):
        # Return a string representation of the class
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skipping the first line (header)
            for line in file:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("The file inventory.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_shoes():
    # Capturing shoe data from user input
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    
    # Create a new shoe object
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

def view_all():
    # View all shoes in the list
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    # Find the shoe with the lowest quantity
    lowest_stock_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"Restock needed for: {lowest_stock_shoe}")
    
    # Ask user for the new quantity to restock
    restock_amount = int(input(f"How many {lowest_stock_shoe.product} do you want to add? "))
    lowest_stock_shoe.quantity += restock_amount
    print(f"Updated quantity: {lowest_stock_shoe.quantity}")

def search_shoe():
    # Search for a shoe by code
    search_code = input("Enter the shoe code to search for: ")
    for shoe in shoe_list:
        if shoe.code == search_code:
            print(shoe)
            return
    print("Shoe not found.")

def value_per_item():
    # Calculate the total value for each shoe
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} - Total Value: {value}")

def highest_qty():
    # Find the shoe with the highest quantity
    highest_stock_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"Shoe with highest quantity: {highest_stock_shoe}")

#==========Main Menu=============
def main_menu():
    while True:
        print("\nShoe Inventory Menu")
        print("1. Read shoes data from file")
        print("2. Capture new shoe data")
        print("3. View all shoes")
        print("4. Restock shoes")
        print("5. Search shoe by code")
        print("6. Calculate value per item")
        print("7. Find shoe with highest quantity")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
