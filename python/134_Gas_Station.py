class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # TLE
        # # 找gas - cost的序列，累计和始终>=0
        # remain = [gas[ii] - cost[ii] for ii in range(len(gas))]
        # # acc_sum = [[0 for ii in gas] for jj in gas]
        # # for ii in range(len(gas)):
        # #     acc_sum[ii][ii] = remain[ii]
        # for start in range(len(remain)):
        #     # if remain[start] < 0:
        #     #     continue
        #     # acc_sum = remain[start]
        #     acc_sum = 0
        #     for offset in range(len(remain)):
        #         # acc_sum[start][end] = acc_sum[start][(end-1)%len(remain)] + remain[end]
        #         # if acc_sum[start][end] < 0:
        #         #     break
        #         end = (start + offset) % len(remain)
        #         acc_sum += remain[end]
        #         if acc_sum < 0:
        #             break
        #         if offset == len(remain) - 1:
        #             return start
        # return -1        # 找gas - cost的序列，累计和始终>=0

        # remain = [gas[ii] - cost[ii] for ii in range(len(gas))]
        # start, end = 0, 0
        # s = 0
        # while True:
        #     s += remain[end]
        #     end = (end + 1) % len(gas)
        #     # if s < 0:
        #     while start != end and s < 0:
        #         s -= remain[start]
        #         start = (start + 1) % len(gas)
        #     if start == (end + 1) % len(gas) and s >= -remain[(end + 1) % len(gas)]:
        #         return start
        #     print(remain, start, end, s)
        # return -1

        # submission 1 avs inequation
        # 如果x到达不了y+1，那么x-y之间的点也不可能到达y+1，因为中间任何一点的油都是拥有前面的余量的，所以下次遍历直接从y+1开始
        remain = [gas[ii] - cost[ii] for ii in range(len(gas))]
        start = 0
        while start < len(gas):
            # if remain[start] < 0:
            #     continue
            # acc_sum = remain[start]
            acc_sum = 0
            offset = 0
            while offset < len(gas):
            # for offset in range(len(remain)):
                end = (start + offset) % len(remain)
                acc_sum += remain[end]
                if acc_sum < 0:
                    # start = end
                    break
                offset += 1
            if offset == len(remain):
                return start
            start += offset + 1
        return -1  # 找gas - cost的序列，累计和始终>=0
