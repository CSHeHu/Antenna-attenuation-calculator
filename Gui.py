import customtkinter as tk

START_ROW = 1

class Gui:
    def __init__(self, components):
        self.__components = components
        self.__pcs_entries = []

        tk.set_appearance_mode("system")
        tk.set_default_color_theme("blue")

        self.__root = tk.CTk()
        self.__root.geometry("800x600")

        self.__root.title("Antenna attenuation calculator")
        self.__root.grid_columnconfigure((0, 1, 2, 4, 5), weight=1)

        self.printout_component_labels()
        self.printout_components()
        self.add_read_button()
        self.__root.mainloop()


    def printout_component_labels(self):
        label01 = tk.CTkLabel(self.__root, text="Component",
                              fg_color="transparent")
        label01.grid(row=START_ROW, column=0, padx=1, pady=20, sticky="ew")
        label02 = tk.CTkLabel(self.__root, text="Attenuation, low",
                              fg_color="transparent")
        label02.grid(row=START_ROW, column=1, padx=1, pady=20, sticky="ew")
        label02 = tk.CTkLabel(self.__root, text="Attenuation, high",
                              fg_color="transparent")
        label02.grid(row=START_ROW, column=2, padx=1, pady=20, sticky="ew")

    def printout_components(self):
        row = START_ROW + 1
        for component in self.__components:
            label1 = tk.CTkLabel(self.__root, text=component.get_type(), fg_color="transparent")
            label1.grid(row=row, column=0, sticky="ew")
            label2 = tk.CTkLabel(self.__root, text=component.get_attenuation_low(), fg_color="transparent")
            label2.grid(row=row, column=1, sticky="ew")
            label3 = tk.CTkLabel(self.__root, text=component.get_attenuation_high(), fg_color="transparent")
            label3.grid(row=row, column=2,sticky="ew")
            pcs_entry = tk.CTkEntry(self.__root, placeholder_text="pcs")
            pcs_entry.grid(row=row, column=3, padx=3)
            self.__pcs_entries.append(pcs_entry)  # Store the entry widgets
            row += 1

    def add_read_button(self):
        read_button = tk.CTkButton(self.__root, text="Read Entries", command=self.read_entries)
        read_button.grid(row=6, column=1, padx=20, pady=20, sticky="ew", columnspan=1)

    def read_entries(self):
        for index, component in enumerate(self.__components):
            pcs_value = self.__pcs_entries[index].get()  # Get the value from the corresponding entry field
            print(f"Component: {component.get_type()}, PCS value: {pcs_value}")

def main():
    ui = Gui()

if __name__ == "__main__":
    main()
