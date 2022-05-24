from models.HomeApplience import HomeApplience


class RadioReceiver(HomeApplience):
    def __init__(self, energy_consumption: float, producer_name: str, price: float,
                 is_digital: bool, sound_render_quality: str):
        super().__init__(energy_consumption, producer_name, price)
        self.__sound_render_quality = sound_render_quality
        self.__is_digital = is_digital

    def __str__(self):
        return super().__str__() + f', is digital = {str(self.__is_digital).lower()}' \
                                   f', and its sound render is {self.__sound_render_quality} quality'
