from Component import Component


class FileImporter:
    @staticmethod
    def import_from_file(file_name):
        try:
            with open(file_name, mode="r") as file_stream:
                component_list = []
                for line in file_stream:
                    if line.isspace() or line.startswith('#'):
                        continue

                    line_list = line.rstrip().split(";")
                    if len(line_list) != 3:
                        continue

                    try:
                        float(line_list[1])
                        float(line_list[2])
                    except ValueError:
                        continue

                    component_name = line_list[0]
                    component_attenuation_low = float(line_list[1])
                    component_attenuation_high = float(line_list[2])

                    component = Component(component_name,
                    component_attenuation_low, component_attenuation_high)
                    component_list.append(component)

                return component_list
        except OSError:
            return None
