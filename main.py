"""
A program which does antenna attenuation calculations according to users
inputs.
HeHu
20231127
"""

from Gui import Gui
from fileimporter import FileImporter


def main():
    component_list = FileImporter.import_from_file("components.txt")
    if component_list:
        ui = Gui(component_list)


if __name__ == "__main__":
    main()