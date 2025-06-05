import numpy as np
import matplotlib.pyplot as plt

def generate_map(rows, cols, obstacle_prob):
    """生成带有随机障碍物的地图"""
    grid = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if np.random.rand() < obstacle_prob:
                grid[i][j] = 1
    # 确保起点和终点无障碍
    grid[0][0] = 0
    grid[-1][-1] = 0
    return grid

def plan_s_path(grid):
    """S形路径规划算法"""
    rows, cols = grid.shape
    path = []
    visited = set()
    direction = 1  # 初始方向向右
    
    for i in range(rows):
        # 确定当前行遍历方向
        if i % 2 == 0:
            col_range = range(cols)
        else:
            col_range = reversed(range(cols))
        
        for j in col_range:
            if grid[i][j] == 0 and (i, j) not in visited:
                # 添加当前点到路径
                path.append((i, j))
                visited.add((i, j))
                
                # 尝试直线移动直到遇到障碍
                while True:
                    next_j = j + direction
                    if 0 <= next_j < cols and grid[i][next_j] == 0 and (i, next_j) not in visited:
                        j = next_j
                        path.append((i, j))
                        visited.add((i, j))
                    else:
                        break
        direction *= -1  # 换行时改变方向
    
    return path

def plot_map_and_path(grid, path):
    """可视化地图和路径"""
    rows, cols = grid.shape
    plt.figure(figsize=(cols, rows))
    
    # 绘制网格和障碍物
    for i in range(rows):
        for j in range(cols):
            color = 'black' if grid[i][j] == 1 else 'white'
            plt.fill_between([j-0.5, j+0.5], i-0.5, i+0.5, color=color, edgecolor='gray')
    
    # 绘制路径
    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, 'r-', marker='o', markersize=8, linewidth=2)
    
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.gca().invert_yaxis()  # 原点在左上角
    plt.grid(True)
    plt.show()

# 参数设置
rows, cols = 20, 20
obstacle_prob = 0.05

# 生成地图
grid = generate_map(rows, cols, obstacle_prob)

# 生成路径
path = plan_s_path(grid)

# 可视化
plot_map_and_path(grid, path)