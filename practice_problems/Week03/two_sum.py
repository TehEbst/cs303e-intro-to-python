import matplotlib.pyplot as plt
from random import randint

class Solution:


    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        limit = len(self.nums)
        lb = [0]
        ub = [limit - 1]
        lb_dir = 1
        ub_dir = 1
        sum = []
        for i in range(10):
            print()
            print(f'loop {i+1}')
            print(f'lb: {lb[-1]}, value: {self.nums[lb[-1]]}')
            print(f'ub: {ub[-1]}, value: {self.nums[ub[-1]]}')

            sum.append(self.nums[lb[-1]] + self.nums[ub[-1]])

            if sum[-1] == self.target and lb[-1] != ub[-1]:
                break

            if lb[-1] == 0:
                lb_dir = 1
            elif lb[-1] == limit - 1:
                lb_dir = -1

            if ub[-1] == 0:
                ub_dir = 1
            elif ub[-1] == limit - 1:
                ub_dir = -1

            if abs(self.nums[lb[-1]]) > self.target:
                lb.append(lb[-1] + lb_dir)
                ub.append(ub[-1])
                print('move lb by 1')
                print(f'lb: {lb[-1]}, value: {self.nums[lb[-1]]}')
                print(f'ub: {ub[-1]}, value: {self.nums[ub[-1]]}')
            elif abs(self.nums[lb[-1]] + self.nums[ub[-1]]) > abs(self.target):
                ub.append(ub[-1] + ub_dir)
                lb.append(lb[-1])
                print('move ub by 1')
                print(f'lb: {lb[-1]}, value: {self.nums[lb[-1]]}')
                print(f'ub: {ub[-1]}, value: {self.nums[ub[-1]]}')
            elif abs(self.nums[lb[-1]] + self.nums[ub[-1]]) < abs(self.target):
                lb.append(lb[-1] + lb_dir)
                ub.append(ub[-1])
                print('move lb by 1')
                print(f'lb: {lb[-1]}, value: {self.nums[lb[-1]]}')
                print(f'ub: {ub[-1]}, value: {self.nums[ub[-1]]}')

        if not self.nums[lb[-1]] < self.nums[ub[-1]]:
            print('flip')
            temp = lb[-1]
            lb.append(ub[-1])
            ub.append(temp)
            print(f'lb: {lb[-1]}, value: {self.nums[lb[-1]]}')
            print(f'ub: {ub[-1]}, value: {self.nums[ub[-1]]}')

        return lb, ub, sum

vector = [150,24,79,50,88,345,3]
targ = 200

sol = Solution(nums=vector, target=targ)

x_lb, x_ub, x_sum = (sol.twoSum())
print(x_lb)
print(x_ub)

plt.plot(x_ub)
plt.plot(x_lb)
plt.plot(x_sum)
plt.show()

