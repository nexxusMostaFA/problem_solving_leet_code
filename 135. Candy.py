class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        l = 0
        r = 1
        candies = [1] * n

        while l < n and r < n:
            if ratings[l] < ratings[r]:
                candies[r] = candies[l] + 1
            l += 1
            r += 1

        l = n - 2
        r = n - 1
        while l >= 0:
            if ratings[l] > ratings[r]:
                candies[l] = max(candies[l], candies[r] + 1)
            l -= 1
            r -= 1

        return sum(candies)

