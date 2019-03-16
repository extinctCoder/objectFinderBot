# from img import module_img_ai

# if __name__ == "__main__":
#     module_img_ai("extinctCoder", 0, True)
import numpy as np
from maddux.objects import Obstacle, Ball
from maddux.environment import Environment
from maddux.robots import simple_human_arm

obstacles = [Obstacle([1, 2, 1], [2, 2.5, 1.5]), Obstacle([3, 2, 1], [4, 2.5, 1.5])]
ball = Ball([2.5, 2.5, 2.0], 0.25)

q0 = np.array([0, 0, 0, np.pi / 2, 0, 0, 0])
human_arm = simple_human_arm(2.0, 2.0, q0, np.array([3.0, 1.0, 0.0]))

env = Environment(dimensions=[10.0, 10.0, 20.0], dynamic_objects=[ball], static_objects=obstacles, robot=human_arm)

q_new = human_arm.ikine(ball.position)
human_arm.update_angles(q_new)
env.plot()
