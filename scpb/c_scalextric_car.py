from i_car import ICar

class CScalextricDigitalCar(ICar):
    def __init__(self, car_id: int = 0) -> None:
        self.car_id: int = car_id
        self.car_speed: int = 0
        self.car_brake: bool = 0
        self.car_lane_change: bool = 0
        self.car_current_lap: int = 0

    def get_car_id(self) -> int:
        return self.car_id

    def set_car_speed(self, speed: int) -> None:
        self.car_speed = speed
    
    def get_car_speed(self) -> int:
        return self.car_speed
    
    def set_car_brake(self, brake: bool) -> None:
        self.car_brake = brake

    def get_car_brake(self) -> bool:
        return self.car_brake
    
    def set_car_lane_change(self, lane_change: bool) -> None:
        self.car_lane_change = lane_change

    def get_car_lane_change(self) -> bool:
        return self.car_lane_change
    
    def set_car_state(self, speed: int, brake: bool, lane_change: bool):
        self.set_car_speed(speed)
        self.set_car_brake(brake)
        self.set_car_lane_change(lane_change)

    def get_car_state(self) -> tuple:
        return self.car_speed, self.car_brake, self.car_lane_change
