from models.HomeApplience import HomeApplience


class TapeRecorder(HomeApplience):
    def __init__(self, energy_consumption: float, producer_name: str, price: float,
                 is_vintage: bool, sound_render_quality: str):
        super().__init__(energy_consumption, producer_name, price)
        self.__sound_render_quality = sound_render_quality
        self.__is_vintage = is_vintage

    def __str__(self):
        return super().__str__() + f', is vintage = {str(self.__is_vintage).lower()}' \
                                   f', and its sound render is {self.__sound_render_quality} quality'
