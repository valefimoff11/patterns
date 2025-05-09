import sys

#demo of class and object attributes and methods

class MethodDemo:

    #class (static) attributes
    y = 100

    #object constructor
    def __init__(self):

        #object instance attributes
        self.x = 1

    #string representation of the object
    def __repr__(self):
        return f"Value: {self.x}"

    @classmethod
    def class_method_demo(cls):
        #only class attributes are accessible
        cls.y = 99
        print(cls.y)

    def object_instance_method_demo(self):
        #both object and class attributes are accessible from object instance method
        print(self.x)
        print(self.y)

#direct access to class (static) variable through the class (object) itself
print(MethodDemo.y)

#access to class method through the class (object) itself
MethodDemo.class_method_demo()

o = MethodDemo()

#access to class method through object handle
o.class_method_demo()

o.object_instance_method_demo()

print(o)