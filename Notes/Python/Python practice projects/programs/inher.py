class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Canine")
        self.breed = breed # Attributes specifically for dog

    def make_sound(self):
        print("Woof!")

generic_animal = Animal("Unknown")
specific_dog = Dog("Labrador")

generic_animal.make_sound()
specific_dog.make_sound()