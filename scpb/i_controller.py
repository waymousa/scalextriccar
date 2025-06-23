from abc import ABCMeta, abstractmethod

class IController(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def send_serial_byte_array():
        """Sends a message to the controller."""
        raise NotImplementedError("This method should be overridden by subclasses")