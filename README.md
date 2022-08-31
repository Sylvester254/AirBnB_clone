# AirBnB clone
## Features:
- A ```command interpreter``` to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A ```website``` (the front-end) that shows the final product to everybody: static and dynamic
- A ```database``` or files that store data (data = objects)
- An ```API``` that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Steps Overview:
- Each step will link to a concept:
### The console

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.
<img src = "img/815046647d23428a14ca.png">

### Web static
- learn HTML/CSS
- create the HTML of your application
- create template of each object
<img src = "img/87c01524ada6080f40fc.png">

### MySQL storage
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.
<img src = "img/5284383714459fa68841.png">

### Web framework - templating
- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database
<img src = "img/cb778ec8a13acecb53ef.png">

### RESTful API
- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API
<img src = "img/06fccc41df40ab8f9d49.png">

### Web dynamic
- learn JQuery
- load objects from the client side by using your own RESTful API
<img src = "img/d2d06462824fab5846f3.png">

## First Step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called ```BaseModel```) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (```User, State, City, Place```…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

Our command interpreter should be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
