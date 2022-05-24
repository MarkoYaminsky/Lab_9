from models.HomeApplience import HomeApplience


class WashingMachine(HomeApplience):
    def __init__(self, energy_consumption: float, producer_name: str, price: float,
                 has_modes: bool, water_consumption: float):
        super().__init__(energy_consumption, producer_name, price)
        self.__water_consumption = water_consumption
        self.__has_modes = has_modes

    def __str__(self):
        return super().__str__() + f', has modes = {str(self.__has_modes).lower()}, and its water consumption is ' \
                                   f' {self.__water_consumption} liters per default wash'
