from tkinter import ttk, constants

class StartView:
    def __init__(self, root, start_game_button, select_level_button, exit_app_button):
        self._root = root
        self._start_game_button = start_game_button
        self._select_level_button = select_level_button
        self._exit_app_button = exit_app_button

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        button_start = ttk.Button(master=self._frame, text="Aloita peli", command=self._start_game_button)
        button_levels = ttk.Button(master=self._frame, text="Valitse taso", command=self._select_level_button)
        button_exit = ttk.Button(master=self._frame, text="Poistu", command=self._exit_app_button)

        button_start.grid(row=0, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_levels.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_exit.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=200)
