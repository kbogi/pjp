from operator import itemgetter
import itertools
import operator


def calc_neighbors(r, c):
    neighbors = set()
    for i in range(9):
        neighbors.add(r * 9 + i)
        neighbors.add(i * 9 + c)
        neighbors.add((r - (r % 3) + int(i / 3)) * 9 + (c - (c % 3) + i % 3))
    return tuple(neighbors)


def prepare_neighbors():
    neighbors = []
    for c in range(9):
        for r in range(9):
            neighbors.append(calc_neighbors(c, r))
    return tuple(neighbors)


FILLED = -1
STACK_EMPTY = -1
NEIGHBORS = prepare_neighbors()


class Sudoku:
    # prepare neighbors
    neighbors = NEIGHBORS

    def __init__(self):
        self.solutions = 0
        self.lastSolution = None
        self.data = None
        self.empty = set()
        self.stack = []
        self.colors = [-1] * (9 * 9)

    def set_data(self, data):
        self.data = data

    def read_sudoku(self):
        solutions = 0
        sudoku = []
        for i in range(9):
            raw_line = input()
            raw_array = raw_line.split(' ')
            for n in raw_array:
                if (n != ''):
                    sudoku.append(int(n))
        self.data = sudoku

    def print_sudoku(self):
        for r in range(9):
            raw_row = ''
            for c in range(9):
                raw_row += str(self.data[r * 9 + c]) + ' '
            print(raw_row)

    def set(self, last, col):
        self.data[last] = col
        self.empty.remove(last)

    def clear_last(self, last):
        colors = self.colors
        self.data[last] = 0
        self.empty.add(last)
        colors[last] = -1
        for neigh in NEIGHBORS[last]:
            colors[neigh] = -1

    def save_solution(self):
        self.lastSolution = Sudoku()
        self.lastSolution.set_data(tuple(self.data))
        self.solutions += 1

    def get_min_color(self, coords, col):
        colors = self.colors
        while True:
            if colors[coords] & (1 << col) == 0:
                return col
            col += 1

    def get_saturation(self, i):
        cols = self.colors
        if cols[i] == -1:
            colors = 0
            count = 0
            data = self.data
            for neigh in NEIGHBORS[i]:
                old = colors
                colors |= 1 << data[neigh]
                if old != colors:
                    count += 1
            nc = count << 10
            cols[i] = colors | nc
            return (count, i)
        else:
            return (cols[i] >> 10, i)

    def clearColor(self):
        self.colors = -1

    def fill_next(self, start_color):
        def get_next_empty_satur(self):
            i_max = -1
            val_max = -1
            for sat in map(get_saturation, self.empty):
                if sat[0] > val_max:
                    i_max = sat[1]
                    val_max = sat[0]
            return i_max

        cols = self.colors
        data = self.data

        def get_saturation(i):
            nonlocal cols
            if cols[i] == -1:
                colors = 0
                count = 0
                nonlocal data
                for neigh in NEIGHBORS[i]:
                    old = colors
                    colors |= 1 << data[neigh]
                    if old != colors:
                        count += 1
                nc = count << 10
                cols[i] = colors | nc
                return count
            else:
                return cols[i] >> 10

        i_max = -1
        val_max = -1
        for i in self.empty:
            sat = get_saturation(i)
            if sat > val_max or sat == 9:
                i_max = i
                val_max = sat
        next = i_max
        if next == FILLED:
            self.save_solution()
            return False
        col = start_color
        while True:
            if cols[next] & (1 << col) == 0:
                break
            col += 1
        if col > 9:
            return False
        self.set(next, col)
        self.stack.append((next, col))
        cols[next] = -1
        for neigh in NEIGHBORS[next]:
            cols[neigh] = -1
        return True

    def revert(self):
        if len(self.stack) > 0:
            last = self.stack.pop()
            self.clear_last(last[0])
            return last[1]
        return STACK_EMPTY

    def fill_sudoku(self):
        fill_next = self.fill_next
        revert = self.revert
        color = 0
        for i in range(9 * 9):
            if self.data[i] == 0:
                self.empty.add(i)
        while True:
            if fill_next(color):
                color = 0
            else:
                revert_result = revert()
                if revert_result != STACK_EMPTY:
                    color = revert_result + 1
                else:
                    break
        print(self.solutions)
        if self.solutions == 1:
            self.lastSolution.print_sudoku()


if __name__ == '__main__':
    repeats = int(input())
    for repeat in range(repeats):
        sudoku = Sudoku()
        sudoku.read_sudoku()
        sudoku.fill_sudoku()
        if (repeat + 1 < repeats):
            input()
