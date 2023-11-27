class Component:


    def __init__(self, type = "default", attenuation_low = 0, attenuation_high = 0, amount = 0):
        """
        Initializes a class for components. Each component and cable will
        have amount and attenuation values
        """
        self.__type = type
        self.__amount = amount
        self.__attenuation_low = attenuation_low
        self.__attenuation_high = attenuation_high

    def __str__(self):
        return f"{self.__type}, {self.__attenuation_low}, {self.__attenuation_high}"

    def get_amount(self):
        return self.__amount

    def get_attenuation_low(self):
        return self.__attenuation_low

    def get_attenuation_high(self):
        return self.__attenuation_high

    def get_type(self):
        return self.__type




