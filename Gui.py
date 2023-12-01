import customtkinter as tk
from calculator import Calculator

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
        self.__pcs_amounts = []
        self.__root = None
        self.__scrollable_frame = None
        self.__read_frame = None
        self.__sums_frame = None
        self.__sum_low_label = None
        self.__sum_high_label = None
        self.__tilt_label = None

        self.create_gui()


    def create_gui(self):
        tk.set_appearance_mode("system")
        tk.set_default_color_theme("blue")

        self.__root = tk.CTk()
        try:
            self.__root.iconbitmap('antenna.ico')
        except Exception:
            pass
        self.__root.geometry("600x700")
        self.__root.title("Antenna cablegrid attenuation calculator")
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.resizable(width=False, height=False)  # Disables resizing

        self.create_scrollable_frame()
        self.add_read_button_frame()
        self.add_sums_frame()

        self.__root.mainloop()

    def create_scrollable_frame(self):
        """
        Creates the scrollable frame for components
        """
        self.__scrollable_frame = tk.CTkScrollableFrame(self.__root,
        width=550, height=600)
        self.__scrollable_frame.grid(row=0, column=0, padx=20, pady=20)
        self.__scrollable_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Call the methods to print the component labels and components
        self.printout_component_labels()
        self.printout_components()

    def printout_component_labels(self):
        """
        Creates the main labels for components from labels
        :return:
        """
        px = 5
        py = 5
        label01 = tk.CTkLabel(self.__scrollable_frame, text="Component",
                              fg_color="transparent")
        label01.grid(row=0, column=0, padx=px, pady=py, sticky="nsew")
        label02 = tk.CTkLabel(self.__scrollable_frame, text="47MHz",
                              fg_color="transparent")
        label02.grid(row=0, column=1, padx=px, pady=py, sticky="nsew")
        label03 = tk.CTkLabel(self.__scrollable_frame, text="1000MHz",
                              fg_color="transparent")
        label03.grid(row=0, column=2, padx=px, pady=py, sticky="nsew")
        label04 = tk.CTkLabel(self.__scrollable_frame, text="Amount of equipment",
                              fg_color="transparent")
        label04.grid(row=0, column=3, padx=px, pady=py, sticky="nsew")

    def printout_components(self):
        """
        Goes trough the list of components and prints out their information.
        After each component a entry field will be created which are stored
        in a list
        """
        px = 5
        py = 5
        for index, component in enumerate(self.__components, start=1):
            label1 = tk.CTkLabel(self.__scrollable_frame,
            text=component.get_type(), fg_color="transparent")
            label1.grid(row=index, column=0, padx=px, sticky="nsew")

            label2 = tk.CTkLabel(self.__scrollable_frame,
            text=component.get_attenuation_low(), fg_color="transparent")
            label2.grid(row=index, column=1, padx=px, sticky="nsew")

            label3 = tk.CTkLabel(self.__scrollable_frame,
            text=component.get_attenuation_high(), fg_color="transparent")
            label3.grid(row=index, column=2, padx=px, sticky="nsew")

            pcs_entry = tk.CTkEntry(self.__scrollable_frame, placeholder_text="pcs")
            pcs_entry.grid(row=index, column=3, padx=px, pady=py, sticky="nsew")
            self.__pcs_entries.append(pcs_entry)  # Store the entryfields
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
        """
        Creates the frame for final sum calculations
        """
        px = 5
        py = 5
        self.__sums_frame = tk.CTkFrame(self.__root)
        self.__sums_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.__sums_frame.grid(row=2, column=0, padx=px, pady=py, sticky="nsew")


        sum_low_static_label = tk.CTkLabel(self.__sums_frame,
        text="47MHz sum (25-40dB):", fg_color="transparent")
        sum_low_static_label.grid(row=0, column=0, padx=px, sticky="nsew")
        sum_high_static_label = tk.CTkLabel(self.__sums_frame,
        text="1000MHz sum (25-40dB)", fg_color="transparent")
        sum_high_static_label.grid(row=0, column=1, padx=px, sticky="nsew")
        tilt_static_label = tk.CTkLabel(self.__sums_frame,
        text="Tilt (max. 15dB)", fg_color="transparent")
        tilt_static_label.grid(row=0, column=2, padx=px, sticky="nsew")

        self.__sum_low_label = tk.CTkLabel(self.__sums_frame,
        text="-dB", fg_color="transparent")
        self.__sum_low_label.grid(row=1, column=0, padx=px, sticky="nsew")
        self.__sum_high_label = tk.CTkLabel(self.__sums_frame,
        text="-dB", fg_color="transparent")
        self.__sum_high_label.grid(row=1, column=1, padx=px, sticky="nsew")
        self.__tilt_label = tk.CTkLabel(self.__sums_frame,
        text="-dB", fg_color="transparent")
        self.__tilt_label.grid(row=1, column=2, padx=px, sticky="nsew")

    def add_clear_quit_frame(self):
        """
        Creates the frame for final sum calculations
        """
        px = 5
        py = 5
        pass

    def read_entries(self):
        """
        Reads the user inputs from entryfields. Stores the input in every
        component objects attributes. After that the calculations are done.
        :return:
        """
        for index, component in enumerate(self.__components):
            pcs_value = self.__pcs_entries[index].get()
            # Get the value from the corresponding entry field and store
            # them in components amount attribute
            component.set_amount(pcs_value)

        calculator = Calculator(self.__components)
        low_sum = calculator.calculate_low_att()
        high_sum = calculator.calculate_high_att()
        tilt = calculator.calculate_tilt(low_sum, high_sum)
        self.__sum_low_label.configure(text=f"{low_sum:.1f}dB")
        self.__sum_high_label.configure(text=f"{high_sum:.1f}dB")
        self.__tilt_label.configure(text=f"{tilt:.1f}dB")
        self.__pcs_amounts = [] # clear the list after calculations





