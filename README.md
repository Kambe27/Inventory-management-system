
# This is my thought process before developing anything #
Inventory Management System
- Should allow the addition and removal of items, as well as updating the items. CRUD basically, create - read - update - delete.
- Not a core feature but will consider adding filters to get the specific type of item, a certain price range etc.
- Bulk import, user should be able to import the csv, so many create a specific folder where the csv can be placed into, then once a cli option is prompted, the data will then be pulled, sorted, and renumbered to match the existing items, if items match - add on the supply.
- Since this is an inventory management system, and nothing is really mentioned by the assessment.md I will not be making a customer/admin side.
- Simple way to handle the data would be to use JSON, plaintxt and CSV would be a bit annoying to work with in my opinion. If an actual system using SQL would be the way, things like postgre etc. 
- Since the assessment mentioned the use of any language, the easiest method for me to work with would be python, my go to is Java, but it has been a while since I have worked with Python so a nice simple challenge would be interesting.
- Maybe an async function could work? Maybe when the system is sorting and cleaning the import data, the user should be allowed to go do other tasks and once the data is sorted, user can be prompted with Import Data Cleaned, want to view? If yes then they can view and then confirm the merge into the existing data which will send to another Async function, if No, they can either cancel the import or just instantlly add it without viewing it.But then again implementing something like that for a really small sample incoming_stock file would be kind of pointless since it would be almost instant.


# Steps for Development
1) Setting up the basic framework for the CLI, making a simple crud system, no storage of info yet + simple navigation.
2) Once framework done, can move on to connecting parts as well as implementing the JSON to store data.
3) Work on the Import function.
4) Tests + Debugging.


# Sources 
https://www.w3schools.com/python/
