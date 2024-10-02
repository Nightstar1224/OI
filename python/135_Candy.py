class Solution:
    def candy(self, ratings: List[int]) -> int:
        # wrong answer
        # # [1,2,2] 1,0
        # # [1,0,2] -1,1
        # direction = []
        # for ii in range(1, len(ratings)):
        #     if ratings[ii - 1] < ratings[ii]:
        #         inc_or_dec = 1
        #     elif ratings[ii - 1] == ratings[ii]:
        #         inc_or_dec = 0
        #     else:
        #         inc_or_dec = 0
        #     direction.append(inc_or_dec)
        # lr_squished = [0 for _ in ratings]
        # for ii in range(1, len(ratings)):
        #     lr_squished[ii] = lr_squished[ii - 1] + direction[ii - 1]
        # print(squished)
        # valley = min(squished)
        # return sum(squished) + len(ratings) * (1 - valley)

        # avs
        lr_squished = [0 for _ in ratings]
        rl_squished = [0 for _ in ratings]
        for ii in range(1, len(ratings)):
            lr_squished[ii] = lr_squished[ii - 1] + 1 if ratings[ii - 1] < ratings[ii] else 0
        lr_valley = min(lr_squished)
        for ii in range(len(ratings) - 2, -1, -1):
            rl_squished[ii] = rl_squished[ii + 1] + 1 if ratings[ii] > ratings[ii + 1] else 0
        rl_valley = min(rl_squished)
        n_candies = 0
        for ii in range(len(ratings)):
            n_candies += max(lr_squished[ii] - lr_valley, rl_squished[ii] - rl_valley) + 1
        # print(lr_squished, lr_valley, rl_squished, rl_valley)
        return n_candies
