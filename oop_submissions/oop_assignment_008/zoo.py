class Animal:
    increased_food_in_kgs = 0
    sound = "Buck Buck"
    def __init__(self, age_in_months = 1, breed = "ELK", required_food_in_kgs = 10):
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        self._age_in_months = age_in_months
        if required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        self._required_food_in_kgs = required_food_in_kgs
        self._breed = breed
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @property
    def breed(self):
        return self._breed
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.increased_food_in_kgs
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
class HuntingAnimals:
    hunt_animal_sound = "Buck Buck"
    no_animals_to_hunt = "No deers to hunt"
    @classmethod
    def hunt(cls, zoo_object):
        count = 0
        for animal in zoo_object.no_of_animals:
            if animal.sound == cls.hunt_animal_sound:
                count = 1
                zoo_object.no_of_animals.remove(animal)
                Zoo.animals_in_zoo.remove(animal)
                break
        if count == 0:
            print(cls.no_animals_to_hunt)
            
class LandAnimals:
    breath = "Breathe in air"
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
class WaterAnimals:
    breath = "Breathe oxygen from water"
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
class Deer(Animal, LandAnimals):
    sound = "Buck Buck"
    increased_food_in_kgs = 2
    
class Lion(Animal, LandAnimals, HuntingAnimals):
    sound = "Roar Roar"
    increased_food_in_kgs = 4
    
class Shark(Animal, WaterAnimals, HuntingAnimals):
    sound = "Shark Sound"
    increased_food_in_kgs = 8
    hunt_animal_sound = "Hum Hum"
    no_animals_to_hunt = "No GoldFish to hunt"
    
class GoldFish(Animal, WaterAnimals, HuntingAnimals):
    sound = "Hum Hum"
    increased_food_in_kgs = 0.2
    
class Snake(Animal, LandAnimals, HuntingAnimals):
    sound = "Hiss Hiss"
    increased_food_in_kgs = 0.5
    
class Zoo:
    animals_in_zoo = []
    def __init__(self, reserved_food_in_kgs = 0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self._no_of_animals = []
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    @property
    def no_of_animals(self):
        return self._no_of_animals
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.animals_in_zoo)
        
    @staticmethod
    def count_animals_in_given_zoos(zoo_objects):
        count = 0
        for i in zoo_objects:
            count += i.count_animals()
        return count
        
    def add_food_to_reserve(self, food_in_kgs):
        self._reserved_food_in_kgs += food_in_kgs
        
    def add_animal(self, added_animal):
        self.animals_in_zoo.append(added_animal)
        self._no_of_animals.append(added_animal)
        
    def count_animals(self):
        return len(self._no_of_animals)
        
    def feed(self, animal):
        if self._reserved_food_in_kgs >= animal.required_food_in_kgs:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
        else:
            self._reserved_food_in_kgs = 0