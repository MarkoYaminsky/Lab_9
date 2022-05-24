from models.HomeApplience import HomeApplience


class MusicCenter(HomeApplience):
    def __init__(self, energy_consumption: float, producer_name: str, price: float,
                 is_bluetooth: bool, max_volume: float):
        super().__init__(energy_consumption, producer_name, price)
        self.__max_volume = max_volume
        self.__is_bluetooth = is_bluetooth

    def __str__(self):
        return super().__str__() + f', is connected via bluetooth = {str(self.__is_bluetooth).lower()}' \
                                   f', and its maximum volude is {self.__max_volume} dB'
