# AirBnB Clone - The Console

## Project Overview
This project is an AirBnB clone, focusing on building a command-line interface (CLI) to manage AirBnB objects. The project is to be completed in teams of 2 people, and our team consists of Ayomitan Omotayo and Bright Victor.

## Resources
- [cmd module](https://docs.python.org/3/library/cmd.html)
- [cmd module in depth](https://docs.python.org/3/library/cmd.html)
- [Python packages concept page](https://packaging.python.org/key_projects/#setuptools)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [cmd module wiki page](https://en.wikipedia.org/wiki/Cmd.exe)
- [Python unittest](https://docs.python.org/3/library/unittest.html)

## Description
The goal of this project is to create a command interpreter to manage AirBnB objects. It serves as the first step towards building a full web application, covering foundational concepts such as serialization/deserialization, inheritance, and storage management.

### Tasks
- Implement a parent class (BaseModel) for initialization, serialization, and deserialization of instances.
- Establish a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Define classes for AirBnB objects (User, State, City, Place) inheriting from BaseModel.
- Develop the first abstracted storage engine: File storage.
- Create unit tests to validate classes and storage engine functionality.

### Operations
The command interpreter should support the following operations:
- Create a new object (e.g., User, Place).
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, compute stats, etc.).
- Update attributes of an object.
- Destroy an object.

## Getting Started
To get started with the project, clone the repository and follow the instructions provided in the project documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

