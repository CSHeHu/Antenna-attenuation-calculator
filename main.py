"""
A program which does antenna attenuation calculations according to users
inputs.
HeHu
20231127
"""

from Component import Component
from Gui import Gui

def import_from_file():
    try:
        file_stream = open("components.txt", mode="r")
    except OSError:
        return None

    component_list = []
    for line in file_stream:
        line_list = line.rstrip().split(";")
        component_name = line_list[0]
        component_attenuation_low = line_list[1]
        component_attenuation_high = line_list[2]

        component = Component(component_name, component_attenuation_low, component_attenuation_high)
        component_list.append(component)

    file_stream.close()
    return component_list


def main():
    component_list = import_from_file()

    ui = Gui(component_list)




if __name__ == "__main__":
    main()