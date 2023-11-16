import numpy as np
import matplotlib.pyplot as plt

# 问题参数
num_centers = 3  # 配送中心数量
initial_temperature = 100.0
cooling_rate = 0.95
num_iterations = 1000  # 增加到1000次

# 生成随机初始位置
current_positions = np.random.rand(num_centers, 2) * 100

# 计算初始适应度
current_fitness = np.sum(np.linalg.norm(current_positions - np.array([50, 50]), axis=1))

# 初始化最佳位置和最佳适应度
best_positions = current_positions.copy()
best_fitness = current_fitness

# 保存每次迭代的最佳适应度值
best_fitness_values = []

# 保存每次迭代的选址变化
positions_history = []

# 模拟退火算法主循环
for iteration in range(num_iterations):
    # 生成新的候选位置
    candidate_positions = current_positions + np.random.randn(num_centers, 2) * 5

    # 计算候选位置的适应度
    candidate_fitness = np.sum(np.linalg.norm(candidate_positions - np.array([50, 50]), axis=1))

    # 判断是否接受候选位置
    if candidate_fitness < current_fitness or np.random.rand() < np.exp((current_fitness - candidate_fitness) / initial_temperature):
        current_positions = candidate_positions
        current_fitness = candidate_fitness

    # 更新最佳位置和适应度
    if current_fitness < best_fitness:
        best_positions = current_positions
        best_fitness = current_fitness

    # 降低温度
    initial_temperature *= cooling_rate

    # 保存每次迭代的最佳适应度值
    best_fitness_values.append(best_fitness)

    # 保存每次迭代的选址变化
    positions_history.append(current_positions.copy())

# 打印结果
print("最优位置:", best_positions)
print("最优适应度值:", best_fitness)

# 绘制图表
plt.figure(figsize=(12, 5))

# 绘制最佳适应度值变化图
plt.subplot(1, 2, 1)
plt.plot(best_fitness_values)
plt.title('模拟退火算法收敛过程')
plt.xlabel('迭代次数')
plt.ylabel('最优适应度值')

# 绘制选址变化图
plt.subplot(1, 2, 2)
positions_history = np.array(positions_history)
for i in range(num_centers):
    plt.plot(positions_history[:, i, 0], positions_history[:, i, 1], label=f'Center {i+1}', marker='o')
plt.scatter(best_positions[:, 0], best_positions[:, 1], color='red', label='Best Centers', marker='x')
plt.title('选址变化图')
plt.xlabel('X坐标')
plt.ylabel('Y坐标')
plt.legend()

# 在选址变化图中标注最佳位置
for i in range(num_centers):
    plt.annotate(f'Center {i+1} Best', (best_positions[i, 0], best_positions[i, 1]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()