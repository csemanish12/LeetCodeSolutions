class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        to_city_a = n/2
        to_city_b = n/2
        for i in range(n):
            for j in range(n-1):
                if abs(costs[j][0] - costs[j][1]) < abs(abs(costs[j+1][0] - costs[j+1][1])):
                    costs[j], costs[j+1] = costs[j+1], costs[j]

        print(costs)
        sum = 0
        for i in range(n):
            if to_city_b == 0 or (costs[i][0] <= costs[i][1] and to_city_a > 0):
                sum += costs[i][0]
                to_city_a -= 1

            else:
                sum += costs[i][1]
                to_city_b -= 1
        return sum

