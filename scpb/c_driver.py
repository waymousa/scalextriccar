class CDriver:
    def __init__(self, name: str):
        self.driver_name = name

    def get_driver_name(self):
        return self.driver_name
    
    def set_driver_name(self, name):
        self.driver_name = name