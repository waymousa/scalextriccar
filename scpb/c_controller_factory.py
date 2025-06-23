from i_controller import IController
from c_event_manager import CEventManager

class CControllerFactory:

    @staticmethod
    def create_controller(event_manager: CEventManager, controller_type: str) -> IController:
        if controller_type == "ScalextricSixCarPowerBase":
            from c_scalextrix_scpb import CScalextricSixCarPowerBase
            return CScalextricSixCarPowerBase(event_manager)
        elif controller_type == "Carerra":
            from c_carrera import CCarerra
            return CCarerra()
        else:
            raise ValueError("Invalid controller type")