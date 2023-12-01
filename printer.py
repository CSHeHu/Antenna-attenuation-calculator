from Component import Component

class Printer:


    def __init__(self, components, sum_low, sum_high, tilt):

        self.__components = components
        self.__sum_low = sum_low
        self.__sum_high = sum_high
        self.__tilt_sum = tilt

    def print_calculations(self):
        print("Antenna grid attenuation calculations:")
        print("Component\t\t50Mhz\t1000MHz\tPcs")
        print()

        for index, component in enumerate(self.__components):
            if component.get_amount() != 0 and component.get_amount() is not None:
                print(f"{component}, {component.get_amount()}pcs")

