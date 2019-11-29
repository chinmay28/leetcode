

class Solution(object):

    def balanced_buckets(self, nums, pcount):
        self.nums = nums
        self.pcount = pcount
        self.part_sum, remainder = divmod(sum(nums), pcount)
        self.psums = [0] * pcount
        self.results = []
        self.no_insert = True
        self.holes = [max(nums) for _ in range(pcount)]

        # nums are sorted
        part_list = [[] for _ in range(pcount)]
        print part_list
        result = self.make_partitions(part_list)

        self.psums.sort()
        if result and self.nums:
            for i, num in enumerate(self.nums):
                self.psums[i % pcount] += num
                self.results[i % pcount].append(num)

        print self.psums, self.results

    def make_partitions(self, part_list):
        if not self.nums:  # all nums are used
            self.results = part_list
            return True

        if max(self.holes) < min(self.nums):
            # extra numbers
            self.results = part_list
            return True

        item = self.nums.pop()
        for i, psum in enumerate(self.psums):
            self.no_insert = True
            if psum + item <= self.part_sum:
                self.psums[i] += item
                part_list[i].append(item)
                self.holes[i] -= item
                self.no_insert = False
                if self.make_partitions(part_list):
                    return True
                self.psums[i] -= item
                part_list[i].remove(item)
                self.holes[i] += item
            if not psum:
                # we finished all nums and one of the psums is empty
                break
        # put the item back to the list for a new combination
        self.nums.append(item)
        return False


a = [2,3,4,5,4,3]
Solution().balanced_buckets(sorted(a), 2)
