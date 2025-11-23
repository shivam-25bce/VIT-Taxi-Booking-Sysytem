


#Data base
users=["user1","user2"]
user_passwords=["123","456"]

drivers=["driver1","driver2"]
driver_passwords=["111","222"]

bookings = []                                   # Each booking will be stored as {user, route, fare, status}




#User's Login
def user_login():
    """Authenticate user and open user menu if successful."""
    username=input("Enter username: ")
    password=input("Enter password: ")

    for index in range(len(users)):
        if users[index]==username and user_passwords[index]==password:
            print("User login successful!")
            user_menu(username)
            return

    print("Invalid user login!")


#Driver's Login
def driver_login():
    """Authenticate driver and open driver menu if successful."""
    username=input("Driver username: ")
    password=input("Password: ")

    for index in range(len(drivers)):
        if drivers[index]==username and driver_passwords[index]==password:
            print("Driver login successful!")
            driver_menu(username)
            return

    print("Invalid driver login!")


#User Menu
def user_menu(username):
     while True:
        print("\n====USER MENU====")
        print("1.Book Taxi")
        print("2.View My Bookings")
        print("3.Logout")
        choice=input("Enter choice=")
        if choice=="1":
            book_taxi(username)
        elif choice=="2":
            view_user_bookings(username)
        elif choice=="3":
            print("Logging out")
            break
        else:
            print("Invalid choice T_T")


#Booking
def book_taxi(username):
    print("\nChoose Route:")
    print("1.VIT'Bhopat to Bhopal Jn(₹1200)")
    print("2.VIT'Bhopal to Rani Kamlapati Jn(₹1100)")
    print("3.VIT'Bhopal to Sehore Jn(₹400)")
    choice=input( "Enter your choice=")
    routes = {
        "1":("VIT'Bhopal to Bhopal Junction",1200),
        "2":("VIT'Bhopal to Rani Kamlapati",1100),                    
        "3":("VIT'Bhopal to Sehore",400)
    }

    if choice not in routes:
        print("Invalid route!")
        return
    r_name,fare_amount=routes[choice]
    booking = {
        "user":username,
        "route":r_name,                                       
        "fare":fare_amount,
        "status":"Pending"
    }

    bookings.append(booking)
    print("\nTaxi Booked Successfully...." )
    print("Route:",r_name)
    print("Fare:",fare_amount)


#User's booking
def view_user_bookings(username):
    print("\n====YOUR BOOKINGS====" )
    found=False
    for booking in bookings:
        if booking["user"]== username:
            print(booking)
            found=True
    if not found:
        print("No bookings found :<")


#Driver's option
def driver_menu(driver_name):
     while True:
        print("\n====DRIVER MENU====")
        print("1.View All Trips")
        print("2.Update Trip Status")
        print("3.Logout")
        choice =input("Enter choice=")
        if choice=="1":
            view_all_trips()
        elif choice=="2":
            update_trip_status()
        elif choice=="3":
            print("Logging out")
            break
        else:
            print("Invalid choice T_T")


#Driver's view all booking
def view_all_trips():
    print("\n====ALL BOOKINGS====")
    if not bookings:
        print("No trips available ")
        return
    for booking in bookings:
        print(booking)


#Driver Trip Status
def update_trip_status():
    route_name=input("Enter exact route name to update=")
    for booking in bookings:
        if booking["route"]==route_name:
            new_status=input("Enter new status(Accepted/Completed)=")
            booking["status"]=new_status
            print("Status updated")
            return
    print("Route not found")


#Main Menu
def main():
    while True:
        print("\n==== VIT BHOPAL TAXI SERVICE ====")
        print("1.User Login")
        print("2.Driver Login")
        print("3.Exit")
        choice=input("Enter choice=")
        if choice=="1":
            user_login()
        elif choice=="2":
            driver_login()
        elif choice=="3":
            print("Goodbye")
            break
        else:
            print("Invalid Choice T_T ")

main()





