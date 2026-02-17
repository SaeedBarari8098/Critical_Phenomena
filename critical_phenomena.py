import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid_size = 50              #size of lattice
threshold = 4               # threshold height parameter
delay = 0.001             # delay time in showing the frame of animation
grain_number = 35000        # amount of grain that we input in system
frames = grain_number + 50  # parameter for animation
time_steps = []             # just save time for avg height
input_type = "center"       # this show that where we input grain
# input_type = "random"


def topple_normal(grid_normal):                                      # this is normal sandpile's toppling
    topple_positions = np.where(grid_normal > threshold)
    while len(topple_positions[0]) > 0:
        for i, j in zip(topple_positions[0], topple_positions[1]):
            grid_normal[i, j] -= 4
            if i > 0:
                grid_normal[i - 1, j] += 1
            if i < grid_normal.shape[0] - 1:
                grid_normal[i + 1, j] += 1
            if j > 0:
                grid_normal[i, j - 1] += 1
            if j < grid_normal.shape[1] - 1:
                grid_normal[i, j + 1] += 1

        topple_positions = np.where(grid_normal > threshold)
    return grid_normal

def topple_mana(grid_mana):                                           # this is mana sandpile's toppling
    topple_positions = np.where(grid_mana > threshold)
    while len(topple_positions[0]) > 0:
        for i, j in zip(topple_positions[0], topple_positions[1]):
            grid_mana[i, j] -= 2
            for r in range(2):
                random_neighbor = np.random.randint(0, 4)
                if random_neighbor == 0:
                    if i - 1 >= 0:
                        grid_mana[i - 1][j] += 1
                if random_neighbor == 1:
                    if i + 1 <= grid_mana.shape[0] - 1:
                        grid_mana[i + 1][j] += 1
                if random_neighbor == 2:
                    if j - 1 >= 0:
                        grid_mana[i][j - 1] += 1
                if random_neighbor == 3:
                    if j + 1 <= grid_mana.shape[0] - 1:
                        grid_mana[i][j + 1] += 1
        topple_positions = np.where(grid_mana > threshold)
    return grid_mana


def calculate_average_height(grid):     # this function is just used for calculating height
    return np.mean(grid)


def run_normal(grain_number, grid_size):   # in this part I run the code with initial parameter
    avg_normal_heights = []
    avg_mana_heights = []
    animation_normal_grid = np.zeros((grain_number, grid_size, grid_size))
    animation_mana_grid = np.zeros((grain_number, grid_size, grid_size))
    grid_normal = np.zeros((grid_size, grid_size), dtype=int)
    grid_mana = np.zeros((grid_size, grid_size), dtype=int)

    for time in range(1, grain_number):
        if time % 2000 == 0: print(time)
        duration = 0
        size = 0
        x_n, x_m, y_n, y_m = [0, 0, 0, 0]
        if input_type == "center":
            x_n = x_m = y_n = y_m = (grid_size // 2)
        elif input_type == "random":
            x_n = np.random.randint(0, high=grid_size)  # random x to add normal sandpile grain
            y_n = np.random.randint(0, high=grid_size)  # random y to add normal sandpile grain
            x_m = np.random.randint(0, high=grid_size)  # random x to add mana sandpile grain
            y_m = np.random.randint(0, high=grid_size)  # random y to add mana sandpile grain

        grid_normal[x_n, y_n] += 1
        grid_normal = topple_normal(grid_normal)
        grid_mana[x_m, y_m] += 1
        grid_mana = topple_mana(grid_mana)

        time_steps.append(time)
        normal_height = calculate_average_height(grid_normal)
        avg_normal_heights.append(normal_height)

        mana_height = calculate_average_height(grid_mana)
        avg_mana_heights.append(mana_height)

        animation_normal_grid[time] = grid_normal
        animation_mana_grid[time] = grid_mana

    return (animation_normal_grid, animation_mana_grid, avg_normal_heights, avg_mana_heights)




grid_normal_list, grid_mana_list, avg_normal_h, avg_mana_h = run_normal(grain_number, grid_size)

# this part is for making plots that used in animation
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 7))
im_normal = ax1.imshow(grid_normal_list[0], interpolation='nearest', cmap='hot', vmin=0, vmax=threshold)
plt.colorbar(im_normal, label='Number of Grains')
ax1.set_title("Normal sandpile Grid")

avg_normal_height_line, = ax2.plot([], [], lw=2)
ax2.set_xlim(0, grain_number)
ax2.set_ylim(0, threshold)
ax2.set_title("Average Height Over Time")
ax2.set_ylabel("Average Height")

im_mana = ax3.imshow(grid_mana_list[0], interpolation='nearest', cmap='hot', vmin=0, vmax=threshold)
plt.colorbar(im_mana, label='Number of Grains')
ax3.set_title("Mana sandpile Grid")

avg_mana_height_line, = ax4.plot([], [], lw=2)
ax4.set_xlim(0, grain_number)
ax4.set_ylim(0, threshold)
ax4.set_xlabel("Time Step")
ax4.set_ylabel("Average Height")

def update(frame):         # this function is used for showing the evolution of plots
    im_normal.set_data(grid_normal_list[frame])
    im_mana.set_data(grid_mana_list[frame])
    avg_normal_height_line.set_data(time_steps[:frame], avg_normal_h[:frame])
    avg_mana_height_line.set_data(time_steps[:frame], avg_mana_h[:frame])
    return im_normal, im_mana, avg_normal_height_line, avg_mana_height_line


ani = animation.FuncAnimation(fig, update, frames=grain_number, interval=100, blit=True)

plt.tight_layout(pad=1, w_pad=5.0, h_pad=1)
plt.show()



# in this part I make a structure of results
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 7))
im_normal = ax1.imshow(grid_normal_list[0], interpolation='nearest', cmap='hot', vmin=0, vmax=threshold)
plt.colorbar(im_normal, label='Number of Grains')
ax1.set_title("Normal sandpile Grid")

avg_normal_height_line, = ax2.plot([], [], lw=2)
ax2.set_xlim(0, grain_number)
ax2.set_ylim(0, threshold)
ax2.set_title("Average Height Over Time")
ax2.set_ylabel("Average Height")

im_mana = ax3.imshow(grid_mana_list[0], interpolation='nearest', cmap='hot', vmin=0, vmax=threshold)
plt.colorbar(im_mana, label='Number of Grains')
ax3.set_title("Mana sandpile Grid")

avg_mana_height_line, = ax4.plot([], [], lw=2)
ax4.set_xlim(0, grain_number)
ax4.set_ylim(0, threshold)
ax4.set_xlabel("Time Step")
ax4.set_ylabel("Average Height")

im_normal.set_data(grid_normal_list[-1])
im_mana.set_data(grid_mana_list[-1])
avg_normal_height_line.set_data(time_steps, avg_normal_h)
avg_mana_height_line.set_data(time_steps, avg_mana_h)

plt.tight_layout(pad=1, w_pad=5.0, h_pad=1)
plt.show()
print("finish")


