'''
**Find the Duplicate Number

Given an array of integers nums containing n + 1 integers 
    where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums
    and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely
    one integer which appears two or more times.
'''
'''
# 80ms used runtime - code in leetcode
sys.stdout = open('user.out', 'w')
for nums in map(loads, sys.stdin):
    print(Counter(nums).most_common(1)[0][0])
'''

# Here the array changes
def findDuplicate(nums):
        for i in range(len(nums)):
            ind = abs(nums[i])
            if nums[ind] < 0:
                return ind
            nums[ind] = -nums[ind]
        return -1

nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))


# The Required one
def findDuplicate_(nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

nums = [3, 1, 3, 4, 2]
print(findDuplicate_(nums))