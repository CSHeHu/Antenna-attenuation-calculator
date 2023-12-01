from Component import Component

class Printer:

    def __init__(self, components, sum_low, sum_high, tilt):

        self.__components = components
        self.__sum_low = sum_low
        self.__sum_high = sum_high
        self.__tilt = tilt

    def print_calculations(self, save_file):

        save_file.write(f"Antenna grid attenuation calculations:\n")
        save_file.write(f"{'Component':<20}{'t50Mhz(dB)':<15}{'1000MHz(dB)':<15}{'Pcs':<10}\n")
        save_file.write("\n")

        for index, component in enumerate(self.__components):
            if component.get_amount() != 0 and component.get_amount() is not None:
                save_file.write(f"{component.get_type():<20}{component.get_attenuation_low():<15}{component.get_attenuation_high():<15}{component.get_amount():<10}\n")
        save_file.write("\n")
        save_file.write(f"Total 50MHz attenuatin: {self.__sum_low:.1f}dB\n")
        save_file.write(f"Total 1000MHz attenuatin: {self.__sum_high:.1f}dB\n")
        save_file.write(f"Tilt: {self.__tilt:.1f}dB\n")
        save_file.write("\n")