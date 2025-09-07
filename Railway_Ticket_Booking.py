import random
import string

class Train:
    """
    A class to represent a Train in Indian Railways.   Provides methods to book tickets, check seat availability, get fare information, and retrieve ticket details by PNR.
    """

    def __init__(self, train_name, total_seats, fare):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare = fare
        self.booked_tickets = {}  # Store tickets with PNR as key

    def generate_pnr(self):  #Generate a random 6-character alphanumeric PNR
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def book_ticket(self):  #Book a ticket if seats are available.
        if self.available_seats > 0:
            print("\n--- Ticket Booking ---")
            name = input("Enter Passenger Name: ").strip()
            age = input("Enter Age: ").strip()
            source = input("Enter Source Station: ").strip()
            destination = input("Enter Destination Station: ").strip()

            # Generate PNR and update seat count
            self.available_seats -= 1
            pnr = self.generate_pnr()

            ticket = {
                "PNR": pnr,
                "Passenger Name": name,
                "Age": age,
                "Train Name": self.train_name,
                "From": source,
                "To": destination,
                "Fare": self.fare,
                "Seat No": self.total_seats - self.available_seats
            }

            # Save ticket in dictionary
            self.booked_tickets[pnr] = ticket

            print(f"\n✅ Ticket Booked Successfully for {name}!")
            self.print_ticket(ticket)

        else:
            print("❌ Sorry, No seats available!")

    def get_status(self):  #Show train seat availability status.
        print("\n--- Train Status ---")
        print(f"Train Name     : {self.train_name}")
        print(f"Total Seats    : {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")

    def get_fare_info(self):  #Show fare information of the train.
        print("\n--- Fare Information ---")
        print(f"Train Name : {self.train_name}")
        print(f"Fare       : Rs.{self.fare} per passenger")

    def check_ticket_by_pnr(self, pnr):  #Retrieve ticket details using PNR.
        ticket = self.booked_tickets.get(pnr)
        if ticket:
            print("\n--- Ticket Details ---")
            self.print_ticket(ticket)

        else:
            print("❌ No ticket found with this PNR!")

    def print_ticket(self, ticket):  #Print formatted ticket details.
        print("--------------------------------------")
        for key, value in ticket.items():
            print(f"{key:<15}: {value}")
        print("--------------------------------------")


# Example trains
train1 = Train("Mumbai Express", 5, 250)
train2 = Train("Delhi Rajdhani", 3, 1200)

while True:
    print("\n========= Indian Railways =========")
    print("1. Book a Ticket")
    print("2. Get Train Status")
    print("3. Get Fare Information")
    print("4. Check Ticket by PNR")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nSelect Train: 1. Mumbai Express  2. Delhi Rajdhani")
        train_choice = input("Enter train number: ")
        if train_choice == "1":
            train1.book_ticket()
        elif train_choice == "2":
            train2.book_ticket()
        else:
            print("Invalid Train Choice!")

    elif choice == "2":
        print("\nSelect Train: 1. Mumbai Express  2. Delhi Rajdhani")
        train_choice = input("Enter train number: ")
        if train_choice == "1":
            train1.get_status()
        elif train_choice == "2":
            train2.get_status()
        else:
            print("Invalid Train Choice!")

    elif choice == "3":
        print("\nSelect Train: 1. Mumbai Express  2. Delhi Rajdhani")
        train_choice = input("Enter train number: ")
        if train_choice == "1":
            train1.get_fare_info()
        elif train_choice == "2":
            train2.get_fare_info()
        else:
            print("Invalid Train Choice!")

    elif choice == "4":
        pnr = input("Enter your PNR: ").strip().upper()
        found = False

         # Check in train1
        if pnr in train1.booked_tickets:
            train1.check_ticket_by_pnr(pnr)
            found = True

         # Check in train2
        elif pnr in train2.booked_tickets:
            train2.check_ticket_by_pnr(pnr)
            found = True

        if not found:
            print("❌ No ticket found with this PNR!")

    elif choice == "5":
        print("🚆 Thank you for using Indian Railways!")
        break

    else:
        print("❌ Invalid choice, please try again.")

