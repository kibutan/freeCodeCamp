import copy
import random
# Consider using the modules imported above.

class Hat:
  # def __init__(self,red=0,brue=0,green=0,orange=0,pink=0,striped=0):
  def __init__(self,**kwargs):
    self.contents = []
    self.draw_list=[]

    # self.contents = *kwargs
    for i in kwargs:
      for j in range(kwargs[i]):
        self.contents.append(i)
    # print("i",self.contents)
    pass

  def draw(self,num):
    if num >= len(self.contents):self.draw_list = self.contents
    else:
      for i in range(0, num):
        # print(num,len(self.contents),i )
        index = random.randrange(0,len(self.contents))
        draw_ball = self.contents.pop(index)
        self.draw_list.append(draw_ball)
    return self.draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  probability = 0
  copy_hat = [0]*num_experiments
  cnt = 0
  for i in range(num_experiments):
    copy_hat[i] = copy.deepcopy(hat)
    copy_hat[i].draw(num_balls_drawn)
    # print("copy_hat.draw-------------------",copy_hat[i].draw_list)
    for j in expected_balls:
      # print(expected_balls)
      # print("attempt",copy_hat[i].draw_list.count(j))
      # print("border",j,expected_balls[j])
    # for j in expected_balls:
      if copy_hat[i].draw_list.count(j) < expected_balls[j]:break
    else:cnt += 1
  print("cnt",cnt)
  probability = cnt/num_experiments
      
  return probability
