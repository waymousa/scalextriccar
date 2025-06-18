from i_controller import IController

class CControllerFactory:

    @staticmethod
    def create_controller(controller_type: str) -> IController:
        if controller_type == "ScalextricSixCarPowerBase":
            from c_scalextrix_scpb import CScalextricSixCarPowerBase
            return CScalextricSixCarPowerBase()
        elif controller_type == "Carerra":
            from c_carrera import CCarerra
            return CCarerra()
        else:
            raise ValueError("Invalid controller type")