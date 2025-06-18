from i_car import ICar

class CCarreraCar(ICar):
    def __init__(self):
        self.car_id = 0
        self.car_speed = 0
        self.car_brake = 0
        self.car_lane_change = 0
        self.car_current_lap = 0
        self.lap_times = []

    def get_car_id(self):
        return self.car_id

    def set_car_speed(self, speed):
        self.car_speed = speed
    
    def get_car_speed(self):
        return self.car_speed
    
    def set_car_brake(self, brake):
        self.car_brake = brake

    def get_car_brake(self):
        return self.car_brake
    
    def set_car_lane_change(self, lane_change):
        self.car_lane_change = lane_change

    def get_car_lane_change(self):
        return self.car_lane_change
    
    def set_car_state(self, speed, brake, lane_change):
        self.set_car_speed(speed)
        self.set_car_brake(brake)
        self.set_car_lane_change(lane_change)

    def get_car_state(self):
        return self.car_speed, self.car_brake, self.car_lane_change
    
    def get_car_current_lap(self):
        return self.car_current_lap

    def set_car_current_lap(self, lap):
        self.car_current_lap = lap

    def get_latest_lap_time(self):
        if self.lap_times:
            return self.lap_times[-1]
        return None

    def set_latest_lap_time(self, lap_time):
        self.lap_times.append(lap_time) 