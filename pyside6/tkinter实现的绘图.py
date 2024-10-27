import tkinter as tk
import numpy as np

class GridApp:
    def __init__(self, root, size=100):
        self.root = root
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.canvas = tk.Canvas(root, width=size * 5, height=size * 5)  # 每个格子大小为5x5像素
        self.canvas.pack()
        self.draw_grid()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)  # 添加单击事件

    def draw_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                x1, y1 = i * 5, j * 5
                x2, y2 = x1 + 5, y1 + 5
                color = 'white' if self.grid[i, j] == 0 else 'black'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def paint(self, event):
        x, y = event.x // 5, event.y // 5
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[x, y] = 1
            self.canvas.create_rectangle(x * 5, y * 5, (x + 1) * 5, (y + 1) * 5, fill='black', outline='')

    def export_grid(self):
        np.savetxt('grid_data.csv', self.grid, delimiter=',', fmt='%d')
        self.root.destroy()  # 关闭窗口

if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.title("画板 - 手写数字识别")
    root.protocol("WM_DELETE_WINDOW", app.export_grid)  # 关闭窗口时保存数据
    root.mainloop()