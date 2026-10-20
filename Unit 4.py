
# Contact Management System

SIZE = 10
table = [[] for _ in range(SIZE)]

def hash_function(name):
    return sum(ord(ch) for ch in name.lower()) % SIZE

def add_contact(name, phone):
    index = hash_function(name)

    for contact in table[index]:
        if contact[0].lower() == name.lower():
            contact[1] = phone
            print("Contact updated successfully!")
            return

    table[index].append([name, phone])
    print("Contact added successfully!")

def search_contact(name):
    index = hash_function(name)

    for contact in table[index]:
        if contact[0].lower() == name.lower():
            print("Name:", contact[0])
            print("Phone:", contact[1])
            return

    print("Contact not found!")

def delete_contact(name):
    index = hash_function(name)

    for contact in table[index]:
        if contact[0].lower() == name.lower():
            table[index].remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")

def display_contacts():
    print("\nAll Contacts:")
    found = False

    for bucket in table:
        for contact in bucket:
            print(contact[0], ":", contact[1])
            found = True

    if not found:
        print("No contacts available.")


while True:
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name and phone.isdigit() and len(phone) == 10:
            add_contact(name, phone)
        else:
            print("Enter a name and valid 10-digit phone number.")

    elif choice == "2":
        name = input("Enter name to search: ").strip()
        search_contact(name)

    elif choice == "3":
        name = input("Enter name to delete: ").strip()
        delete_contact(name)

    elif choice == "4":
        display_contacts()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
