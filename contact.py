import sys

# Dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}")
    else:
        print("No contacts found.")

def search_contact():
    search_query = input("Enter the name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_query in name or search_query in info['Phone']:
            print(f"Found - Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
            found = True
    if not found:
        print("No contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Select what you would like to update:")
        print("1. Phone")
        print("2. Email")
        print("3. Address")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            new_phone = input("Enter the new phone number: ")
            contacts[name]['Phone'] = new_phone
        elif choice == '2':
            new_email = input("Enter the new email address: ")
            contacts[name]['Email'] = new_email
        elif choice == '3':
            new_address = input("Enter the new address: ")
            contacts[name]['Address'] = new_address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
