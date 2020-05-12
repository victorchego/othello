# Victor Chang

import tkinter
import OthelloGame
import OthelloDialog

DEFAULT_FONT = ('Helvetica', 14)

class Board:
    def __init__(self):
        ''' Opens a root window and creates a new game class.  The board displays
        the correct number of columns and rows and the proper disc placement. '''
        self._root_window = tkinter.Tk()

        self._game_state = start_game()
        self._game_state.calc_score()

        self._score_text = tkinter.StringVar()
        self._score_text.set('Black: ' + str(self._game_state._count['Black']) + 2*'\t'
                      + 'White: ' + str(self._game_state._count['White']) + 2*'\t'
                      + 'Current turn: ' + self._game_state._turn)
        
        score_label = tkinter.Label(
            master = self._root_window, textvariable = self._score_text,
            font = DEFAULT_FONT)

        score_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self._game_state._columns * 50,
            height = self._game_state._rows * 50 + 216,
            background = 'green')
        
        self._canvas.grid(
            row = 1, column = 0, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._status_text = tkinter.StringVar()
        self._status_text.set('STATUS: ' + 'READY')

        self._status_label = tkinter.Label(
            master = self._root_window, textvariable = self._status_text,
            font = DEFAULT_FONT)

        self._status_label.grid(
            row = 2, column = 0, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._canvas.bind('<ButtonRelease-1>', self._on_canvas_released)

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        ''' Makes this window run forever until it is closed '''
        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        ''' Resizes every non-text entity on the board '''
        self._redraw_all_pieces()

    def _on_canvas_released(self, event: tkinter.Event) -> None:
        ''' Changes the status back to READY '''
        self._status_text.set('STATUS: ' + 'READY')

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        ''' If the cell where the user clicks into counts as a valid move,
        then it will update the game state's board status. '''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        box_width = canvas_width / self._game_state._columns
        box_height = canvas_height / self._game_state._rows

        col_index, row_index = self._detect_bounds((event.x, event.y))

        while True:
            
            message = self._game_state.make_move(col_index, row_index)
            if message != None:
                self._status_text.set('STATUS: ' + message)
            else:
                self._status_text.set('STATUS: ' + 'READY')
            if self._game_state.check_move():
                break
            else:
                message = self._game_state.determine_winner()
                self._redraw_all_pieces()
                self._score_text.set('Black: ' + str(self._game_state._count['Black']) + 2*'\t'
                      + 'White: ' + str(self._game_state._count['White']) + 2*'\t'
                      + 'Current turn: ' + self._game_state._turn)
                self._status_text.set('STATUS: ' + message)
                OthelloDialog.WinnerDialog(self._game_state).show()
                self._root_window.destroy()
                return
                
            
        self._redraw_all_pieces()
        self._score_text.set('Black: ' + str(self._game_state._count['Black']) + 2*'\t'
                      + 'White: ' + str(self._game_state._count['White']) + 2*'\t'
                      + 'Current turn: ' + self._game_state._turn)
        if not self._game_state.check_move():
            message = self._game_state.determine_winner()
            self._redraw_all_pieces()
            self._score_text.set('Black: ' + str(self._game_state._count['Black']) + 2*'\t'
                  + 'White: ' + str(self._game_state._count['White']) + 2*'\t'
                  + 'Current turn: ' + self._game_state._turn)
            self._status_text.set('STATUS: ' + message)
            OthelloDialog.WinnerDialog(self._game_state).show()
            self._root_window.destroy()
            return
                
    def _redraw_all_pieces(self) -> None:
        ''' Deletes and creates new entities of the column/row lines and the
        existing black and white discs corresponding to the new window size '''
        self._canvas.delete(tkinter.ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        box_width = canvas_width / self._game_state._columns
        box_height = canvas_height / self._game_state._rows

        radius_x = box_width*2/5
        radius_y = box_height*2/5     

        for col in range(self._game_state._columns):
            self._canvas.create_line(
                box_width * col, 0,
                box_width * col, canvas_height)

        for row in range(self._game_state._rows):
            self._canvas.create_line(
                0, box_height * row,
                canvas_width, box_height * row)

        for col in range(self._game_state._columns):
            for row in range(self._game_state._rows):
                if self._game_state._board[col][row] == OthelloGame.BLACK:
                    self._canvas.create_oval(
                    box_width*col+box_width/10, box_height*row+box_height/10,
                    box_width*(col+1)-box_width/10, box_height*(row+1)-box_height/10,
                    fill = '#000000', outline = '#FFFFFF')
                elif self._game_state._board[col][row] == OthelloGame.WHITE:
                    self._canvas.create_oval(
                    box_width*col+box_width/10, box_height*row+box_height/10,
                    box_width*(col+1)-box_width/10, box_height*(row+1)-box_height/10,
                    fill = '#FFFFFF', outline = '#000000')

    def _detect_bounds(self, coord: tuple) -> (int, int):
        ''' Returns the indices for the column and row respectively in which
        the user clicked into '''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        box_width = canvas_width / self._game_state._columns
        box_height = canvas_height / self._game_state._rows

        center_x, center_y =  coord
        
        for x in range(1, self._game_state._columns + 1):
            if center_x > box_width * x:
                continue
            else:
                for y in range(1, self._game_state._rows + 1):
                    if center_y > box_height * y:
                        continue
                    else:
                        return (x-1,y-1)         
    
def start_game() -> OthelloGame.Game:
    ''' Returns the game state set up by the input parameters for the game '''
    game_state = OthelloGame.Game()
    dialog = OthelloDialog.OptionDialog()
    dialog.show()
    game_state._columns = dialog._col
    game_state._rows = dialog._row
    game_state._turn = dialog._move
    game_state._topleft = dialog._top_left
    game_state._mode = dialog._winmode
    
    game_state.create_board()
    return game_state

        
if __name__ == '__main__':
    Board().start()
