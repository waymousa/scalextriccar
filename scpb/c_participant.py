class CParticipant:

    def __init__(self):
        self.driver: str = None
        self.car: int = None
        self.lap_times = []

    def set_driver(self, driver: str) -> None:
        self.driver = driver

    def set_car(self, car: int) -> None:
        self.car = car

    def get_driver(self) -> str:
        return self.driver

    def get_car(self) -> str:
        return self.car
    
    def get_car_current_lap(self) -> int:
        return self.car_current_lap

    def set_car_current_lap(self, lap: int) -> None:
        self.car_current_lap = lap

    def get_latest_lap_time(self) -> int:
        if self.lap_times:
            return self.lap_times[-1]
        return None

    def set_latest_lap_time(self, lap_time: int) -> None:
        self.lap_times.append(lap_time) 