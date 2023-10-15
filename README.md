this is project aims to create a console program to manage our objects:
    -Create a new object (ex: a new User or a new Place)
    -Retrieve an object from a file, a database etc…
    -Do operations on objects (count, compute stats, etc…)
    -Update attributes of an object
    -Destroy an object

how to run the console:
    ./console.py

how to use it:

Command    | Description
-------------------------------------------------------------------------------------------------
create     | Creates a new instance of BaseModel, saves it (to the JSON file), and prints the ID.
Usage      | create (class_name)
example    | create BaseModel
-------------------------------------------------------------------------------------------------
show       | Prints the string representation of an instance based on the class name and ID.
Usage      | show (class_name) (id)
example    | show BaseModel the_objects_id
-------------------------------------------------------------------------------------------------
destroy    | Deletes an instance based on the class name and ID (saves the change into the JSON file).
Usage      | destroy (class_name) (id)
example    | destroy BaseModel the_objects_id
-------------------------------------------------------------------------------------------------
all        | Prints all string representations of all instances based on the class name.
Usage      | all (class_name)
example    | all BaseModel
-------------------------------------------------------------------------------------------------
update     | Updates an instance based on the class name and ID by adding or updating attributes.
Usage      | update (class_name) (the_objects_id) (attribute_name) (attribute_value)
example    | update User user_id first_name joe 
------------------------------------------------------------------------