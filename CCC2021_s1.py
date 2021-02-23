# Justin G. Fr. Micheal Goetz CSS
# 2/17/2021
# Problem S1: Crazy Fencing

def calc_area(b1, b2, h):
  area = ((b1 + b2) / 2 ) * h

  return area

fence_num = int(input())
fence_h = input().split()
fence_w = input().split()
total_area = 0.0 

for i in range(fence_num):
  total_area += calc_area(int(fence_h[i]), int(fence_h[i + 1]), int(fence_w[i]))

print(total_area)
 
