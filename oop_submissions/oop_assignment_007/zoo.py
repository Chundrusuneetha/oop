class Deer:
    sound = "Buck Buck"
    breath = "Breathe in air"
    increase_food_in_kgs = 2
    hunt_animal = "deers"
    def __init__(self, age_in_months = 1, breed = "ELK", required_food_in_kgs = 10):
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        self._age_in_months = age_in_months
        self._breed = breed
        if required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        self._required_food_in_kgs = required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod 
    def breathe(cls):
        print(cls.breath)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.increase_food_in_kgs
    
    @classmethod    
    def hunt(cls, animal):
        if not(isinstance(animal, Deer)):
            print(f"No {cls.hunt_animal} to hunt")
        if any([isinstance(i,Deer) for i in animal.no_of_animals]):
            Zoo.reduce_animals(animal)

class Lion(Deer):
    sound = "Roar Roar"
    increase_food_in_kgs = 4
    
class Shark(Deer):
    sound = "Shark Sound"
    increase_food_in_kgs = 8
    breath = "Breathe oxygen from water"
    
    def hunt(self, animal):
        if any([isinstance(i,GoldFish) for i in animal.no_of_animals]):
            Zoo.reduce_animals(animal)
        else:
            print("No GoldFish to hunt")

class GoldFish(Deer):
    sound = "Hum Hum"
    increase_food_in_kgs = 0.2
    breath = "Breathe oxygen from water"
    
class Snake(Deer):
    sound = "Hiss Hiss"
    increase_food_in_kgs = 0.5
    
class Zoo:
    animals_in_zoo = []
    def __init__(self, reserved_food_in_kgs = 0):
        self._no_of_animals = []
        self._reserved_food_in_kgs = reserved_food_in_kgs
        
    @property
    def no_of_animals(self):
        return self._no_of_animals
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def reduce_animals(self):
        for i in self._no_of_animals:
            if isinstance(i, Deer):
                self._no_of_animals.remove(i)
                break
    
    def add_food_to_reserve(self, food_in_kgs):
        self._reserved_food_in_kgs += food_in_kgs
        
    def add_animal(self, added_animal):
        self.animals_in_zoo.append(added_animal)
        self._no_of_animals.append(added_animal)
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.animals_in_zoo)
        
    @staticmethod
    def count_animals_in_given_zoos(zoo_objects):
        count = 0
        for i in zoo_objects:
            count += len(i.no_of_animals)
        return count
        
    def count_animals(self):
        return len(self._no_of_animals)
        
    def feed(self, animal):
        if self._reserved_food_in_kgs >= animal.required_food_in_kgs:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
        else:
            self._reserved_food_in_kgs = 0