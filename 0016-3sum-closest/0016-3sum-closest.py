class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1

            while i < j:
                total = nums[k] + nums[i] + nums[j]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total > target:
                    j -= 1
                elif total < target:
                    i += 1
                else:
                    return target

        return closest