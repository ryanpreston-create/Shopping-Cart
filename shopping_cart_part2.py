"""
Online Shopping Cart - Final Portfolio Project
Implements ItemToPurchase and ShoppingCart classes with an interactive menu.
"""

SALES_TAX_RATE = 0.06875  # 6.875% sales tax


class ItemToPurchase:
    """Represents a single item a customer wants to buy."""

    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        """Print the item's line total in the form: Name Qty @ $Price = $Total."""
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    def print_item_description(self):
        """Print the item's name and description."""
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """Holds a customer's items and provides cart operations."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Add an ItemToPurchase object to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Remove the item whose name matches item_name, if it exists."""
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        """Update an existing item using non-default values from item_to_purchase."""
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """Return the total quantity of all items in the cart."""
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """Return the total cost of all items in the cart."""
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        """Print each item's cost, the cart total, sales tax, and grand total."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        subtotal = self.get_cost_of_cart()
        tax = round(subtotal * SALES_TAX_RATE, 2)
        print(f"\nTotal: ${subtotal:.2f}")
        print(f"Sales tax ({SALES_TAX_RATE * 100:.3f}%): ${tax:.2f}")
        print(f"Grand total: ${subtotal + tax:.2f}")

    def print_descriptions(self):
        """Print each item's description."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def get_positive_number(prompt, cast):
    """Prompt until the user enters a valid non-negative number of the given type."""
    while True:
        try:
            value = cast(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please try again.")


def print_menu(cart):
    """Display the menu and process commands until the user quits."""
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    command = ""
    while command != "q":
        print(menu)
        command = input("Choose an option:\n").strip().lower()

        if command == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = get_positive_number("Enter the item price:\n", float)
            quantity = get_positive_number("Enter the item quantity:\n", int)
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif command == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif command == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = get_positive_number("Enter the new quantity:\n", int)
            temp_item = ItemToPurchase(name=name, quantity=quantity)
            cart.modify_item(temp_item)

        elif command == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif command != "q":
            print("Invalid option. Please choose a, r, c, i, o, or q.")


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
