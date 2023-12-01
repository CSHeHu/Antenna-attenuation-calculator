class Fileexporter:

    def __init__(self, calculations):
        self.__calculations = calculations
        self.export_to_file()

    def export_to_file(self):
        try:
            save_file = open("calculations.txt", mode="a")
        except OSError:
            return None

        self.__calculations.print_calculations(save_file)

        save_file.close()
