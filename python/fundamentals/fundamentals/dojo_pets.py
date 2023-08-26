class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.energy = 100
        self.health = 100

# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5

# noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)
        return self

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# Implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

# feed() - feeds the ninja's pet invoking the pet eat() method
# if feed something, print out pet food.
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

my_treats = ['Snausage', 'Bacon', 'Trash Bag']
my_pet_food = ['Pizza', 'Burger']
nibbles = Pet("Mr. Nibbles", "horse", ['nibbles on things', 'is invisible'], "Hey Hey" )


sarang = Ninja("Sarang", "Kim", my_treats, my_pet_food, nibbles)
sarang.feed();
sarang.feed();
sarang.feed();

