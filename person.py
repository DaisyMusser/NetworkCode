
'''
Represents a person, has:
    + full name[s]
    + simple name
'''

# Maybe helpful to convert from full name to simple
# here? maybe not. think about it cutie ;)
class Person:
    def __init__(self, full_name, simple_name):
        self.full_name   = full_name
        self.simple_name = simple_name

    # todo: don't concat! gross
    def __str__(self):
        return str(self.simple_name)


