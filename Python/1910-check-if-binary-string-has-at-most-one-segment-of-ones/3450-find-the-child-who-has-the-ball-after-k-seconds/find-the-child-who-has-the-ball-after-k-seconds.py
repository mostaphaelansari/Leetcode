class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # The ball bounces back and forth, creating a cycle
        # Pattern: 0 -> 1 -> 2 -> ... -> (n-1) -> (n-2) -> ... -> 1 -> 0 -> ...
        # This cycle has length 2(n-1)
        
        cycle_length = 2 * (n - 1)
        position_in_cycle = k % cycle_length
        
        # In the first half of cycle: 0, 1, 2, ..., n-1
        # In the second half of cycle: n-2, n-3, ..., 1
        
        if position_in_cycle < n:
            # First half: moving right from 0 to n-1
            return position_in_cycle
        else:
            # Second half: moving left from n-1 to 1 (then back to 0)
            # position_in_cycle - (n-1) gives us how many steps into the return journey
            return n - 1 - (position_in_cycle - (n - 1))