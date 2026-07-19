class Solution:
    def jump(self, nums: List[int]) -> int: # Changed name from findMinJumps to jump
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            # Scout the best possible future landing spot
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of our current reach, we MUST jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
                # Tiny optimization: if we can already reach the end, stop looking
                if current_jump_end >= len(nums) - 1:
                    break
                
        return jumps