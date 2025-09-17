class Solution:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        my_dict = {}
        ind = 0
        my_answer = []
        for num in self.nums:
            if num in my_dict:
                my_dict[num].append(ind)
            else:
                my_dict[num] = [ind]

            if self.target - num in my_dict and my_dict[num] != my_dict[self.target - num]:
                my_answer.append(my_dict[num][0])
                my_answer.append(my_dict[self.target - num][0])

            ind += 1

        if self.target % 2 == 0 and len(my_answer ) == 0:
            my_answer = my_dict[self.target / 2]
        return sorted(my_answer)


my_input = [3, 3]
my_target = 6

my_Solution = Solution(my_input, my_target)

print( my_Solution.twoSum() )