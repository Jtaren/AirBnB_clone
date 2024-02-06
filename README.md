AirBnB Clone Command Interpreter

Welcome to the AirBnB clone project! This project aims to develop a
command-line interface(CLI) for managing AirBnB objects.
The CLI allows users to perform various operations on objects
such as creating, retrieving, updating,
and deleting(CRUD) objects like Users, States, Cities, and Places.

Project Overview
The project consists of several components:

BaseModel:
	A parent class responsible for the initialization,
	serialization, and deserialization of objects.

AirBnB Objects:
	Various classes(e.g., User, State, City, Place)
	that inherit from the BaseModel.

File Storage Engine:
	An abstracted storage engine to save and
	load objects to and from files.

Command Interpreter:
	The main interface where users interact
	with the system to manage AirBnB objects.

Command Interpreter

The command interpreter is similar to a shell but tailored
for managing AirBnB objects. Here's how to start and use it.

How to Start

Clone the repository to your local machine.
Navigate to the project directory.
Run the command interpreter script(e.g., console.py).

Usage

Once the command interpreter is running, you can perform 
the following actions

Create:
	Create a new object(e.g., User, Place).
Retrieve:
	Retrieve an object from storage(file, database, etc.).
Operations:
	Perform operations on objects(e.g., count, compute stats).
Update:
	Update attributes of an existing object.

Destroy:
	Delete an object.
