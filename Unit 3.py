
# Railway Ticket Reservation and Waiting List System

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class RailwaySystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.confirmed = None       # Linked list
        self.wait_front = None      # Queue front
        self.wait_rear = None       # Queue rear
        self.undo_stack = []        # Stack
        self.seats = 0

    def book_ticket(self, name):
        if self.seats < self.capacity:
            new_node = Node(name)
            if self.confirmed is None:
                self.confirmed = new_node
            else:
                temp = self.confirmed
                while temp.next:
                    temp = temp.next
                temp.next = new_node

            self.seats += 1
            print(name, "ticket confirmed!")
        else:
            self.add_waiting(name)

    def add_waiting(self, name):
        new_node = Node(name)
        if self.wait_rear is None:
            self.wait_front = self.wait_rear = new_node
        else:
            self.wait_rear.next = new_node
            self.wait_rear = new_node

        print(name, "added to waiting list.")


    def cancel_ticket(self, name):
        temp = self.confirmed
        prev = None

        while temp and temp.name != name:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Confirmed passenger not found.")
            return

        if prev is None:
            self.confirmed = temp.next
        else:
            prev.next = temp.next

        self.seats -= 1
        self.undo_stack.append(name)
        print(name, "ticket cancelled.")

        if self.wait_front:
            next_passenger = self.wait_front
            self.wait_front = self.wait_front.next

            if self.wait_front is None:
                self.wait_rear = None

            self.book_ticket(next_passenger.name)
            print(next_passenger.name, "promoted from waiting list.")

    def show_confirmed(self):
        print("\nConfirmed Passengers:")
        temp = self.confirmed
        if temp is None:
            print("No confirmed passengers.")
        while temp:
            print("-", temp.name)
            temp = temp.next

    def show_waiting(self):
        print("\nWaiting List:")
        temp = self.wait_front
        if temp is None:
            print("No waiting passengers.")
        while temp:
            print("-", temp.name)
            temp = temp.next

    def undo_cancel(self):
        if not self.undo_stack:
            print("No cancellation to undo.")
            return

        name = self.undo_stack.pop()
        print("Last cancellation was:", name)
        print("Note: Full undo requires restoring the earlier seat allocation.")



capacity = int(input("Enter total available seats: "))
railway = RailwaySystem(capacity)

while True:
    print("\n===== RAILWAY RESERVATION SYSTEM =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Display Confirmed Passengers")
    print("4. Display Waiting List")
    print("5. Undo Last Cancellation (Stack Demo)")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter passenger name: ")
        railway.book_ticket(name)

    elif choice == "2":
        name = input("Enter passenger name to cancel: ")
        railway.cancel_ticket(name)

    elif choice == "3":
        railway.show_confirmed()

    elif choice == "4":
        railway.show_waiting()

    elif choice == "5":
        railway.undo_cancel()

    elif choice == "6":
        print("Thank you for using Railway Reservation System!")
        break

    else:
        print("Invalid choice. Try again.")
