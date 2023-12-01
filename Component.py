class Component:


    def __init__(self, type = "default", attenuation_low = 0, attenuation_high = 0):
        """
        Initializes a class for components. Each component and cable will
        have amount and attenuation values
        """
        self.__type = type
        self.__amount = 0
        self.__attenuation_low = attenuation_low
        self.__attenuation_high = attenuation_high

    def __str__(self):
        return f"{self.__type},\t\t{self.__attenuation_low}db,\t{self.__attenuation_high}db"

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_attenuation_low(self):
        return self.__attenuation_low

    def get_attenuation_high(self):
        return self.__attenuation_high

    def get_type(self):
        return self.__type





