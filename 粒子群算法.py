import numpy as np
import matplotlib.pyplot as plt

# 问题参数
num_particles = 20
num_dimensions = 2
num_iterations = 100
c1 = 2.0
c2 = 2.0
w = 0.7

# 生成随机位置的粒子群
particles_position = np.random.rand(num_particles, num_dimensions) * 100

# 初始化速度
particles_velocity = np.zeros((num_particles, num_dimensions))

# 计算适应度函数（这里用一个简单的距离函数）
def fitness(position):
    # 这里可以根据实际情况修改适应度函数
    target_location = np.array([50, 50])  # 目标位置
    return np.linalg.norm(position - target_location)

# 初始化个体最佳位置和全局最佳位置
personal_best = particles_position.copy()
global_best_index = np.argmin([fitness(p) for p in particles_position])
global_best = particles_position[global_best_index].copy()

# 保存每次迭代的全局最佳适应度值
global_best_fitness = []

# 开始迭代
for iteration in range(num_iterations):
    for i in range(num_particles):
        # 更新速度和位置
        r1, r2 = np.random.rand(), np.random.rand()
        particles_velocity[i] = w * particles_velocity[i] + c1 * r1 * (personal_best[i] - particles_position[i]) + c2 * r2 * (global_best - particles_position[i])
        particles_position[i] = particles_position[i] + particles_velocity[i]

        # 更新个体最佳位置
        if fitness(particles_position[i]) < fitness(personal_best[i]):
            personal_best[i] = particles_position[i]

            # 更新全局最佳位置
            if fitness(personal_best[i]) < fitness(global_best):
                global_best = personal_best[i]
    
    global_best_fitness.append(fitness(global_best))

# 打印结果
print("最优位置:", global_best)
print("最优适应度值:", fitness(global_best))

# 绘制图表
plt.plot(global_best_fitness)
plt.title('粒子群算法收敛过程')
plt.xlabel('迭代次数')
plt.ylabel('最优适应度值')
plt.show()