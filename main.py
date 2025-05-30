def display_menu(menu):
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item} - {price} PKR")

def take_order(menu):
    total = 0
    while True:
        item = input("\nEnter item name to order (or type 'done' to finish): ").strip().title(break)
        if item.lower() == 'done':
            break
        if item in menu:
            try:
                quantity = int(input(f"Enter quantity for {item}: "))
                total += menu[item] * quantity
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print("Item not found in the menu. Please try again.")
    return total

def main():
    desi_menu = {
        "Chapati": 20,
        "Karahi": 400,
        "Biryani": 300,
        "Daal": 150
    }

    italian_menu = {
        "Pizza": 800,
        "Pasta": 600,
        "Lasagna": 700,
        "Bruschetta": 300
    }

    chinese_menu = {
        "Fried Rice": 350,
        "Manchurian": 400,
        "Noodles": 300,
        "Spring Rolls": 200
    }

    print("Select Cuisine Type:")
    print("1. Desi\n2. Italian\n3. Chinese")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        menu = desi_menu
        print("\nYou selected Desi cuisine.")
    elif choice == '2':
        menu = italian_menu
        print("\nYou selected Italian cuisine.")
    elif choice == '3':
        menu = chinese_menu
        print("\nYou selected Chinese cuisine.")
    else:
        print("Invalid choice. Exiting program.")
        return

    display_menu(menu)
    total_bill = take_order(menu)
    print(f"\nYour total bill is: {total_bill} PKR")

if __name__ == "__main__":
    main()
