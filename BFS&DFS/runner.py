from maze import Maze
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python runner.py small_maze.txt")

filename = sys.argv[1]
m = Maze(filename)
print(f"Solving {filename}...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("output.png", show_solution=True, show_explored=True)
print("Image saved as output.png!")