import numpy as np
from maddux.robots.predefined_robots import simple_human_arm
from maddux.objects import Ball, Target, Obstacle
from maddux.environment import Environment

# Create an arm with a specific config and base position
q0 = np.array([0.5, 0.2, 0, 0.5, 0, 0, 0])
base_pos = np.array([2.0, 2.0, 0.0])

# And link segments of length 2.0
arm = simple_human_arm(2.0, 2.0, q0, base_pos)

# We then create a ball, target, and obstacle
ball = Ball(position=[2.0, 0.0, 2.0], radius=0.15)
target = Target(position=[5.0, 8.0, 2.0], radius=0.5)
obstacle = Obstacle([4, 4, 0], [5, 5, 2])

# And use these to create an environment with dimensions 10x10x10
env = Environment(dimensions=[10, 10, 10],
                  dynamic_objects=[ball],
                  static_objects=[obstacle, target],
                  robot=arm)

env.animate(2.0)
