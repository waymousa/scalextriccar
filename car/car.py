# Class file for a car

class Car:

    def __init__(self, id=0, speed=0, brake=False, lane_change=False):
        self.id = int(id)
        self.speed = int(speed)
        self.brake = brake
        self.lane_change = lane_change
        
    def __str__(self):
        return f"{self.id}({self.speed},{self.brake},{self.lane_change})"
    
    def set_speed(self, speed):
        self.speed = speed
        
    def get_speed(self):
        return self.speed
        
    def set_brake(self, brake):
        self.brake = brake
        
    def get_brake(self):
        return self.brake
        
    def set_lane_change(self, lane_change):
        self.lane_change = lane_change
        
    def get_lane_change(self):
        return self.lane_change
    
    def set_id(self, id):
        self.id=id
        
    def get_id(self):
        return self.id