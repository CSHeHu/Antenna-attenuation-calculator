class Component:
    def __init__(self, amount = 0, attenuation = 0):
        """
        Initializes a class for components. Each component and cable will
        have amount and attenuation values
        """

        self.__amount = amount
        self.__attenuation = attenuation

    def get_amount(self):
        return self.__amount

    def get_attenuation(self):
        return self.__attenuation



