<center> <h1>HBNB - The Console</h1> </center>

<p align="center"><img src="bnb.png" alt="AirBnb  logo"></p>

## Descreption:
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---
## Installation
* Clone This Repo `git clone https://github.com/salahbesbes/AirBnB_clone.git`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Available Command:
* quit and EOF to exit the program
* help for every Command
* create 
* show
* destroy
* all
* update
* count
<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| N/A: Authors | [AUTHORS](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 0: README File| [README.md](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/README.md) | Read Me file
| N/A: Pep8 | N/A | All code is pep8 compliant|
| 1: Unit Testing | [/tests](https://github.com/Theemiss/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 2. Consol improvements | [console.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/console.py)<br> [/models](https://github.com/Theemiss/AirBnB_clone_v2/tree/master/models)<br> [/test](https://github.com/Theemiss/AirBnB_clone_v2/tree/master/tests) | Makes improvements to the console made in the part 1 of the Airbnb Clone|
| 3. MySQL setup development | [setup_mysql_dev.sql](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) | Create a database and user, and grant privileges to the created user on the created database for the development|
| 4. MySQL setup test | [setup_mysql_test.sql](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) | Cteate a database and user, and grant privileges to the created user on the created database for testing|
| 5. Delete object | [models/engine/file_storage.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Add function that deletes objects from satorage|
| 6. DBStorage - States and Cities | [models/base_model.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/base_model.py)<br> [models/city.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/city.py)<br> [models/state.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/state.py)<br>[models/engine/db_storage.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/engine/db_storage.py)<br>[models/__init__.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/engine/__init__.py) | Update DBstorage|
| 7. DBStorage - User | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/user.py) | Update user |
| 8. DBStorage - Place | [/models/user.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/city.py) | Update place |
| 9. DBStorage - Review  | [/models/review.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/review.py) [/models/user.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/user.py) [/models/place](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/place.py) | Update Review |
| 10. DBStorage-Amenity... and BOOM! | [/models/amenity.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/place.py](https://github.com/Theemiss/AirBnB_clone_v2/blob/master/models/place.py) | Update Amenties | 
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

2. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```


## Bugs
No known bugs at this time. 

## Authors
Ahmed Belhaj - [Github](https://github.com/Theemiss)

Mohamed Amin Bondi - [Github](https://github.com/aminbnd)

<br>
<center><img src="https://www.holbertonschool.com/holberton-logo.png"></center>
