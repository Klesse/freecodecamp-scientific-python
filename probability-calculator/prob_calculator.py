import random
from collections import Counter
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number > len(self.contents):
      copy_contents = self.contents.copy()
      self.contents = []
      return copy_contents
    balls_i = []
    balls_v = []
    while len(balls_i) < number:
      ball_index = random.randint(0, len(self.contents) - 1)
      if ball_index not in balls_i:
        balls_i.append(ball_index)
        balls_v.append(self.contents[ball_index])
    balls_removed = []
    for i in balls_i:
      balls_removed.append(self.contents[i])
    for i in balls_v:
      self.contents.remove(i)
    return balls_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  N = num_experiments
  balls = []
  for key, value in expected_balls.items():
    for i in range(value):
      balls.append(key)

  for i in range(num_experiments):
    balls_removed = hat.draw(num_balls_drawn)
    for ball in balls_removed:
      hat.contents.append(ball)

    c = list((Counter(balls_removed) & Counter(balls)).elements())
    if sorted(c) == sorted(balls):
      M += 1
  return M / N
