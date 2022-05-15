import sys
from tkinter import Tk
from ui_views.start_view import StartView
from ui_views.stage_view import StageView
from game import Game

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _start_game_button(self):
        Game()

    def _select_level_button(self):
        self._show_level_view()

    def _exit_app_button(self):
        sys.exit()

    def _stage_one_button(self):
        Game(0, True)

    def _stage_two_button(self):
        Game(1, True)

    def _stage_three_button(self):
        Game(2, True)

    def _stage_four_button(self):
        Game(3, True)

    def _stage_five_button(self):
        Game(4, True)

    def _stage_six_button(self):
        Game(5, True)

    def _stage_seven_button(self):
        Game(6, True)

    def _stage_eight_button(self):
        Game(7, True)

    def _stage_nine_button(self):
        Game(8, True)

    def _go_back_button(self):
        self._show_start_view()

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._start_game_button,
            self._select_level_button,
            self._exit_app_button
        )

        self._current_view.pack()

    def _show_level_view(self):
        self._hide_current_view()

        self._current_view = StageView(
            self._root,
            self._go_back_button,
            self._stage_one_button,
            self._stage_two_button,
            self._stage_three_button,
            self._stage_four_button,
            self._stage_five_button,
            self._stage_six_button,
            self._stage_seven_button,
            self._stage_eight_button,
            self._stage_nine_button
        )

        self._current_view.pack()

window = Tk() # pylint: disable=invalid-name
window.title("World's Hardest Game")

ui = UI(window) # pylint: disable=invalid-name
ui.start()

window.mainloop()
