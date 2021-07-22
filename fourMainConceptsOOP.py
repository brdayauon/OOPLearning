1. What are the four main concepts of OOP, and how do they work?
    - Abstraction:
        - important because it simplfies programming process. Works by only
        displaying data that is relevant to your goal and hides the complex details.
        
        Showing essential details and keeping everything else hidden. 
        Users of the class shouldn't worry about the inner details of the class.'
        Classes shouldn't directly interact with other classes' data.

        Example.. modern programmers are complex where multiple programmers work on one program. 
         - what is best is if the section you are working on is able to function without knowledge of the inner workings of 
         colleague's section'

        #interfaces refer to the way sections of code can communicate with one another
        #implementation of these methods or how these methods are coded, should be hidden.
        if classes are tangled.. one change can create a ripple effect that causes many more changes. 
        - creating an interface which classes can interact ensures that each piece can be individually developed. 





    - Inheritance:
        - just like what it sounds, when a class is able to inherit the properties and characteristics of another class.
        * access modifiers such as private, public, protected.
        private - only accessible to that class (allows you to create multiple private members of the same name in diff locations)
        public - accessed from anywhere in the program 
        protected - can be accessed within the class it is defined as well as subclasses of that class.

    - Encapsulation:
        - Class that conceals data fields and methods that achieve functions, though become accessible through access modifiers.
        - Basically, acts as information hiding. For example if you have a class with data fields.. other classes can access those data fields,
        by the setter/getter methods you defined within the class. Keep's programmer in control of access to data. Prevent program from ending up 
        in strange or unwanted states'. 


    - Polymorphism
        - runtime Polymorphism:
        - compile-time Polymorphism:
        Its process assigns the value or behavior of something in a subclass to something that was already defined in the main class."

        - runtime Polymorphism. (dynamic Polymorphism):
            - basically when you have methods of the same name and same parameters but different implementation/definition. 
            When method is called of that object (with same name).. that object invoke's that method's definition. 
        
        - compile time Polymorphism:
        when you have the same function name the same but different arguments (parameters) 

        #problem#
        Compile time Polymorphism is method overloading where if you don't keep straight parameters which you need for implementation. 
        Using the wrong argument might not have an error if it matches another form of the method.  *make sure you call correct method*