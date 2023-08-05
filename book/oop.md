Abstraction means the implementation is hidden from the user, and only the relevant data or information is shown

A class method can modify the state of the class, but they can’t directly modify the state of an instance that inherits from that class

### Suppose a Game class inherits from two parent classes: BoardGame and LogicGame. Which statement is true about the methods of an object instantiated from the Game class?

An instance of the Game class will inherit whatever methods the BoardGame and LogicGame classes have


### What does a class’s init() method do?

The __init__ method is a constructor method that is called automatically whenever a new object is created from a class. It sets the initial state of a new object


### What is the purpose of the self keyword when defining or calling methods on an instance of an object?

self refers to the instance whose method was called

### Why would you create an abstract class, if it can have no real instances?
to avoid redundant coding in children
to have common behavior in derived classes

### What is encapsulation?
hiding the data and implementation details within a class

### Which two blocks are used to handle and check errors?
try and catch

### What are the five Creational Design patterns by the Gang of Four?
Abstract Factory, Builder, Factory Method, Prototype, and Singleton