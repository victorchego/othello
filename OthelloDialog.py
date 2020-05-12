# Victor Chang 

DEFAULT_FONT = ('Helvetica', 14)
DEFAULT_COL = 4
DEFAULT_ROW = 4
DEFAULT_TOP_LEFT = 'WHITE'
DEFAULT_MOVE = 'BLACK'
DEFAULT_WINMODE = 'MOST'

import tkinter
import OthelloGame

class WinnerDialog:
    def __init__(self, game_state: OthelloGame.Game):
        '''  Opens a winner dialog box based off the game state in the parameter '''
        self._dialog_window = tkinter.Toplevel()

        status_label = tkinter.Label(
            master = self._dialog_window,
            text = 'No more available moves.  GAME OVER',
            font = DEFAULT_FONT)

        status_label.grid(row = 0, column = 0,
                          sticky = tkinter.W + tkinter.N)

        win_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Winner: \t' + game_state._winner,
            font = DEFAULT_FONT)
        
        win_label.grid(row = 1, column = 0,
                       sticky = tkinter.W + tkinter.N)

        score_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Black: ' + str(game_state._count['Black']) + '\t' +
            'White: ' + str(game_state._count['White']),
            font = DEFAULT_FONT)

        score_label.grid(row = 2, column = 0,
                       sticky = tkinter.W + tkinter.N)

        ok_button = tkinter.Button(
            master = self._dialog_window, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 3, column = 0, columnspan =2, padx = 10, pady = 10,
                       sticky = tkinter.E + tkinter.S)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)

    def show(self) -> None:
        ''' This makes it a modal dialog box '''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def _on_ok_button(self) -> None:
        ''' Destroys the winner dialog box '''
        self._dialog_window.destroy() 

class ErrorDialog:
    def __init__(self):
        ''' Opens an error dialog box '''
        self._dialog_window = tkinter.Toplevel()

        label_1 = tkinter.Label(
            master = self._dialog_window,
            text = 'One or more fields may have an invalid input.',
            font = DEFAULT_FONT)

        label_1.grid(
            row = 0, column = 0,
            sticky = tkinter.W + tkinter.N)

        label_2 = tkinter.Label(
            master = self._dialog_window,
            text = 'Please make sure all numbers are even integers between 4 and 16 inclusive',
            font = DEFAULT_FONT)

        label_2.grid(
            row = 1, column = 0,
            sticky = tkinter.W + tkinter.N)

        label_3 = tkinter.Label(
            master = self._dialog_window,
            text = 'and all text fields follow the format specified.',
            font = DEFAULT_FONT)

        label_3.grid(
            row = 2, column = 0,
            sticky = tkinter.W + tkinter.N)

        ok_button = tkinter.Button(
            master = self._dialog_window, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 3, column = 0, columnspan =2, padx = 10, pady = 10,
                       sticky = tkinter.E + tkinter.S)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
                
    def show(self) -> None:
        ''' This makes it a modal dialog box '''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def _on_ok_button(self) -> None:
        ''' Destroys the dialog box '''
        self._dialog_window.destroy()

class OptionDialog:
    def __init__(self):
        ''' Opens up an options dialog box. No inputs are treated as the default
        4 by 4 settings with black moving first and white on the top left '''
        self._dialog_window = tkinter.Toplevel()

        col_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of columns [4-16] >>> DEF = 4',
            font = DEFAULT_FONT)

        col_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_entry = tkinter.Entry(
            master = self._dialog_window, width = 3, font = DEFAULT_FONT)

        self._col_entry.grid(
            row = 0, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of rows [4-16] >>> DEF = 4',
            font = DEFAULT_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 3, font = DEFAULT_FONT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        move_label = tkinter.Label(
            master = self._dialog_window, text = 'Which color moves first? [WHITE] or [BLACK] >>> DEF = BLACK',
            font = DEFAULT_FONT)

        move_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._move_entry = tkinter.Entry(
            master = self._dialog_window, width = 6, font = DEFAULT_FONT)

        self._move_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        top_left_label = tkinter.Label(
            master = self._dialog_window, text = 'Which color goes on the top left? [WHITE] or [BLACK] >>> DEF = WHITE',
            font = DEFAULT_FONT)

        top_left_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._top_left_entry = tkinter.Entry(
            master = self._dialog_window, width = 6, font = DEFAULT_FONT)

        self._top_left_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        winmode_label = tkinter.Label(
            master = self._dialog_window, text = 'Select winner for [MOST] or [LEAST] discs >>> DEF = MOST',
            font = DEFAULT_FONT)

        winmode_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._winmode_entry = tkinter.Entry(
            master = self._dialog_window, width = 6, font = DEFAULT_FONT)

        self._winmode_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        ok_button = tkinter.Button(
            master = self._dialog_window, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 5, column = 0, columnspan =2, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)

        #INITIALIZE WITH DEFAULTS
        self._col = DEFAULT_COL
        self._row = DEFAULT_ROW
        self._move = DEFAULT_MOVE
        self._top_left = DEFAULT_TOP_LEFT
        self._winmode = DEFAULT_WINMODE
        self._counter = 0

    def show(self) -> None:
        ''' This makes it a modal dialog box '''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def get_col(self) -> int:
        ''' If the column entry is a positive integer between 4 and 16 inclusive
        then it will return that value, otherwise, the the counter will increase '''
        if self._col_entry.get() != '':
            try:
                self._col = int(self._col_entry.get())
                if self._col %2 == 0 and (4<= self._col <= 16):
                    return int(self._col)
                else:
                    self._counter += 1
                    return DEFAULT_COL
            except:
                self._counter += 1
                return DEFAULT_COL
        else:
            return DEFAULT_COL

    def get_row(self) -> int:
        ''' If the row entry is a positive integer between 4 and 16 inclusive
        then it will return that value, otherwise, the counter will increase '''
        if self._row_entry.get() != '':
            try:
                self._row = int(self._row_entry.get())
                if self._row %2 == 0 and (4<= self._row <= 16):
                    return int(self._row)
                else:
                    self._counter += 1
                    return DEFAULT_ROW
            except:
                self._counter += 1
                return DEFAULT_ROW
        else:
            return DEFAULT_ROW

    def get_move(self) -> str:
        ''' If the move entry is either BLACK or WHITE then it will return
        that value, otherwise, the counter will increase '''
        if self._move_entry.get() != '':
            if self._move_entry.get().upper() in ['BLACK', 'WHITE']:
                return self._move_entry.get().upper()
            else:
                self._counter += 1
                return DEFAULT_MOVE
        else:
            return DEFAULT_MOVE

    def get_top_left(self) -> str:
        ''' If the top left entry is either BLACK or WHITE then it will return
        that value, otherwise, the counter will increase '''
        if self._top_left_entry.get() != '':
            if self._top_left_entry.get().upper() in ['BLACK', 'WHITE']:
                return self._top_left_entry.get().upper()
            else:
                self._counter += 1
                return DEFAULT_TOP_LEFT
        else:
            return DEFAULT_TOP_LEFT

    def get_winmode(self) -> str:
        ''' If the win mode entry is either MOST or LEAST then it will return
        that value, otherwise, the counter will increase '''
        if self._winmode_entry.get() != '':
            if self._winmode_entry.get().upper() in ['MOST', 'LEAST']:
                return self._winmode_entry.get().upper()
            else:
                self._counter += 1
                return DEFAULT_WINMODE
        else:
            return DEFAULT_WINMODE

    def _on_ok_button(self) -> None:
        ''' Assigns the respective values to the attributes and destroys the
        window if there are no invalid inputs.  Otherwise, the box will not
        close until all fields have valid inputs. '''
        
        self._col = self.get_col()
        self._row = self.get_row()
        self._move = self.get_move()
        self._top_left = self.get_top_left()
        self._winmode = self.get_winmode()

        if self._counter == 0:
            self._dialog_window.destroy()
        else:
            self._counter = 0
            ErrorDialog().show()
