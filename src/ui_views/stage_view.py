from tkinter import ttk, constants

class StageView:
    def __init__(self, root, go_back_button, stage_one_button, stage_two_button, stage_three_button, stage_four_button, stage_five_button, stage_six_button, stage_seven_button, stage_eight_button, stage_nine_button):
        self._root = root
        self._stage_one_button = stage_one_button
        self._stage_two_button = stage_two_button
        self._stage_three_button = stage_three_button
        self._stage_four_button = stage_four_button
        self._stage_five_button = stage_five_button
        self._stage_six_button = stage_six_button
        self._stage_seven_button = stage_seven_button
        self._stage_eight_button = stage_eight_button
        self._stage_nine_button = stage_nine_button
        self._go_back_button = go_back_button
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Valitse taso")
        button_stage_one = ttk.Button(master=self._frame, text="Taso 1", command=self._stage_one_button)
        button_stage_two = ttk.Button(master=self._frame, text="Taso 2", command=self._stage_two_button)
        button_stage_three = ttk.Button(master=self._frame, text="Taso 3", command=self._stage_three_button)
        button_stage_four = ttk.Button(master=self._frame, text="Taso 4", command=self._stage_four_button)
        button_stage_five = ttk.Button(master=self._frame, text="Taso 5", command=self._stage_five_button)
        button_stage_six = ttk.Button(master=self._frame, text="Taso 6", command=self._stage_six_button)
        button_stage_seven = ttk.Button(master=self._frame, text="Taso 7", command=self._stage_seven_button)
        button_stage_eight = ttk.Button(master=self._frame, text="Taso 8", command=self._stage_eight_button)
        button_stage_nine = ttk.Button(master=self._frame, text="Taso 9", command=self._stage_nine_button)
        button_go_back = ttk.Button(master=self._frame, text="Takaisin", command=self._go_back_button)

        label.grid(row=0, column=1, padx=5, pady=5)
        button_stage_one.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_two.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_three.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_four.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_five.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_six.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_seven.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_eight.grid(row=2, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_stage_nine.grid(row=3, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_go_back.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=150)
        self._frame.grid_columnconfigure(1, weight=1, minsize=150)
        self._frame.grid_columnconfigure(2, weight=1, minsize=150)
