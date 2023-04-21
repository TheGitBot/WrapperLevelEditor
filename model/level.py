class Cell:
    def __init__(self):
        self.isActive = False
        self.goal = None
        self.gamePiece = None

    def get_p8_mapping(self) -> int:
        """
        mappings:
        -1 -> out of bounds
        0  -> empty space
        1  -> green piece
        2  -> green goal
        4  -> red piece
        8  -> red goal
        """
        if not self.isActive: return -1
        mapping = 0
        if self.goal == 'green': mapping += 2
        elif self.goal == 'red': mapping += 8
        elif self.goal == 'wild': mapping += 10
        if self.gamePiece == 'green': mapping += 1
        elif self.gamePiece == 'red': mapping += 4
        elif self.gamePiece == 'wild': mapping += 5
        return mapping


class Level:
    __height = 16
    __width = 16

    def __init__(self):
        self.__map = [[Cell() for j in range(Level.__height)] for i in range(Level.__width)]
        self.message = ""

    def get_cell(self, row: int, column: int) -> Cell:
        return self.__map[row][column]

    def set_cell(self, cell: Cell, row: int, column: int) -> None:
        if len(self.__map) <= row or row < 0:
            return

        if len(self.__map[row]) <= column or column < 0:
            return

        if not cell.isActive:
            self.__map[row][column] = Cell()
            return

        self.__map[row][column] = cell

    def get_bounds(self) -> ((int, int), (int, int)):
        first_row = None
        first_col = None
        last_row = None
        last_col = None
        for row in range(Level.__height):
            for col in range(Level.__width):
                if self.__map[row][col].isActive:
                    first_row = row
                    break
            if first_row is not None:
                break
        if first_row is None: return None
        for col in range(Level.__width):
            for row in range(first_row, Level.__height):
                if self.__map[row][col].isActive:
                    first_col = col
                    break
            if first_col is not None:
                break
        if first_col is None: return None
        for row in reversed(range(first_row, Level.__height)):
            for col in range(first_col, Level.__width):
                if self.__map[row][col].isActive:
                    last_row = row
                    break
            if last_row is not None:
                break
        if last_row is None: return None
        for col in reversed(range(first_col, Level.__width)):
            for row in range(first_row, last_row):
                if self.__map[row][col].isActive:
                    last_col = col
                    break
            if last_col is not None:
                break
        if last_col is None: return None
        return (first_row, first_col), (last_row, last_col)

    def print_level_for_p8(self) -> str:
        bounds = self.get_bounds()
        out_string = ""
        out_string += " {\n"
        for row in range(bounds[0][0], bounds[1][0]+1):
            out_string += "  {"
            for col in range(bounds[0][1], bounds[1][1]+1):
                cell = self.__map[row][col]
                out_string += str(cell.get_p8_mapping())
                if col != bounds[1][1]:
                    out_string += ","
            out_string += "}"
            if row != bounds[1][0]:
                out_string += ","
            out_string += "\n"
        if len(self.message) > 0:
            out_string += "  message = \"" + self.message + "\""
        out_string += "\n }"
        return out_string
