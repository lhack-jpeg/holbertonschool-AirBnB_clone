# AirBnB clone - The console
<p align="center" width="70%">
    <img src="https://user-images.githubusercontent.com/91517809/176107896-998e3280-f565-4e09-a801-c609984bfed6.png">
</p>

## :page_with_curl: Description
This console is the first part of the AirBnB project at Holberton School. This program will cover some concepts from higher level programming that we have studied and gone over during the curriculum. The goal of this project is to produce a simple clone of the AirBnB website. A simple command interpeter has been created to manage the main objects for the website.

## :evergreen_tree: Environment
All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## :cd: Compilation
> Step 1: Clone git hub repository locally using the following command
```
git clone https://github.com/lhack-jpeg/holbertonschool-AirBnB_clone
```
> Step 2: Navigate to the newly created repo
```
cd holbertonschool-AirBnB_clone
```
> Step 3: Run the console with the following command
```
./console.py
```
> Step 4: Type in a command, examples below
```
(hbnb) help
(hbnb) create BaseModel
```
> Step 5: Exit the program using 2 different ways
```
(hbnb) exit
Ctrl+D
```

## :hourglass: Operations
### Interactive mode
In the interactive mode the console will display the (hbnb) prompt awaiting for user input. After the user inputs a command the command will be executed and the (hbnb) will be displayed again, in a new line, awaiting for using unput again. As long as the user doesn't exit the program (by using 'quit' or 'Ctrl+D'), this will go on indefinitely. Example:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
```
### Non-interactive mode
In the non-interactive mode the console is run with a command pipped into its execution, this way the command is run as soon as the program is executed. In this mode no prompt will appear awaiting user to input more commands, the command that is pipped into the program at execution will be the only command run, therefore no further input is expected from the user. Example:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## :wrench: Testing
All files, classes and functions have been tested using unit tests. To check the tests, see example below:
### Interactive mode
```
python3 -m unittest discover tests
```
### Non-interactive mode
```
echo "python3 -m unittest discover tests" | bash
```
## :open_file_folder: File Descriptions
### [console.py](console.py)
The console is the entry point of the interpreter, the list of commands that are supported are as follows:
- ```EOF``` - Exits the program using 'Ctrl+D'.
- ```quit``` - Exits the program.
- ```create``` - Creates a new instance of ```BaseModel```, and saves it to a JSON file, then prints the id of the instance created.
- ```destroy``` - Deletes an instance based on the class name and id provided (saves the change into the JSON file).
- ```all``` - Prints all instances created as a string representation of a dictionary.
- ```show``` - Prints the instance of a provided class name and id as a string representation.
- ```update``` - Updates an instance based on the class name and id by adding or updating the attribute (saves the change into JSON file).
### [base_model.py](base_model.py)
The BaseModel class is the class in which all other classes inherit from.
- ```def __init__(self, *args, **kwargs)``` - The initialization of the BaseModel class
- ```def __str__(self)``` - String representation of the BaseModel class
- ```def save(self)``` - Updates the attribute ```updated_at``` with the current datetime (saves the change into JSON file)
- ```def to_dict(self)``` - Returns a dictionary of the key/values of ```__dict__``` in an instance

|INHERITED FILES FROM BASEMODEL|DESCRIPTION|ATTRIBUTES|ATTRIBUTE VALUES
|-|-|-|-|
|[user.py](user.py)|user class|email, password, first_name, last_name|```email:``` string, ```password:``` string, ```first_name:``` string, ```last_name:``` string|
|[amenity.py](amenity.py)|amenity class|name|```name:``` string|
|[city.py](city.py)|city class|state_id, name|```state_id:``` string, ```name:``` string|
|[place.py](place.py)|place class|city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids|```city_id:``` string, ```user_id:``` string, ```name:``` string, ```description:``` string, ```number_rooms:``` integer, ```number_bathrooms:``` integer, ```max_guest:``` integer, ```price_by_height:``` integer, ```latitude:``` float, ```longitude:``` float, ```amenity_ids:``` list|
|[review.py](review.py)|review class|place_id, user_id, text|```place_id:``` string, ```user_id:``` string, ```text:``` string|
|[state.py](state.py)|state class|name|```name:``` string

### [file_storage.py](file_storage.py)
The file_storage file serializes instances to a JSON file & deserializes back to instances
- ```def all(self)``` - Returns the dictionary __objects
- ```def new(self, obj)``` - Add new item to object dictionary
- ```def save(self)``` - Writes the __objects dictionary to JSON file
- ```def reload(self)``` - Reads the JSON file and deserialise the file. If the file doesn't exist, does nothing.

## :clapper: Examples
```
(hbnb) all

[]

(hbnb) create BaseModel

cc4858f7-5d54-484f-ae71-641f4021696a

(hbnb) all

["[BaseModel] (cc4858f7-5d54-484f-ae71-641f4021696a) {'id': 'cc4858f7-5d54-484f-ae71-641f4021696a', 'created_at': datetime.datetime(2022, 10, 12, 19, 8, 19, 640154), 'updated_at': datetime.datetime(2022, 10, 12, 19, 8, 19, 640184)}"]

(hbnb) show BaseModel cc4858f7-5d54-484f-ae71-641f4021696a

[BaseModel] (cc4858f7-5d54-484f-ae71-641f4021696a) {'id': 'cc4858f7-5d54-484f-ae71-641f4021696a', 'created_at': datetime.datetime(2022, 10, 12, 19, 8, 19, 640154), 'updated_at': datetime.datetime(2022, 10, 12, 19, 8, 19, 640184)}

(hbnb) destroy BaseModel cc4858f7-5d54-484f-ae71-641f4021696a

(hbnb) show BaseModel cc4858f7-5d54-484f-ae71-641f4021696a

** no instance found **

(hbnb) 
```
## :ant: Bugs
No known bugs at this stage.

## :paperclip: Authors
- [Luke Hacket](https://github.com/lhack-jpeg)
- [Dylan Anderson](https://github.com/RubberizedDuck)
