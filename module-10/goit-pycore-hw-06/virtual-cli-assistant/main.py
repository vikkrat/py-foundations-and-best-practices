'''
Task 1
--------------------------------------------------------------------------------------------

The user interacts with a contact book by adding, removing, and editing entries. The user 
should also be able to search the contact book for entries using one or multiple criteria (fields).
About the fields, it can be said that some fields are mandatory (like the name) and some are 
optional (like phone or email, for example). Entries can also contain several fields of the same type 
(like multiple phones, for example). The user should be able to add, remove, or edit fields in any record.

Technical Description of the Task

Develop a system for managing an address book.

Entities:

• Field: A base class for entry fields.
• Name: A class for storing a contact's name. This is a mandatory field.
• Phone: A class for storing a phone number. Includes validation of the format (10 digits).
• Record: A class for storing information about a contact, including the name and a list of phones.
• AddressBook: A class for storing and managing entries.

Functionality:

• AddressBook: Adding entries.
• Searching for entries by name.
• Removing entries by name.
• Record: Adding phones.
• Removing phones.
• Editing phones.
• Searching for a phone.

Assessment Criteria

AddressBook Class:
• Implemented the add_record method that adds an entry to self.data.
• Implemented the find method that locates an entry by name.
• Implemented the delete method that removes an entry by name.

Record Class:
• Implemented storage of the Name object in a separate attribute.
• Implemented storage of a list of Phone objects in a separate attribute.
• Implemented methods for adding - add_phone/removing - remove_phone/editing - 
  edit_phone/searching for Phone objects - find_phone.

Phone Class:
• Implemented phone number validation (must check for 10 digits).
'''
from classes.address_book_class import AddressBook
from classes.record_class import Record

# Test the function
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Output all records
for name, record in book.data.items():
    print('------------------All contacts--------------------')
    print('--------------------------------------------------')
    print(record)

# Edit John's phone number
john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")
    # Print John's updated record
    print(f"{john} was updated!")

# Find a specific phone number
found_phone = john.find_phone("5555555555")
if found_phone:
    print(f"{john.name.value}: {found_phone}")

# Delete Jane's record
book.delete("Jane")