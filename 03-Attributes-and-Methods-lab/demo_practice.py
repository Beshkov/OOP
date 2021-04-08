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

'''
point of using getattr() method is so if you do not know the given attribute "name" 
and you are getting it from elsewhere.
The getattr() method take two arguments: 
on position one -> object ; position two  -> an attribute if such exist in the object. 
On that Note: you can also give a method and it will store attribute.  
!IMPORTANT: if attribute that does not exist in the object is given it is risen "AttributeError" / check line 24 /
TO PREVENT THE ERROR: you can give an third argument what getattr() to return if the second argument is not 
found withing the object. / for ref line 25/
'''
