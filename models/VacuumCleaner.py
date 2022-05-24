from models.HomeApplience import HomeApplience


class VacuumCleaner(HomeApplience):
    def __init__(self, energy_consumption: float, producer_name: str, price: float,
                 noise_level: int, does_wet_cleaning: bool):
        super().__init__(energy_consumption, producer_name, price)
        self.__does_wet_cleaning = does_wet_cleaning
        self.__noise_level = noise_level

    def __str__(self):
        return super().__str__() + f', its noise level is {self.__noise_level},' \
                                   f' and does wet cleaning parameter is {str(self.__does_wet_cleaning).lower()}'
