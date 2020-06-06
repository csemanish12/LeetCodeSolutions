import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weight = w
        self.sum_of_weight = sum(self.weight)
        self.weight_proportions = [self.weight[0]]
        for i in range(1, len(self.weight)):
            self.weight_proportions.append(self.weight_proportions[i - 1] + self.weight[i])

    def pickIndex(self):
        """
        :rtype: int
        """
        random_value = random.random() * self.sum_of_weight
        low = 0
        high = len(self.weight_proportions)

        while low < high:
            mid = low + (high - low) // 2
            if random_value > self.weight_proportions[mid]:
                low = mid + 1
            else:
                high = mid
        return low