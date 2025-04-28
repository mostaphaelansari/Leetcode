# Two Sum - Solution Explanation

## Problem Statement

We are given an array of integers `nums` and an integer `target`. The goal is to return the indices of the two numbers that add up to `target`.

We can assume that there is **exactly one solution** and that we cannot use the same element twice.

**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Solution 1: Brute Force

The simplest solution is to check every possible pair of numbers in the array.

### Algorithm
1. Use two nested loops to iterate through each pair of elements.
2. For each pair, check if their sum equals the `target`.
3. If so, return their indices.

### Implementation
```python
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # If no solution is found
```

### Complexity Analysis
- **Time Complexity**: O(n²), where n is the length of `nums`. We check all possible pairs in the array.
- **Space Complexity**: O(1), as we use only constant extra space.

## Solution 2: Hash Map (Optimal Solution)

A more efficient approach is to use a hash map to reduce time complexity at the cost of extra space.

### Algorithm
1. Create an empty hash map to store numbers and their indices.
2. Iterate through the array once.
3. For each element:
   - Calculate the complement (target - current element).
   - Check if the complement already exists in the hash map.
   - If it does, return the current index and the complement's index.
   - If not, add the current number and its index to the hash map.

### Implementation
```python
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in d:
                return [d[rest], i]
            d[nums[i]] = i
        return []  # If no solution is found
```

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of `nums`. We process each element once.
- **Space Complexity**: O(n) in the worst case, as we may need to store all elements in the hash map.

## Solution 3: Hash Map in Two Passes

A variation of the hash map approach is to use two passes through the array.

### Algorithm
1. First pass: Build the hash map with each element and its index.
2. Second pass: For each element, check if its complement exists in the hash map.

### Implementation
```python
class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        # First pass: build the hash map
        for i, num in enumerate(nums):
            num_map[num] = i
        
        # Second pass: find the complement
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
        return []  # If no solution is found
```

### Complexity Analysis
- **Time Complexity**: O(n), as we process the array twice, but each pass is O(n).
- **Space Complexity**: O(n) for storing the hash map.

## Why the Hash Map Approach is Best

The hash map approach (Solution 2) is the most efficient solution for the "Two Sum" problem because:

1. **Time Efficiency**: It reduces time complexity from O(n²) to O(n) by eliminating the need for a nested loop.
2. **Single Pass**: Unlike the two-pass variation, this solution solves the problem in a single pass through the array.
3. **Space Efficiency**: While it uses O(n) space, the trade-off is worthwhile for the significant improvement in time complexity.

The one-pass hash map solution is particularly effective because it leverages the key insight that we can check for the complement of the current element as we build the hash map, rather than building the map first and then searching.
