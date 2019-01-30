import numpy as np
import matplotlib.pyplot as plt


class DrawTools:
    def __init__(self):
        pass
    def draw_line_with_points(self, X, y):
        """
        X [1, 2, 3]
        y [1, 2, 3]
        """
        # plot函数作图
        plt.plot(X, y)

        # show函数展示出这个图，如果没有这行代码，则程序完成绘图，但看不到
        plt.show()

    def draw_line_with_func(self, func, step=0.1, x_range=(1, 50)):
        """
        func 是函数表达式
        range 是自变量的范围
        """
        _min, _max = x_range
        X = np.arange(_min, _max, step)
        y = []
        for i in X:
            y.append(func(i))
        
        self.draw_line_with_points(X, y)
        

def main():
    dt = DrawTools()
    # X = [1, 2, 3]
    # y = [1, 2, 3]
    # dt.draw_line_with_points(X, y)
    def func(x):
        y = x**700 * (1-x)**300 
        return y
    dt.draw_line_with_func(func, step=0.01, x_range=(0, 1))

if __name__ == "__main__":
    main()
