# class class_name(parent_class_name)
class Animal(object):

    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        print('name: {0}, age: {1}, is_hungry: {2}'.format(self.name, self.age, self.is_hungry))
                
# create class object
cat = Animal('dog', 12, False)
cat.description()
