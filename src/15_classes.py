# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
      self.lat = lat
      self.lon = lon

# my_location = LatLon(25, 87)
# print(my_location.lat)
# print(my_location.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return '"{self.name}", {self.lat}, {self.lon}'.format(self=self)

# my_waypoint = Waypoint("Tiffany", "Hard", "Large", 25, 87)
# print(my_waypoint.name)
# print(my_waypoint.lat)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, difficulty, size, lat, lon)
        
    def __str__(self):
        return '"{self.name}", {self.difficulty}, {self.size}, {self.lat}, {self.lon}'.format(self=self)

# my_geocache = Geocache("Sophie", "Easy", "Small", 16, 30)
# print(my_geocache.name)
# print(my_geocache.size)
 
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", "Hard", "Extra-Large", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
