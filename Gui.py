import customtkinter as tk

class Gui:
    def __init__(self, components):
        self.__components = components
        tk.set_appearance_mode("system")
        tk.set_default_color_theme("blue")

        self.__root = tk.CTk()
        self.__root.geometry("1920x1080")

        self.__root.title("Antenna attenuation calculator")
        self.__root.grid_columnconfigure((0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1)

        """
        self.__root.button = tk.CTkButton(self.__root, text="my button",
                                              command=self.button_callback)
        self.__root.button.grid(row=6, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
        self.__root.checkbox_1 = tk.CTkCheckBox(self.__root, text="checkbox 1")
        self.__root.checkbox_1.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
        self.__root.checkbox_2 = tk.CTkCheckBox(self.__root, text="checkbox 2")
        self.__root.checkbox_2.grid(row=6, column=2, padx=20, pady=(0, 20), sticky="w")
        """

        self.printout_component_labels()
        self.__root.mainloop()

    def button_callback(self):
        print("button pressed") # Test to be removed later

    def printout_component_labels(self):
        label01 = tk.CTkLabel(self.__root, text="Component",
                              fg_color="transparent")
        label01.grid(row=0, column=0, padx=1, pady=20, sticky="ew")
        label02 = tk.CTkLabel(self.__root, text="Attenuation, low",
                              fg_color="transparent")
        label02.grid(row=0, column=1, padx=1, pady=20, sticky="ew")
        label02 = tk.CTkLabel(self.__root, text="Attenuation, high",
                              fg_color="transparent")
        label02.grid(row=0, column=2, padx=1, pady=20, sticky="ew")

        row = 1
        for component in self.__components:
            label1 = tk.CTkLabel(self.__root, text=component.get_type(), fg_color="transparent")
            label1.grid(row=row, column=0, padx=1, pady=5, sticky="ew")
            label2 = tk.CTkLabel(self.__root, text=component.get_attenuation_low(), fg_color="transparent")
            label2.grid(row=row, column=1, padx=1, pady=5, sticky="ew")
            label3 = tk.CTkLabel(self.__root, text=component.get_attenuation_high(), fg_color="transparent")
            label3.grid(row=row, column=2, padx=1, pady=5, sticky="ew")
            row += 1

def main():
    ui = Gui()

if __name__ == "__main__":
    main()
