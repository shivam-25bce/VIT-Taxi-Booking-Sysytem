
#User/Driver login and password Data

users = ["user1", "user2"]
user_passwords = ["123", "456"]

drivers = ["driver1", "driver2"]
driver_passwords = ["111", "222"]

bookings = []   # store bookings as list of dictionaries



# User Login

def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for i in range(len(users)):
        if users[i] == username and user_passwords[i] == password:
            print("User login successful!")
            user_menu(username)
            return
    print("Invalid user login!")



# Driver Login

def driver_login():
    username = input("Driver username: ")
    password = input("Password: ")

    for i in range(len(drivers)):
        if drivers[i] == username and driver_passwords[i] == password:
            print("Driver login successful!")
            driver_menu(username)
            return
    print("Invalid driver login!")



# User Menu
def user_menu(username):
    while True:
        print("\n--- USER MENU ---")
        print("1. Book Taxi")
        print("2. View My Bookings")
        print("3. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            book_taxi(username)
        elif ch == "2":
            view_user_bookings(username)
        elif ch == "3":
            break
        else:
            print("Invalid choice!")



# Taxi Booking
def book_taxi(username):
    print("\nChoose Route:")
    print("1. VIT → Bhopal Jn (₹700)")
    print("2. VIT → Rani Kamlapati (₹600)")
    print("3. VIT → Sehore (₹500)")

    ch = input("Enter choice: ")

    if ch == "1":
        route = "VIT to Bhopal Junction"
        fare = 700
    elif ch == "2":
        route = "VIT to Rani Kamlapati"
        fare = 600
    elif ch == "3":
        route = "VIT to Sehore"
        fare = 500
    else:
        print("Invalid route!")
        return

    booking = {
        "user": username,
        "route": route,
        "fare": fare,
        "status": "Pending"
    }

    bookings.append(booking)

    print("\nTaxi Booked Successfully!")
    print("Route:", route)
    print("Fare:", fare)


# User booking
def view_user_bookings(username):
    print("\n--- YOUR BOOKINGS ---")
    for b in bookings:
        if b["user"] == username:
            print(b)


# Driver Menu
def driver_menu(driver_name):
    while True:
        print("\n--- DRIVER MENU ---")
        print("1. View All Trips")
        print("2. Update Trip Status")
        print("3. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            view_all_trips()
        elif ch == "2":
            update_trip_status()
        elif ch == "3":
            break
        else:
            print("Invalid choice!")



# Trips 
def view_all_trips():
    print("\n--- ALL BOOKINGS ---")
    for b in bookings:
        print(b)


# Status update option
def update_trip_status():
    route = input("Enter route name to update: ")

    for b in bookings:
        if b["route"] == route:
            new = input("Enter new status (Accepted/Completed): ")
            b["status"] = new
            print("Status updated!")
            return

    print("Route not found!")



#Main menu
def main():
    while True:
        print("\n==== VIT BHOPAL TAXI SERVICE ====")
        print("1. User Login")
        print("2. Driver Login")
        print("3. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            user_login()
        elif ch == "2":
            driver_login()
        elif ch == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")


main()
