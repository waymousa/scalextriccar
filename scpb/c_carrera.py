from i_controller import IController

class CCarerra(IController):
    def __init__(self):
        self.controller_id = 0
        self.controller_state = 0

    def get_controller_id(self):
        return self.controller_id

    def set_controller_id(self, controller_id):
        self.controller_id = controller_id

    def get_controller_state(self):
        return self.controller_state

    def set_controller_state(self, controller_state):
        self.controller_state = controller_state