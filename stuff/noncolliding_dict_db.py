"""
This script is a simple program that implements a non colliding ID based database in a dictionary data structure.

The Faker library is used to generate names, emails, addresses, and phone numbers for each record.
The database dictionary has an additional pointer variable named newIdxPointer that keeps track of where new records
can be added without colliding with existing ones.

There are two functions defined: insertData and printDict. The first function adds a new entry into the data structure
while making sure the index is increased, and the second function prints the keys and values in the dictionary.

To delete a random record, a random number between 0 and the last index (without the index pointer variable) is generated.
By using pop on the dictionary, the chosen entry is deleted.
"""

from faker import Faker
import random

# Create a new instance of Faker and set the number of records to generate
generator = Faker()
number_of_records = 10

# Define a dict
# Includes special pointer to the last index created, this is used to keep track of where to start adding
# new data to the Database, in order to avoid collisions with old id's that have been deleted
database = {"newIdxPointer": 0}


# Append data function that makes sure the above index counter is always increased
def insertData(data):
    database[database["newIdxPointer"]] = data
    database["newIdxPointer"] += 1


def printDict():
    # Iterate over the dictionary and display its keys and values
    for key, value in database.items():
        print(f"Key: {key}")
        print(f"Data: {value}")


# Generate fake data and fill the dictionary with it
for _ in range(number_of_records):
    # Store records in a list, where the keys are index values like in a list.
    # This makes deleting entries easy, as it does not change other entries' indices
    insertData({
        "name": generator.name(),
        "email": generator.email(),
        "address": generator.address(),
        "phone": generator.phone_number()
    })

printDict()

# Delete a random record, make sure not to delete the indexPointer
entryToDelete = random.randint(0, len(database) - 2)
print(entryToDelete)

print(f'###\n- - - DELETING ENTRY NO. {entryToDelete}\n###')
database.pop(entryToDelete)

# Add a new record
insertData({
    "name": generator.name(),
    "email": generator.email(),
    "address": generator.address(),
    "phone": generator.phone_number()
})

printDict()
