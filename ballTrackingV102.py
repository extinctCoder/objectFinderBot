import numpy as np
from maddux.environment import Environment
from maddux.objects import Ball, Target

ball = Ball([2, 0, 2], 0.25)
target = Target([2, 10, 2], 0.5)
environment = Environment(dynamic_objects=[ball], static_objects=[target])

release_velocity = np.array([0, 15, 5])
ball.throw(release_velocity)

# Either run environment for n seconds
environment.run(2.0)
# And plot the result
environment.plot()

# Or, you can animate it while running
environment.animate(2.0)
