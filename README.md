# Simple Inventory Management System #


# This is my thought process before developing anything 
Inventory Management System
- Should allow the addition and removal of items, as well as updating the items. CRUD basically, create - read - update - delete.
- Not a core feature but will consider adding filters to get the specific type of item, a certain price range etc.
- Bulk import, user should be able to import the csv, so many create a specific folder where the csv can be placed into, then once a cli option is prompted, the data will then be pulled, sorted, and renumbered to match the existing items, if items match - add on the supply.
- Since this is an inventory management system, and nothing is really mentioned by the assessment.md I will not be making a customer/admin side.
- Simple way to handle the data would be to use JSON, plaintxt and CSV would be a bit annoying to work with in my opinion. If an actual system using SQL would be the way, things like postgre etc. 
- Since the assessment mentioned the use of any language, the easiest method for me to work with would be python, my go to is Java, but it has been a while since I have worked with Python so a nice simple challenge would be interesting.
- Maybe an async function could work? Maybe when the system is sorting and cleaning the import data, the user should be allowed to go do other tasks and once the data is sorted, user can be prompted with Import Data Cleaned, want to view? If yes then they can view and then confirm the merge into the existing data which will send to another Async function, if No, they can either cancel the import or just instantlly add it without viewing it.But then again implementing something like that for a really small sample incoming_stock file would be kind of pointless since it would be almost instant.


# Steps for Development
~~1) Setting up the basic framework for the CLI, making a simple crud system, no storage of info yet + simple navigation.~~ Completed

~~2) Once framework done, can move on to connecting parts as well as implementing the JSON to store data.~~ Completed

~~3) Work on the Import function.~~ Completed

~~4) Tests + Debugging.~~ Completed


# Key Consideration Questions
1) **Data Structure:** The data structure for the assessment is pretty straightforward, I used a python dictionary to store the products. The product ID's (SKU) acts as the unique key, and the value is another dictionary which holds the items name and quantity. The main reason I did this was at it makes checking if an item exists or not incredibly fast.

2) **Data Storage:** For the data storage, i used a local JSON file (data/inventory_data.json). JSON allows the mapping to python dictionaries really easy, it also makes it simple for people to read it and safely stores the data so it isnt lost when the application closes.

3) **User Interaction:** I built an interactive CLI, where the use navigates through a menu which is numbered. I also implemented the clear_screen() to allow the screens to be cleared between actions to keep the interface clear.

4) **Error Handling:** For error handling the implementation allows the system to catch common mistakes without crashing the system, an example would be that if a user types letters instead of numbers for a quantity, it shows an "inavlid quantity" error. If a user were to try to update an item that does not exist, it will pause and then warn them that the "item id is not found".

5) **Import Decisions:** Due to some errors which were included in the incoming_stock.csv, I made it so that the system will skip the bad rows, things like negative quantities or missing ids and list them in an error report at the end. If the CSV contains a brand new SKU, the system will automatically add it into the inventory_data.json.

6) **Technology Choice:** For the program I had decided to use Python using the IDE VS Code. The use for python, not just a challenge for me as it has been a while since i've last programmed using python, its in-built json and csv modules were perfect for the assessment to read and handle the files. 


# Setup and Run Instructions

- Require Python 3.6 or higher
- No External Libraries required

- **How to Run the Application:**
- Download or clone the project repo and extract the files
- Open your terminal or command prompt and navigate to the root directory of the project which is Inventory Management System
- Execute the main script which is **python main.py** 
- Another way is if you are using an IDE like VS Code, just opening the main.py file and clicking on the run button at the top without debuggin will run the CLI.

- Following that, to use the CLI just go through the menu by inputting the number options.

# Sources 
https://www.w3schools.com/python/
https://www.geeksforgeeks.org/python/python-programming-language-tutorial/