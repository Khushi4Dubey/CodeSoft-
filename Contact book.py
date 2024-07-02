class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                return True
        return False

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            if contact_book.update_contact(name, new_phone, new_email):
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            if contact_book.delete_contact(name):
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    