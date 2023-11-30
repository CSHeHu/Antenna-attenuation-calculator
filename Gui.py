import customtkinter as tk


class Gui:
    def __init__(self, components):
        """
        Initializes the GUI. Gets the component info's as a parameter.
        :param components: list, class Component objects. Components have
        attributes like type, amount, high and low attenuations.
        """
        self.__components = components  # a list of class Component objects
        self.__pcs_entries = []
        # Store the entry fields for GUI (not their values)

        tk.set_appearance_mode("system")
        tk.set_default_color_theme("blue")

        self.__root = tk.CTk()
        self.__root.geometry("600x1200")
        self.__root.title("Antenna attenuation calculator")
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)

        self.printout_components_frame() # creates the main frame with
        # components, their info etc
        self.add_read_button_frame()
        self.add_sums_frame()


        self.__root.mainloop()



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

    def printout_components_frame(self):
        """
        Creates the main components frame for GUI
        """
        px = 5
        py = 5
        self.__components_frame = tk.CTkFrame(self.__root)
        self.__components_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.__components_frame.grid(row=0, column=0, padx=px,
        pady=py, sticky="nsew")

        self.printout_component_labels()
        self.printout_components()

    def printout_component_labels(self):
        """
        Creates the main labels for components from labels
        :return:
        """
        px = 5
        py = 5
        label01 = tk.CTkLabel(self.__components_frame, text="Component",
                              fg_color="transparent")
        label01.grid(row=0, column=0, padx=px, pady=py, sticky="nsew")
        label02 = tk.CTkLabel(self.__components_frame, text="Attenuation, low",
                              fg_color="transparent")
        label02.grid(row=0, column=1, padx=px, pady=py, sticky="nsew")
        label02 = tk.CTkLabel(self.__components_frame, text="Attenuation, high",
                              fg_color="transparent")
        label02.grid(row=0, column=2, padx=px, pady=py, sticky="nsew")

    def printout_components(self):
        """
        Goes trough the list of components and prints out their information.
        After each component a entry field will be created which are stored
        in a list
        """
        px = 5
        py = 5
        for index, component in enumerate(self.__components, start=1):
            label1 = tk.CTkLabel(self.__components_frame,
            text=component.get_type(), fg_color="transparent")
            label1.grid(row=index, column=0, padx=px, sticky="nsew")

            label2 = tk.CTkLabel(self.__components_frame,
            text=component.get_attenuation_low(), fg_color="transparent")
            label2.grid(row=index, column=1, padx=px, sticky="nsew")

            label3 = tk.CTkLabel(self.__components_frame,
            text=component.get_attenuation_high(), fg_color="transparent")
            label3.grid(row=index, column=2, padx=px, sticky="nsew")

            pcs_entry = tk.CTkEntry(self.__components_frame, placeholder_text="pcs")
            pcs_entry.grid(row=index, column=3, padx=px, pady=py, sticky="nsew")
            self.__pcs_entries.append(pcs_entry)  # Store the amounts
            # of components to list from entry fields

    def add_read_button_frame(self):
        """
        Creates a new frame where the total sums of attenuations will be shown
        and the read info button will be created
        :return:
        """
        px = 5
        py = 5
        self.__read_frame = tk.CTkFrame(self.__root)
        self.__read_frame.grid_columnconfigure(0, weight=1)
        self.__read_frame.grid(row=1, column=0, padx=px, pady=py, sticky="ew")

        read_button = tk.CTkButton(self.__read_frame,
        text="Read Entries", command=self.read_entries)
        read_button.grid(row=0, column=0, padx=px, pady=py, sticky="ew")


    def add_sums_frame(self):
        px = 5
        py = 5
        self.__sums_frame = tk.CTkFrame(self.__root)
        self.__sums_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.__sums_frame.grid(row=2, column=0, padx=px, pady=py, sticky="nsew")


        self.__sum_low_static_label = tk.CTkLabel(self.__sums_frame,
        text="Low freq sum:", fg_color="transparent")
        self.__sum_low_static_label.grid(row=0, column=0, padx=px, sticky="nsew")
        self.__sum_high_static_label = tk.CTkLabel(self.__sums_frame,
        text="High freq sum", fg_color="transparent")
        self.__sum_high_static_label.grid(row=0, column=1, padx=px, sticky="nsew")

        self.__sum_low_label = tk.CTkLabel(self.__sums_frame,
        text="-", fg_color="transparent")
        self.__sum_low_label.grid(row=1, column=0, padx=px, sticky="nsew")
        self.__sum_high_label = tk.CTkLabel(self.__sums_frame,
        text="-", fg_color="transparent")
        self.__sum_high_label.grid(row=1, column=1, padx=px, sticky="nsew")



    def read_entries(self):
        for index, component in enumerate(self.__components):
            pcs_value = self.__pcs_entries[index].get()
            # Get the value from the corresponding entry field
            component.set_amount(pcs_value)

        self.__sum_low_label.configure(text=f"{self.calculate_low_att():.1f}")
        self.__sum_high_label.configure(text=f"{self.calculate_high_att():.1f}")
        self.__pcs_amounts = [] # clear the list after calculations


def main():
    ...

if __name__ == "__main__":
    main()
