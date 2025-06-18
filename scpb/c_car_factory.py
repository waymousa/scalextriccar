from i_car import ICar

class CCarFactory:
    @staticmethod
    def create_car(car_id: int, car_type: str) -> ICar:
        if car_type == "ScalextricDigital":
            from c_scalextric_car import CScalextricDigitalCar
            return CScalextricDigitalCar(car_id=car_id)
        elif car_type == "Carrera":
            from c_carrera_car import CCarreraCar
            return CCarreraCar()
        else:
            raise ValueError(f"Unknown car type: {car_type}")