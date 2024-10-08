import json

def add_contacts(contacts):
    name = input("Enter the name: ")
    contact_no = int(input("Enter the contact number: "))
    email = input("Enter the email: ")
    
    if name in contacts:
        print(f"{name} already exists! Please enter a different name.")
    else:
        contacts[name] = {"phone": contact_no, "email": email}
        print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts available.")

def load_contacts():
    try:
        with open('contact_list.json', 'r') as file:
            contact_file = json.load(file)
            return contact_file
    except FileNotFoundError:
       return {}

def save_contacts(contacts):
    with open('contact_list.json', 'w') as file:
        json.dump(contacts, file)
        print("Contacts saved successfully!")

contacts = load_contacts()

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Save and Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contacts(contacts)
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        save_contacts(contacts)
        break
    else:
        print("Invalid choice. Please try again.")
