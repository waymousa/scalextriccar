from abc import ABCMeta, abstractmethod

class ICar(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_car_id(self) -> int:
        """Returns the unique identifier for the car."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def set_car_speed(self, speed: int) -> None:
        """Sets the speed of the car to the car controller."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def get_car_speed():
        """Returns the current speed of the car."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def set_car_brake():
        """Sets the brake state of the car to the car controller."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def get_car_brake():
        """Returns the current brake state of the car."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def set_car_lane_change():
        """Sets the lane change state of the car to the car controller."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def get_car_lane_change():
        """Returns the current lane change state of the car."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def set_car_state():
        """Sets the state of the car to the car controller."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    @abstractmethod
    def get_car_state():
        """Returns the current state of the car."""
        raise NotImplementedError("This method should be overridden by subclasses")