from typing import List, MutableMapping


class Solution:
    def canTraverseAllPairs2(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        connected_primes = []
        for num in nums:
            if num == 1:
                # 1 cannot have denominator higher than 1
                return False

            # get the primes for num
            temp = num
            primes = set()
            for j in range(2, int(num ** 0.5) + 1):
                if temp % j == 0:
                    primes.add(j)
                    while temp % j == 0:
                        temp //= j
            if temp > 1:
                primes.add(temp)

            size = len(primes)
            t_primes = []
            c_primes = [primes]
            for pset in connected_primes:
                diff = primes - pset
                dsize = len(diff)
                if (not dsize) and len(c_primes) == 1:
                    # "num" primes are all connected already
                    t_primes = connected_primes
                    c_primes.clear()
                    break
                if dsize == size:
                    # the sets have nothing in common
                    t_primes.append(pset)
                else:
                    # there is something in common, try finding the rest
                    c_primes.append(pset)
                    # only look for what is not already in the pset we just went through
                    primes = diff
                    size = len(primes)
            # connect all sets that had something in common
            if c_primes:
                merged = set()
                merged.update(*c_primes)
                t_primes.append(merged)
            connected_primes = t_primes
                
        return True if len(connected_primes) == 1 else False

    index2prime : MutableMapping[int, List[int]]
    prime2index : MutableMapping[int, List[int]]

    def __dfs(self, index: int, visited_nums: List[bool], visited_primes: MutableMapping[int, bool]):
        if visited_nums[index]:
            return
        visited_nums[index] = True
        for p in self.index2prime[index]:
            if visited_primes.get(p, False):
                continue
            visited_primes[p] = True
            for i in self.prime2index[p]:
                if visited_nums[i]:
                    continue
                self.__dfs(i, visited_nums, visited_primes)
        return

    def factorsCalculator(self, n: int) -> List[int]:
        dp = list(range(n + 2))
        for i in range(2, n + 1):
            if dp[i] == i:
                for j in range(i * 2, n + 1, i):
                    if dp[j] == j:
                        dp[j] = i
        return dp

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        maxNumber = max(nums)
        if min(nums) == 1:
            return False
        factors = self.factorsCalculator(maxNumber)

        self.index2prime = {}
        self.prime2index = {}
        for i, num in enumerate(nums):
            temp = num
            while temp > 1:
                p = factors[temp]
                self.index2prime.setdefault(i, []).append(p)
                self.prime2index.setdefault(p, []).append(i)
                while temp % p == 0:
                    temp //= p

        visited_nums = [False] * len(nums)
        visited_primes = {}
        self.__dfs(0, visited_nums, visited_primes)
        return all(visited_nums)

testCases = [
    [42, 40, 45, 42, 50, 33, 30, 45, 33, 45, 30, 36, 44, 1, 21, 10, 40, 42, 42],
    [21, 88, 75],
    [2, 3, 6],
    [3, 9, 5],
    [4, 3, 12, 8],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.canTraverseAllPairs(test)}')
    print(f'{test}: {s.canTraverseAllPairs2(test)}')
