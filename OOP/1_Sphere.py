import math


class Sphere(object):
    def __init__(self, radius=1, x=1, y=1, z=1):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        volume = 4 / 3 * math.pi * math.pow(self.radius, 3)
        return volume

    def get_square(self):
        square = 4 * math.pi * math.pow(self.radius, 2)
        return square

    def get_radius(self):
        return self.radius

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


sphere = Sphere(5, 3, 2, 1)
print('Volume', sphere.get_volume())
print('Square', sphere.get_square())
print('Radius = ', sphere.get_radius(), 'Center', sphere.get_center())
sphere.set_radius(200)
sphere.set_center(10, 22, 33)
print('Radius = ', sphere.get_radius(), 'Center', sphere.get_center())
