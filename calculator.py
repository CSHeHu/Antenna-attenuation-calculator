class Calculator:
    def __init__(self, components):
        self.__components = components

    def calculate_low_att(self):
        """
        Calculates the total attenuations in low frequency
        :return: float, total sum of low frequency attenuation
        """
        total_low_att = 0
        for index, component in enumerate(self.__components):
            try:
                low_att = float(component.get_attenuation_low())
                pcs = float(component.get_amount())
                total_low_att = total_low_att + (pcs * low_att)
            except ValueError:
                total_low_att += 0
        return total_low_att

    def calculate_high_att(self):
        """
        Calculates the total attenuations in high frequency
        :return: float, total sum of low frequency attenuation
        """
        total_high_att = 0
        for index, component in enumerate(self.__components):
            try:
                high_att = float(component.get_attenuation_high())
                pcs = float(component.get_amount())
                total_high_att = total_high_att + (pcs * high_att)
            except ValueError:
                total_high_att += 0
        return total_high_att

    def calculate_tilt(self, high, low):
        """
        Calculates the tilt between low and high attenuations
        :return: float, signal tilt
        """
        try:
            tilt = high - low
        except ValueError:
            tilt = 0
        return tilt