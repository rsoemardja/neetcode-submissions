class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0  # Max money up to house i - 2 💰
        rob2 = 0  # Max money up to house i - 1 💰

        for n in nums:
            # Decision: rob current house + rob1 OR skip current house (keep rob2) 💡
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2