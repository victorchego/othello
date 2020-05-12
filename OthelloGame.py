# Victor Chang

### VARIABLES

NONE = '+'
WHITE = 'WHITE'
BLACK = 'BLACK'

### CLASSES

class Game:
    #setup methods
    def __init__(self):
        ''' Initializes its attributes with default values '''
        self._board = []
        self._columns = 4
        self._rows = 4
        self._turn = BLACK
        self._topleft = WHITE
        self._mode = 'MOST'
        self._winner = None
        self._count = {'Black': 0, 'White': 0}
        self._empty = 0
        self._trigger = False
        
    def create_board(self) -> None:
        ''' Creates the board with the right dimensions and color scheme '''
        for col in range(self._columns):
            self._board.append([])
            for row in range(self._rows):
                self._board[-1].append(NONE)
        self._board = _center_disks(self._board, self._columns, self._rows, self._topleft)

    #continuous (game) methods
    def calc_score(self) -> None:
        ''' Calculates the score '''
        black_count = 0
        white_count = 0
        empty_count = 0
        for col in range(self._columns):
            for row in range(self._rows):
                if self._board[col][row] == BLACK:
                    black_count +=1
                if self._board[col][row] == WHITE:
                    white_count +=1
                if self._board[col][row] == NONE:
                    empty_count +=1
        self._count['Black'] = black_count
        self._count['White'] = white_count
        self._empty = empty_count

    def make_move(self, col_index: int, row_index: int) -> None or str:
        ''' Prompts the user to make a move '''
        try:
            check_empty(self._board, col_index, row_index)
            value = _check_directions(self._board, col_index, row_index, self._turn)
            if value:
                result = _get_directions(self._board, col_index, row_index, self._turn)
                for cases in range(result[0]): #number of possible moves
                    for direct in range(len(result[1])): #direction
                        for i in range(result[1][direct][2]+1): #length
                            self._board[col_index + result[1][direct][0]*i][row_index + result[1][direct][1]*i] = self._turn
                self._board[col_index + result[1][direct][0]][row_index + result[1][direct][1]] = self._turn
                self._turn = opposite_color(self._turn)
            else:
                return 'That is not a valid move'
        except:
            return 'That is not a valid move'
        finally:
            self.calc_score()

    def check_move(self) -> bool:
        ''' Checks if the next player is able to make a move.  If the player
        is unable to move, the turn goes back to the person who made the
        last move. Returns True unless both players are unable to make a move
        or no more moves exist.
        '''
        self.calc_score()
        if self._empty == 0 or self._count['Black'] == 0 or self._count['White'] == 0:
            return False
        for col in range(self._columns):
            for row in range(self._rows):
                if self._board[col][row] == NONE:
                    result = _get_directions(self._board, col, row, self._turn)[0]
                    if result == False:
                        continue
                    elif result >= 1:
                        self._trigger = False
                        return True
        if self._trigger == False:
            self._turn = opposite_color(self._turn)
            self._trigger = True
            return True
        else:
            return False
        
    def determine_winner(self) -> str:
        ''' Determines the winner based on the game mode '''
        if self._mode == 'MOST'  and self._count['Black'] != self._count['White']:
            self._winner = max(self._count, key = self._count.get)
            return 'END'
        elif self._mode == 'LEAST'  and self._count['Black'] != self._count['White']:
            self._winner = min(self._count, key = self._count.get)
            return 'END'
        else:
            self._winner = 'Tied'
            return 'END'

### OPEN FUNCTIONS

def check_empty(board: [[str]], col: int, row: int) -> None:
    ''' Checks if selected place is empty and passes '''
    if board[col][row] != NONE:
        raise MoveError()

def opposite_color(color: str) -> str:
    ''' Switches to the opposite color eg. black to white or white to black '''
    if color == BLACK:
        return WHITE
    elif color == WHITE:
        return BLACK
    elif color == NONE:
        return NONE

### HIDDEN FUNCTIONS

def _center_disks(board: [[str]], col: int, row: int, topleft: str) -> [list]:
    ''' Replaces the center disks with the properly colored disks '''
    mid_x = int(col/2)
    mid_y = int(row/2)
    board[mid_x-1][mid_y-1] = topleft #top left color
    board[mid_x][mid_y-1] = opposite_color(topleft) #top right color
    board[mid_x-1][mid_y] = opposite_color(topleft) #bottom left color
    board[mid_x][mid_y] = topleft #bottom right color
    return board

### LEGAL MOVES

def _check_legal(board: [[str]], col: int, row: int, coldelta: int, rowdelta: int, turn: str) -> bool or int:
    '''
    Returns an integer if a sequence of opposite colored pieces appears on
    the board, beginning in the given column and row, extending in a direction
    specified by the coldelta and rowdelta, and ending with its own color
    '''
    start_cell = board[col][row]
    detected = 0
    
    if start_cell == NONE:
        for i in range(16): #maximum possible value with functions that check limit
            if  _is_valid_column_number(col + coldelta * i, len(board)) \
                and  _is_valid_row_number(row + rowdelta * i, len(board[0])):
                    if i!=0 and board[col + coldelta*i][row + rowdelta*i] == NONE:
                        return False
                    if detected == 0 and turn == board[col + coldelta *i][row + rowdelta * i]:
                        return False
                    elif turn == opposite_color(board[col + coldelta *i][row + rowdelta * i]):
                        detected += 1
                        continue
                    elif detected != 0 and turn == board[col + coldelta *i][row + rowdelta * i]:
                        return detected

def _check_directions(board: [[str]], col: int, row: int, turn: str) -> bool:
    '''
    Returns an integer if a sequence of opposite colored pieces appears on the
    board, beginning in the given column and row, extending in any of the
    eight possible directions, and ending with its own color; returns False
    otherwise
    '''
    if _check_legal(board, col, row, 0, 1, turn) \
        or _check_legal(board, col, row, 1, 1, turn) \
        or _check_legal(board, col, row, 1, 0, turn) \
        or _check_legal(board, col, row, 1, -1, turn) \
        or _check_legal(board, col, row, 0, -1, turn) \
        or _check_legal(board, col, row, -1, -1, turn) \
        or _check_legal(board, col, row, -1, 0, turn) \
        or _check_legal(board, col, row, -1, 1, turn):
        return True
    else:
        return False

def _get_directions(board: [[str]], col: int, row: int, turn: str) -> [int]:
    '''
    Returns an integer list if a sequence of opposite colored pieces appears on the
    board, beginning in the given column and row, extending in any of the
    eight possible directions, and ending with its own color
    '''
    cases = 0
    case_list = []
    
    if _check_legal(board, col, row, 0, 1, turn):
        cases += 1
        case_list.append([0,1, _check_legal(board, col, row, 0, 1, turn)])
    if _check_legal(board, col, row, 1, 1, turn):
        cases += 1
        case_list.append([1,1, _check_legal(board, col, row, 1, 1, turn)])
    if _check_legal(board, col, row, 1, 0, turn):
        cases += 1
        case_list.append([1,0, _check_legal(board, col, row, 1, 0, turn)])
    if _check_legal(board, col, row, 1, -1, turn):
        cases += 1
        case_list.append([1,-1, _check_legal(board, col, row, 1, -1, turn)])
    if _check_legal(board, col, row, 0, -1, turn):
        cases += 1
        case_list.append([0,-1, _check_legal(board, col, row, 0, -1, turn)])
    if _check_legal(board, col, row, -1, -1, turn):
        cases += 1
        case_list.append([-1,-1, _check_legal(board, col, row, -1, -1, turn)])
    if _check_legal(board, col, row, -1, 0, turn):
        cases += 1
        case_list.append([-1,0, _check_legal(board, col, row, -1, 0, turn)])
    if _check_legal(board, col, row, -1, 1, turn):
        cases += 1
        case_list.append([-1,1, _check_legal(board, col, row, -1, 1, turn)])

    return (cases, case_list) # case_list is [col index, row index, function val]

def _is_valid_column_number(col: int, board_col: int) -> bool:
    '''Returns True if the given column number is valid; returns False otherwise'''
    return 0 <= col < board_col

def _is_valid_row_number(row: int, board_row: int) -> bool:
    '''Returns True if the given row number is valid; returns False otherwise'''
    return 0 <= row < board_row
