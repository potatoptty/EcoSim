class Animal:

    animal_count = 0

    def __init__(self, species, age, lifespan): #animal constructor
        self.species = species
        self.age = age
        self.lifespan = lifespan
        Animal.animal_count += 1

    def aging(self, years):
        self.age += years

    def is_dead(self):
        return self.age > self.lifespan

    def display(self):
        print("This {} is {} years old.".format(self.species,self.age))

class EcoManager:
    def __init__(self):
        self.animals = []
        self.dead_animals = []

    def add_animal(self, species, age, lifespan):
        new_animal = Animal(species, age, lifespan)
        self.animals.append(new_animal)
        return new_animal

    def step_years(self, years):
        move_to_dead = []
        # age all the animals
        for i in self.animals:
            # age the animal
            i.aging(years)
            # mark 'dead' animal for removal later
            if i.is_dead():
                move_to_dead.append(i)
        # process all the dead animals
        for i in move_to_dead:
            self.dead_animals.append(i)
            self.animals.remove(i)

    def print_all(self):
        for i in self.animals:
            i.display()
            
manager = EcoManager() 

# adding some animals to ecosystem 1
l1 = manager.add_animal("lion",1,10)
l2 = manager.add_animal("lion",1,10)
w1 = manager.add_animal("wildebeest",1,20)
