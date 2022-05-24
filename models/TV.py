from models.HomeApplience import HomeApplience


class TV(HomeApplience):
    def __init__(self, energy_consumption: float, producer_name: str, price: float,
                 is_digital: bool, placing_type: str):
        super().__init__(energy_consumption, producer_name, price)
        self.__placing_type = placing_type
        self.__is_digital = is_digital

    def __str__(self):
        return super().__str__() + f', digital = {str(self.__is_digital).lower()}, ' \
                                   f'and it is placed on the {self.__placing_type}'
