"""
This file contains general use functions for all exercises.
"""
from copy import copy
import heapq
import inspect
import os
import re
import numpy as np
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.widgets


def read(split='\n', ints=False):
    """Returns a list containing one string for each line of the day's input file. Optionally calls int()."""
    day = re.findall(r'\d+', inspect.stack()[1].filename)[-1]  # Last number in the filename of the caller
    with open(f"Input/input{day}.txt") as f:
        strings = f.read().strip().split(split)
    if ints:
        return [int(n) for n in strings]
    else:
        return strings


def clip(text):
    """Outputs text to the system clipboard as a string."""
    string = str(text)
    with os.popen('xclip -selection c', 'w') as out:
        out.write(string)


def neighbours(x: int, y: int, grid: np.ndarray):
    """Yields all neighbours of a point in a 2D NumPy array."""
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) != (0, 0):
                yield grid[x + dx, y + dy]


def repeat(f, x, n: int):
    """Applies f to x successively n times."""
    for i in range(n):
        x = f(x)
    return x


def a_star(start, target, h, neighbours, equal_weights=True, **kwargs):
    """Generic A* pathfinding algorithm. Does not return a path, only the discovered path length.

    A binary heap (heapq) is used for the priority queue. f(n) = g(n) + h(n) is prioritised as always.
    In case of a tie, the node with the lowest heuristic h(n) is prioritised. Further ties are handled
    in reverse insertion order (Last In, First Out).

    Different algorithms are used for graphs with unit weights and diverse weights; the former is
    faster, but it breaks for certain inadmissible heuristics. 

    Nodes are stored in sets, so they must be hashable.

    Args:
        start: The starting node.
        target: The target node.
        h: A function that returns the heuristic h(n) of a given node. Takes two arguments: (node, target)
        neighbours: A single-argument function that takes the current node and yields each neighbouring node.
            If the graph weights are not equal, it must also yield the cost in a tuple: (neighbour, cost)
            Any additional keyword arguments are passed to this function.
        equal_weights (optional): True if all weights are equal (default), False otherwise. Must be set to
            False for non-admissible heuristics to prevent breakage.

    Returns:
        The length of the discovered path.
    """
    print("Working...\r", end='')

    guess = h(start, target)  # Best guess for the shortest path length
    entry_id = 0

    # Priority queue: f(n) is prioritised, with ties broken first by h(n), then by last inserted.
    queue = [(guess, guess, entry_id, start, 0)]  # (f(n), h(n), entry, node, g(n))

    if equal_weights:  # Faster, more breakable algorithm
        visited = {start}

        while queue:
            _f, _h, _id, node, g = heapq.heappop(queue)
            for neigh in neighbours(node, **kwargs):
                if neigh == target:  # Return straight away when we touch the target node
                    return g + 1
                if neigh not in visited:
                    entry_id -= 1  # Negative to ensure LIFO
                    g_n = g + 1
                    h_n = h(neigh, target)
                    f_n = g_n + h_n  # Total path cost
                    heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))
                    visited.add(neigh)  # We mark the neighbours as visited to prevent duplicates

    else:  # Slower, more resilient algorithm
        visited = set()

        while queue:
            _f, _h, _id, node, g = heapq.heappop(queue)
            if node == target:  # Only return once the target node is current
                return g
            if node not in visited:
                visited.add(node)  # Without an admissible h(n) we have to mark the current node as visited
                for neigh, cost in neighbours(node, **kwargs):
                    if neigh not in visited:
                        entry_id -= 1  # Negative to ensure LIFO
                        g_n = g + cost
                        h_n = h(neigh, target)
                        f_n = g_n + h_n  # Total path cost
                        heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def orientations(tile: np.ndarray):
    """Yields all different orientations of a 2D NumPy array."""
    for direction in (1, -1):  # Tile is not flipped/flipped
        for rotation in range(4):  # CCW quarter turns
            yield np.rot90(tile, k=rotation)[:, ::direction]


class Player(FuncAnimation):
    """Matplotlib video player, adapted from code courtesy of Elan Ernest."""
    def __init__(self, fig, func, frames=None, start=0, init_func=None, fargs=None,
                 save_count=None, pos=(0.125, 0.92), **kwargs):
        self.min = 0
        self.scale = 1
        if isinstance(frames, int):
            self.max = frames - 1
        elif isinstance(frames, range):
            self.min = frames.start
            self.max = frames.stop - 1
            self.scale = frames.step
        else:
            self.max = 100
        self.i = start if self.min <= start <= self.max else self.min
        self.step = self.scale
        self.fig = fig
        self.func = func
        self.artists = self.func(self.i)
        self.setup(pos)
        FuncAnimation.__init__(self, self.fig, self.update, frames=self.play(),
                               init_func=init_func, fargs=fargs,
                               save_count=save_count, **kwargs)

    def play(self):
        while self.step:
            self.i += self.step
            if self.i < self.min:
                self.i = self.max
            elif self.i > self.max:
                self.i = self.min
            yield self.i

    def start(self):
        if not self.step:
            self.event_source.start()

    def stop(self, event=None):
        if self.step:
            self.step = 0
            self.event_source.stop()

    def forward(self, event=None):
        if self.step > self.scale:
            self.step //= 2
        else:
            self.start()
            self.step = self.scale

    def backward(self, event=None):
        if self.step < -self.scale:
            self.step //= 2
        else:
            self.start()
            self.step = -self.scale

    def fastforward(self, event=None):
        if self.step > 0:
            self.step *= 2
        else:
            self.start()
            self.step = 2 * self.scale

    def fastback(self, event=None):
        if self.step < 0:
            self.step *= 2
        else:
            self.start()
            self.step = -2 * self.scale

    def oneforward(self, event=None):
        if self.i < self.max:
            self.i += self.scale
        self.onestep()

    def onebackward(self, event=None):
        if self.i > self.min:
            self.i -= self.scale
        self.onestep()

    def onestep(self):
        self.stop()
        self.func(self.i)
        self.slider.set_val(self.i)
        self.fig.canvas.draw_idle()

    def setup(self, pos):
        playerax = self.fig.add_axes([pos[0], pos[1], 0.64, 0.04])
        divider = mpl_toolkits.axes_grid1.make_axes_locatable(playerax)
        fbax = divider.append_axes("right", size="80%", pad=0.03)
        bax = divider.append_axes("right", size="80%", pad=0.03)
        sax = divider.append_axes("right", size="80%", pad=0.03)
        fax = divider.append_axes("right", size="80%", pad=0.03)
        ffax = divider.append_axes("right", size="80%", pad=0.03)
        ofax = divider.append_axes("right", size="100%", pad=0.03)
        sliderax = divider.append_axes("right", size="400%", pad=0.05)
        self.button_oneback = matplotlib.widgets.Button(playerax, label='$\u29CF$')
        self.button_fastback = matplotlib.widgets.Button(fbax, label='$\u25C2\u25C2$')
        self.button_back = matplotlib.widgets.Button(bax, label='$\u25C0$')
        self.button_stop = matplotlib.widgets.Button(sax, label='$\u25A0$')
        self.button_forward = matplotlib.widgets.Button(fax, label='$\u25B6$')
        self.button_fastforward = matplotlib.widgets.Button(ffax, label='$\u25B8\u25B8$')
        self.button_oneforward = matplotlib.widgets.Button(ofax, label='$\u29D0$')
        self.button_oneback.on_clicked(self.onebackward)
        self.button_fastback.on_clicked(self.fastback)
        self.button_back.on_clicked(self.backward)
        self.button_stop.on_clicked(self.stop)
        self.button_forward.on_clicked(self.forward)
        self.button_fastforward.on_clicked(self.fastforward)
        self.button_oneforward.on_clicked(self.oneforward)
        self.slider = matplotlib.widgets.Slider(sliderax, '',
                                                self.min, self.max, valinit=self.i)
        self.slider.on_changed(self.set_pos)

    def set_pos(self, i):
        self.i = int(self.slider.val)
        self.artists = self.func(self.i)

    def update(self, i):
        self.slider.set_val(i)
        return self.artists


class IntCodeCPU:
    """Computer that executes IntCode. References dictionaries for operatons and parameter modes."""
    def __init__(self):
        self.opcode_dict = {  # For each opcode: (instruction pointer jump, operation)
            1: lambda op: self.write(next(op) + next(op)),  # Add
            2: lambda op: self.write(next(op) * next(op)),  # Multiply
            3: lambda op: self.write(self.input),  # Input
            4: lambda op: self.output.append(next(op)),  # Output
            5: lambda op: self.jump(next(op)) if next(op) else next(op),  # Jump if true
            6: lambda op: next(op) if next(op) else self.jump(next(op)),  # Jump if false
            7: lambda op: self.write(1 if next(op) < next(op) else 0),  # Less than
            8: lambda op: self.write(1 if next(op) == next(op) else 0),  # Equals
            99: lambda _op: self.halt()  # Halt
        }

        self.mode_dict = {  # Parameter modes
            0: lambda i: self.code[i],
            1: lambda i: i
        }

        self.code = self.input = None
        self.output = []
        self.pointer = 0
        self.running = False

    def execute(self, intcode, user_input=None):
        """Main wrapper for execution of the IntCode."""
        if isinstance(intcode, str):
            self.code = [int(n) for n in intcode.split(',')]
        else:
            self.code = copy(intcode)
        self.input = user_input
        self.output = []
        self.pointer = 0
        self.running = True
        while self.running:
            value = self.code[self.pointer]
            modes, opcode = divmod(value, 100)  # Separate the opcode from the operation modes
            operate = self.opcode_dict[opcode]
            operate(self.operands(modes))
            self.pointer += 1
        return self.output

    def operands(self, modes):
        """Yields the values that the instructions operate on, using the correct modes."""
        while True:
            self.pointer += 1
            modes, mode = divmod(modes, 10)
            yield self.mode_dict[mode](self.code[self.pointer])

    def write(self, val):
        """Writes val to the position given in the last parameter."""
        self.pointer += 1
        self.code[self.code[self.pointer]] = val

    def jump(self, val):
        """Used by jump instructions"""
        self.pointer = val - 1

    def halt(self):
        self.running = False
