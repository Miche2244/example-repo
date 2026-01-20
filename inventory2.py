
# Shoe Class


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"{self.country:10} | {self.code:10} | {self.product:15} | "
                f"Cost: {self.cost:<6} | Qty: {self.quantity}")


# Global Shoe List

shoes_list = []

# Functions


def read_shoes_data():
    """Reads inventory.txt and loads Shoe objects into shoes_list."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                if line.strip() == "":
                    continue
                country, code, product, cost, quantity = line.strip().split(",")
                shoes_list.append(Shoe(country, code, product, cost, quantity))
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("Error: inventory.txt not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def capture_shoes():
    """Allows user to input new shoe data."""
    country = input("Enter country: ")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")

    shoes_list.append(Shoe(country, code, product, cost, quantity))
    update_inventory_file()
    print("New shoe added successfully.")


def view_all():
    """Prints all shoes using __str__."""
    if not shoes_list:
        print("No shoes in inventory.")
        return

    print("\n=== ALL SHOES ===")
    for shoe in shoes_list:
        print(shoe)


def re_stock():
    """Finds shoe with lowest quantity and restocks it."""
    if not shoes_list:
        print("No shoes to restock.")
        return

    lowest = min(shoes_list, key=lambda s: s.quantity)
    print("\nLowest stock item:")
    print(lowest)

    choice = input("Restock this item? (yes/no): ").lower()
    if choice == "yes":
        add_qty = int(input("Enter quantity to add: "))
        lowest.quantity += add_qty
        update_inventory_file()
        print("Stock updated successfully.")
    else:
        print("Restock cancelled.")


def search_shoe():
    """Searches for a shoe by code."""
    code = input("Enter shoe code: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print("\nShoe found:")
            print(shoe)
            return
    print("Shoe not found.")


def value_per_item():
    """Calculates and prints value = cost * quantity for each shoe."""
    print("\n=== VALUE PER ITEM ===")
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product:15} | Code: {shoe.code:10} | Value: {value}")


def highest_qty():
    """Finds shoe with highest quantity and marks it for sale."""
    if not shoes_list:
        print("No shoes in inventory.")
        return

    highest = max(shoes_list, key=lambda s: s.quantity)
    print("\n=== HIGHEST QUANTITY — ON SALE ===")
    print(highest)


def update_inventory_file():
    """Writes updated shoe data back to inventory.txt."""
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


# Menu Loop


def main():
    read_shoes_data()

    while True:
        print("\n===== SHOE INVENTORY MENU =====")
        print("1 - View all shoes")
        print("2 - Add new shoe")
        print("3 - Restock lowest quantity")
        print("4 - Search shoe by code")
        print("5 - View value per item")
        print("6 - Highest quantity (for sale)")
        print("7 - Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
