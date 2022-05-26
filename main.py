from models import HomeApplience, WashingMachine, VacuumCleaner, TV, TapeRecorder, RadioReceiver, MusicCenter

applience = HomeApplience.HomeApplience(10, "Barsik", 1000)
print(applience)
applience.repair_applience(True)
print()

bosch_washing_machine = WashingMachine.WashingMachine(5, "Bosch", 300, True, 5)
print(bosch_washing_machine)
print()

philips_vacuum_cleaner = VacuumCleaner.VacuumCleaner(25, "Philips", 500, 7, False)
print(philips_vacuum_cleaner)
philips_vacuum_cleaner.repair_applience(False)
print()

sony_tv = TV.TV(15, "Sony", 1500, True, 'wall')
print(sony_tv)
print()

philips_tape_recorder = TapeRecorder.TapeRecorder(2, "Philips", 100, False, 'high')
print(philips_tape_recorder)
philips_tape_recorder.repair_applience(True)
print()

motorola_radio_receiver = RadioReceiver.RadioReceiver(3, "Motorola", 10, True, 'low')
print(motorola_radio_receiver)
print()

lg_music_center = MusicCenter.MusicCenter(100, "LG", 15000, True, 150)
print(lg_music_center)
lg_music_center.repair_applience(False)
