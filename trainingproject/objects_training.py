class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)



class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')



# Main program
my_dog = Robot_Dog('Spot', 'Chihuaha')
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()





