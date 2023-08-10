#AirBnB clone

Welcome to the AirBnB clone project!

##AirBnB clone -> The console

###Overview

This is the first step towards building full web application **the AirBnB clone**
This first step is very important to manage the objects of our project, so that we can:
    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc…
    - Do operations on objects (count, compute stats, etc…)
    - Update attributes of an object
    - Destroy an object

###Files and Directories

    - `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
    - `tests` directory will contain all unit tests.
    - `console.py` file is the entry point of our command interpreter.
    - `models/base_model.py` file is the base class of all our models. It contains common elements:
     - attributes: id, created_at and updated_at
     - methods: save() and to_json()
    - `models/engine` directory will contain all storage classes.
