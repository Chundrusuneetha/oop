class Car:
    sound = "Beep Beep"
    def __init__(self, color = 'red', max_speed = 0, acceleration = 0, tyre_friction = 0):
        self._color = color
        self._max_speed = 0
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")
        self._max_speed = max_speed
        if acceleration < 0:
            raise ValueError("Invalid value for acceleration")
        self._acceleration = acceleration
        if tyre_friction < 0:
            raise ValueError("Invalid value for tyre_friction")
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._current_speed = 0
            
    @property
    def color(self):
        return self._color
    
    @property
    def max_speed(self):
        return self._max_speed
            
    @property
    def acceleration(self):
        return self._acceleration
            
    @property
    def tyre_friction(self):
        return self._tyre_friction
    
    @property
    def current_speed(self):
        return self._current_speed
    
    @property
    def is_engine_started(self):
        return self._is_engine_started
        
    def start_engine(self):
        self._is_engine_started = True
        
    def stop_engine(self):
        self._is_engine_started = False
        
    def accelerate(self):
        if self._is_engine_started == False:
            print("Start the engine to accelerate")
        elif self._is_engine_started and (self._current_speed + self._acceleration) <= self._max_speed:
                self._current_speed += self._acceleration
        else:
            self._current_speed = self._max_speed
    
    def apply_brakes(self):
        if (self._current_speed - self._tyre_friction) >= 0:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
                
    def sound_horn(self):
        if self._is_engine_started:
            print(self.sound)
        else:
            print("Start the engine to sound_horn")
            
class Truck(Car):
    sound = "Honk Honk"
    def __init__(self, color = 'red', max_speed = 0, acceleration = 0, tyre_friction = 0, max_cargo_weight = 0):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._max_cargo_weight = max_cargo_weight
        self._loads = 0
        
    @property
    def loads(self):
        return self._loads
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self, cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed != 0:
            print("Cannot load cargo during motion")
        else:
            if cargo_weight + self._loads > self._max_cargo_weight:
                print(f'Cannot load cargo more than max limit: {self._max_cargo_weight}')
            else:
                self._loads += cargo_weight
    
    def unload(self, cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed != 0:
            print("Cannot unload cargo during motion")
        else:
            self._loads -= cargo_weight