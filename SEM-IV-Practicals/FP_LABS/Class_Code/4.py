# Write a class train which has methods to book a ticket, get status(no. of seats) and get fare information of tarins running under indian railways

class Train:
    def __init__(self, train_name, total_seats):
        self.train_name = train_name
        self.total_seats = total_seats
        self.booked_seats = 0
        self.fare_per_seat = 100

    def book_ticket(self, num_seats):
        if self.booked_seats + num_seats > self.total_seats:
            print("Sorry, requested number of seats not available.")
        else:
            self.booked_seats += num_seats
            print(f"{num_seats} seats booked successfully!")

    def get_status(self):
        print(f"{self.total_seats - self.booked_seats} seats available.")

    def get_fare_info(self):
        print(f"Fare per seat: {self.fare_per_seat}")


train = Train("Rajdhani Express", 100)
train.get_status()  # 100 seats available.
train.book_ticket(20)  # 20 seats booked successfully!
train.get_status()  # 80 seats available.
train.get_fare_info()  # Fare per seat: 100
