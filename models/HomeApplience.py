class HomeApplience:
    def __init__(self, energy_consumption: float, producer_name: str, price: float) -> None:
        self._energy_consumption = energy_consumption
        self._producer_name = producer_name
        self._price = price

    def __str__(self):
        return f'Applience {self._producer_name} consumes {self._energy_consumption}W and costs ${self._price}'

    def repair_applience(self, has_guarantee) -> None:
        reparation_price = self._price // 3 if not has_guarantee else 0
        print(f"Your applience has been repaired. Reparation price = ${reparation_price}")
