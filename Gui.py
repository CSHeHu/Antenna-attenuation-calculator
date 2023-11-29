import customtkinter as tk



class Gui:
    def __init__(self, components):
        self.__components = components
        self.__pcs_entries = [] # Store the entry fields
        self.__pcs_amounts = [] # Stores the amounts of components to calculate

        tk.set_appearance_mode("system")
        tk.set_default_color_theme("blue")

        self.__root = tk.CTk()
        self.__root.geometry("640x480")

        self.__root.title("Antenna attenuation calculator")
        self.__root.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.printout_components_frame()
        self.add_read_button()
        self.__root.mainloop()

    def calculate_low_att(self):
        total_low_att = 0
        for index, component in enumerate(self.__components):
            low_att = float(component.get_attenuation_low())
            pcs = float(self.__pcs_amounts[index])
            total_low_att = total_low_att + (pcs * low_att)
        return total_low_att

    def printout_components_frame(self):
        px = 5
        py = 5
        self.__components_frame = tk.CTkFrame(self.__root)
        self.__components_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.__components_frame.grid(row=0, column=0, padx=px, pady=py, sticky="nsew")

        self.printout_component_labels()
        self.printout_components()

    def printout_component_labels(self):
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
        px = 5
        py = 5
        for index, component in enumerate(self.__components, start=1):
            label1 = tk.CTkLabel(self.__components_frame, text=component.get_type(), fg_color="transparent")
            label1.grid(row=index, column=0, padx=px, sticky="nsew")
            label2 = tk.CTkLabel(self.__components_frame, text=component.get_attenuation_low(), fg_color="transparent")
            label2.grid(row=index, column=1, padx=px, sticky="nsew")
            label3 = tk.CTkLabel(self.__components_frame, text=component.get_attenuation_high(), fg_color="transparent")
            label3.grid(row=index, column=2, padx=px, sticky="nsew")
            pcs_entry = tk.CTkEntry(self.__components_frame, placeholder_text="pcs")
            pcs_entry.grid(row=index, column=3, padx=px, pady=py, sticky="nsew")
            self.__pcs_entries.append(pcs_entry)  # Store the entry fields


    def add_read_button(self):
        px = 5
        py = 5
        self.__read_frame = tk.CTkFrame(self.__root)
        self.__read_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.__read_frame.grid(row=1, column=0, padx=px, pady=py, sticky="nsew")

        read_button = tk.CTkButton(self.__read_frame, text="Read Entries", command=self.read_entries)
        read_button.grid(row=0, column=3, padx=px, pady=py, sticky="nsew")
        self.__sum_low_label = tk.CTkLabel(self.__read_frame, text="low sum", fg_color="transparent")
        self.__sum_low_label.grid(row=0, column=1, padx=px, sticky="nsew")
        self.__sum_high_label = tk.CTkLabel(self.__read_frame, text="high sum", fg_color="transparent")
        self.__sum_high_label.grid(row=0, column=2, padx=px, sticky="nsew")



    def read_entries(self):
        for index, component in enumerate(self.__components):
            pcs_value = self.__pcs_entries[index].get()  # Get the value from the corresponding entry field
            self.__pcs_amounts.append(pcs_value)

        self.__sum_low_label.configure(text=f"{self.calculate_low_att():.1f}")
        self.__pcs_amounts = [] # clear the list after calculations

def main():
    ui = Gui()

if __name__ == "__main__":
    main()
