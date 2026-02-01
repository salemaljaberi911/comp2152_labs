
"""|Create a dictionary called contacts with:
"Alice": "555-1234"
"Bob": "555-5678"
"Charlie": "555-9999" """

contacts = {
"Alice": "555-1234",
"Bob": "555-5678", 
"Charlie": "555-9999"
}
#Print Alice's phone number by accessing the dictionary

print("Alices Number ",contacts["Alice"])

#Add a new contact: "Diana" with number "555-4321"

contacts["Diana"]= "555-432"
print("Contacts after add Dina ",contacts)
#Update Bob's number to "555-0000"

contacts["Bob"]="555-0000"
print("contacts after updateied bob ",contacts)
#Delete Charlie's contact using del

del contacts["Charlie"]
print("contact after delete Charlie's",contacts)
#Print all contact names using keys()

print("All name ",contacts.keys())
#Print all phone numbers using values()

print("All numbers :",contacts.values())
#Print the total number of contacts
print("Total contacts :",len(contacts))



