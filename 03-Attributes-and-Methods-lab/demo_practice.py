class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


def get_values(obj, attr_names):
    return [getattr(obj, attr_name) for attr_name in attr_names]


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)


pesho = Person('Pesho', 11, 'Sofia', 'Bulgaria')
# print(getattr(pesho, 'car'))
print(getattr(pesho, 'car', f'obj {Person} have no attr named "car"'))
print(get_values(pesho, ['city', 'country']))
circle = Circle(4)
area_method = get_values(circle, ['area'])[0]
# <bound method Circle.area of <__main__.Circle object at 0x0000022171F51C40>>
print(area_method)
print(area_method())  # 50.24
print(getattr(circle, 'radius', 'there is no radius'))
print(getattr(circle, 'radius') if hasattr(circle, 'radius') else None)
print(getattr(circle, 'diameter', 'there is no diameter'))
print(getattr(circle, 'diameter') if hasattr(circle, 'diameter') else None)
print(getattr(Circle, 'area'))  # <function Circle.area at 0x0000025B0FBFBC10>
print(getattr(circle, 'area'))  # <bound method Circle.area of <__main__.Circle object at 0x0000025B0FC0A340>>

'''
point of using getattr() method is so if you do not know the given attribute "name" 
and you are getting it from elsewhere.
The getattr() method take two arguments: 
on position one -> object ; position two  -> an attribute if such exist in the object. 
On that Note: you can also give a method and it will store attribute.  
!IMPORTANT: if attribute that does not exist in the object is given it is risen "AttributeError" / check line 24 /
TO PREVENT THE ERROR: you can give an third argument what getattr() to return if the second argument is not 
found withing the object. / for ref line 25/
getattr() can check if function in the class exist. 
it can do the same for instance 
'''

print(hasattr(pesho, 'city'))
'''
hasattr() method check if the object have attribute or method with the given name and return True/False 
'''

print(setattr(pesho, 'city', 'Plovdiv'))
print(setattr(pesho, 'citie', 'Plovdiv'))  # return None
print(pesho.__dict__)
# print(dir(pesho))
setattr(pesho, 'print_name', lambda: print(pesho.name))
pesho.print_name()
print(pesho.__dict__)
print(setattr(circle, 'diameter', (2 * circle.radius)))
print(circle.__dict__)
# print(dir(circle))
'''
setattr() method sets the attribute to a new value / pesho.city = 'Plovdiv'
you can also set instance attribute with a lambda function / not ideal but useful /
When attribute that does not exist is given the the setattr() method it returns None. 
!HOWEVER it does create a new attribute of the instance.
setattr() only sets attributes. 
'''
"""A way to get only the methods from our classes without the dunders and the attributes is: """

print([attribute for attribute in dir(circle) if
       callable(getattr(circle, attribute)) and attribute.startswith('__') is False])  # ['area']

"""
We need to make one more filter to differentiate between a method and a property.

But this is really simple. The main difference is that any property object is NOT callable, while methods can be called!

In Python, we can use the boolean function callable(attribute) to check if the attribute can be called.

method_list = [attribute for attribute in dir(MyClass) if callable(getattr(MyClass, attribute)) and attribute.startswith('__') is False]
print(method_list)

method_list = []
 
# attribute is a string representing the attribute name
for attribute in dir(MyClass):
    # Get the attribute value
    attribute_value = getattr(MyClass, attribute)
    # Check that it is callable
    if callable(attribute_value):
        # Filter all dunder (__ prefix) methods
        if attribute.startswith('__') == False:
            method_list.append(attribute)
 
print(method_list)
source : https://www.askpython.com/python/examples/find-all-methods-of-class
"""
delattr(pesho, 'citie')
"""
delattr() method delete the method if it exist. If not raise error.
Source: buildsin
    Deletes the named attribute from the given object.
    
    delattr(x, 'y') is equivalent to ''del x.y''
"""
