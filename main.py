from model.level import Level
from model.level import Cell
from model.level import Colors

if __name__ == '__main__':
    level = Level()
    for row in range(5):
        for col in range(5):
            cell = Cell()
            cell.isActive = True
            level.set_cell(cell, row, col)
    green = Cell()
    green.isActive = True
    green.gamePiece = Colors.GREEN
    goal = Cell()
    goal.isActive = True
    goal.goal = Colors.GREEN
    level.set_cell(green, 2, 0)
    level.set_cell(goal, 2, 4)
    distance = Cell()
    distance.isActive = True
    level.set_cell(distance, 2, 15)
    level.message = "Hello world!"
    print(level.print_level_for_p8())
