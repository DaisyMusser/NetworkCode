
'''
Represents an arrest. Has:
    + object id
    + location id
    + city
    + Street
'''

class Arrest:
    def __init__(self, object_id, location_id, city, street):
        self.object_id = object_id
        self.location_id = location_id
        self.city = city
        self.street = street

