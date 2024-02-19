import sys

class HotelReservation:
    RESTAURANT_MENU = {
        1: {"name": "water", "price": 20},
        2: {"name": "tea", "price": 10},
        3: {"name": "breakfast combo", "price": 90},
        4: {"name": "lunch", "price": 110},
        5: {"name": "dinner", "price": 150}
    }

    LAUNDRY_OPTIONS = {
        1: {"name": "Shorts", "price": 3},
        2: {"name": "Trousers", "price": 4},
        3: {"name": "Shirt", "price": 5},
        4: {"name": "Jeans", "price": 6},
        5: {"name": "Girlsuit", "price": 8}
    }

    GAME_SELECTIONS = {
        1: {"name": "Table tennis", "price": 60},
        2: {"name": "Bowling", "price": 80},
        3: {"name": "Snooker", "price": 70},
        4: {"name": "Video games", "price": 90},
        5: {"name": "Pool", "price": 50}
    }

    def init(self):
        """
        Initialize HotelReservation instance with default values.
        """
        print("\n\n*WELCOME TO HEWING HOTEL*\n")
        self.room_rent = 0
        self.food_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        self.additional_charges = 1800
        self.room_number = 101

    def input_data(self):
        """
        Collect customer data including name, address, check-in date, and check-out date.
        """
        self.name = input("\nEnter your name: ")
        self.address = input("\nEnter your address: ")
        self.check_in_date = input("\nEnter your check-in date: ")
        self.check_out_date = input("\nEnter your check-out date: ")
        print("Your room no.:", self.room_number, "\n")
        self.room_number += 1

    def calculate_room_rent(self):
        """
        Calculate room rent based on the selected room type and number of nights stayed.
        """
        print("We have the following rooms for you:-")
        print("1. Type A - Rs 6000 PN")
        print("2. Type B - Rs 5000 PN")
        print("3. Type C - Rs 4000 PN")
        print("4. Type D - Rs 3000 PN")

        room_type = int(input("Enter Your Choice Please: "))
        nights_stay = int(input("For How Many Nights Did You Stay: "))

        room_prices = {1: 6000, 2: 5000, 3: 4000, 4: 3000}

        if room_type in room_prices:
            self.room_rent = room_prices[room_type] * nights_stay
            print(f"You have opted room type {chr(65 + room_type - 1)}")
        else:
            print("Invalid room choice.")

        print("Your room rent is =", self.room_rent, "\n")

    def calculate_restaurant_bill(self):
        """
        Calculate food bill based on the selected items from the restaurant menu.
        """
        print("*RESTAURANT MENU*")
        for key, value in self.RESTAURANT_MENU.items():
            print(f"{key}. {value['name']} ----> Rs {value['price']}")

        while True:
            choice = int(input("Enter your choice (6 to exit): "))
            if choice == 6:
                break
            elif choice in self.RESTAURANT_MENU:
                quantity = int(input("Enter the quantity: "))
                self.food_bill += self.RESTAURANT_MENU[choice]["price"] * quantity
            else:
                print("Invalid option")

        print("Total food Cost = Rs", self.food_bill, "\n")

    def calculate_laundry_bill(self):
        """
        Calculate laundry bill based on the selected items from the laundry menu.
        """
        print("**LAUNDRY OPTIONS*")
        for key, value in self.LAUNDRY_OPTIONS.items():
            print(f"{key}. {value['name']} ----> Rs {value['price']}")

        while True:
            choice = int(input("Enter your choice (6 to exit): "))
            if choice == 6:
                break
            elif choice in self.LAUNDRY_OPTIONS:
                quantity = int(input("Enter the quantity: "))
                self.laundry_bill += self.LAUNDRY_OPTIONS[choice]["price"] * quantity
            else:
                print("Invalid option")

        print("Total Laundry Cost = Rs", self.laundry_bill, "\n")

    def calculate_game_bill(self):
        """
        Calculate game bill based on the selected items from the game menu.
        """
        print("**GAME SELECTIONS*")
        for key, value in self.GAME_SELECTIONS.items():
            print(f"{key}. {value['name']} ----> Rs {value['price']}")

        while True:
            choice = int(input("Enter your choice (6 to exit): "))
            if choice == 6:
                break
            elif choice in self.GAME_SELECTIONS:
                hours = int(input("No. of hours: "))
                self.game_bill += self.GAME_SELECTIONS[choice]["price"] * hours
            else:
                print("Invalid option")

        print("Total Game Bill = Rs", self.game_bill, "\n")

    def show_total_cost(self):
        """
        To show the total cost including room rent, food bill, laundry bill, additional charges, and grand total.
        """
        total_cost = self.room_rent + self.food_bill + self.laundry_bill + self.game_bill + self.additional_charges
        print("**HOTEL BILL**")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check-in date:", self.check_in_date)
        print("Check-out date:", self.check_out_date)
        print("Room no.:", self.room_number - 1)
        print("Your Room rent is:", self.room_rent)
        print("Your Food bill is:", self.food_bill)
        print("Your Laundry bill is:", self.laundry_bill)
        print("Your Game bill is:", self.game_bill)
        print("Your subtotal bill is:", total_cost - self.additional_charges)
        print("Additional Service Charges is:", self.additional_charges)
        print("Your grand total bill is:", total_cost)

def main():
    """
    Main function to initialize HotelReservation instance and handle user interactions.
    """
    hotel_reservation = HotelReservation()
    
    while True:
        print("1. Enter Customer Data")
        print("2. Calculate Room Rent")
        print("3. Calculate Restaurant Bill")
        print("4. Calculate Laundry Bill")
        print("5. Calculate Game Bill")
        print("6. Show Total Cost")
        print("7. EXIT")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            hotel_reservation.input_data()
        elif choice == 2:
            hotel_reservation.calculate_room_rent()
        elif choice == 3:
            hotel_reservation.calculate_restaurant_bill()
        elif choice == 4:
            hotel_reservation.calculate_laundry_bill()
        elif choice == 5:
            hotel_reservation.calculate_game_bill()
        elif choice == 6:
            hotel_reservation.show_total_cost()
        elif choice == 7:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == '_main_':
    main()
